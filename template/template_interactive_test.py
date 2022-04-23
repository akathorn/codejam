import queue
import random
import threading
import pytest
from typing import Any, Callable, List, Optional
from unittest import mock
import template
import template_judge
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

    _read: mock.MagicMock = mocker.patch("template.Input", wraps=judge.output)
    write: mock.MagicMock = mocker.patch("template.Output", wraps=judge.input)

    try:
        template.solve_case(...)
    except template.EndInteractive:
        ...

    calls = ["first call", "second call", ...]
    write.assert_has_calls([mock.call(c) for c in calls], any_order=False)


def test_wrong_answer(mocker: MockerFixture):
    read: mock.MagicMock = mocker.patch("sys.stdin.readline")
    read.side_effect = [-1]

    with pytest.raises(template.EndInteractive):
        template.solve_case(...)


def test_threads(mocker: MockerFixture):
    done: bool = False

    cases: Any = ...
    initial_input: List[str] = [f"{len(cases)} ..."]
    ## Set timeout to None to disable it
    timeout: Optional[int] = 3

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

    sol_read = mocker.patch("template.Input", wraps=Input(judge_sol_queue, timeout))  # type: ignore
    sol_write = mocker.patch("template.Output", wraps=Output(sol_judge_queue))  # type: ignore
    sol_read = mocker.patch("template.Finalize")  # type: ignore
    judge_read = mocker.patch("template_judge.Input", wraps=Input(sol_judge_queue, timeout))  # type: ignore
    judge_write = mocker.patch("template_judge.Output", wraps=Output(judge_sol_queue))  # type: ignore

    thread = threading.Thread(target=template_judge.RunCases)
    thread.start()

    template.main()
    done = True
    thread.join()

    assert judge_write.mock_calls[-1] == mocker.call(1)
