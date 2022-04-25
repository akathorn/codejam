import queue
import random
import threading
import pytest
from typing import Any, Callable, List, Optional
from unittest import mock
import asedatab
import asedatab_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


class MockJudge:
    def __init__(self, case: Any) -> None:
        self.out: List[str] = []  # Put initial messages here
        ...

    def input(self, msg: Any):
        # Process msg
        ...

        # Prepare response
        response: Any = ...
        self.out.append(str(response))

    def output(self) -> str:
        ...

        return self.out.pop(0)


def test_mock(mocker: MockerFixture):
    case: Any = ...
    judge = MockJudge(case)

    _read: mock.MagicMock = mocker.patch("asedatab.Input", wraps=judge.output)
    write: mock.MagicMock = mocker.patch("asedatab.Output", wraps=judge.input)

    try:
        asedatab.solve_case(...)
    except asedatab.EndInteractive:
        ...

    calls = ["first call", "second call", ...]
    write.assert_has_calls([mock.call(c) for c in calls], any_order=False)


def test_wrong_answer(mocker: MockerFixture):
    read: mock.MagicMock = mocker.patch("sys.stdin.readline")
    read.side_effect = [-1]

    with pytest.raises(asedatab.EndInteractive):
        asedatab.solve_case(...)


def test_threads(mocker: MockerFixture):
    done: bool = False

    # cases: Any = ...
    initial_input: List[str] = ["100"]
    ## Set timeout to None to disable it
    timeout: Optional[int] = None

    def Input(q: "queue.Queue[str]", timeout: Optional[int]) -> Callable[..., str]:
        def f() -> str:
            if done:
                raise EOFError
            try:
                return q.get(timeout=timeout)
            except queue.Empty:
                raise queue.Empty(f"Communication deadlocked after {timeout}s")

        return f

    def Output(q: "queue.Queue[str]") -> Callable[..., None]:
        def f(s: Any):
            return q.put(str(s))

        return f

    sol_judge_queue: "queue.Queue[str]" = queue.Queue()
    judge_sol_queue: "queue.Queue[str]" = queue.Queue()
    for line in initial_input:
        judge_sol_queue.put(line)

    sol_read = mocker.patch("asedatab.Input", wraps=Input(judge_sol_queue, timeout))  # type: ignore
    sol_write = mocker.patch("asedatab.Output", wraps=Output(sol_judge_queue))  # type: ignore
    sol_read = mocker.patch("asedatab.Finalize")  # type: ignore
    judge_read = mocker.patch("asedatab_judge.Input", wraps=Input(sol_judge_queue, timeout))  # type: ignore
    judge_write = mocker.patch("asedatab_judge.Output", wraps=Output(judge_sol_queue))  # type: ignore

    thread = threading.Thread(target=asedatab_judge.RunCases, args=[100])
    thread.start()

    asedatab.main()
    done = True
    thread.join()

    assert judge_write.mock_calls[-1] == mocker.call(1)
