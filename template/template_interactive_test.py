import queue
import random
import threading
import pytest
from typing import Any, Callable, List, Optional
from unittest import mock
import template
import template_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


# Value used by the judge to indicate a wrong answer/interaction
WRONG_ANSWER = -1


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
    read.side_effect = [WRONG_ANSWER]

    with pytest.raises(template.EndInteractive):
        template.solve_case(...)


class FakeIO:
    def __init__(self, mocker: MockerFixture, timeout: Optional[int] = 3):
        ##### SETUP I/O ####
        self.done: bool = False

        def Input(q: "queue.Queue[str]", timeout: Optional[int]) -> Callable[..., str]:
            def f() -> str:
                if self.done:
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

        self.sol_judge_queue: "queue.Queue[str]" = queue.Queue()
        self.judge_sol_queue: "queue.Queue[str]" = queue.Queue()
        self.sol_read = mocker.patch("template.Input", wraps=Input(self.judge_sol_queue, timeout))  # type: ignore
        self.sol_write = mocker.patch("template.Output", wraps=Output(self.sol_judge_queue))  # type: ignore
        self.sol_read = mocker.patch("template.Finalize")  # type: ignore
        self.judge_read = mocker.patch("template_judge.Input", wraps=Input(self.sol_judge_queue, timeout))  # type: ignore
        self.judge_write = mocker.patch("template_judge.Output", wraps=Output(self.judge_sol_queue))  # type: ignore


def test_threads(mocker: MockerFixture):
    IO = FakeIO(mocker, timeout=3)

    # The judge will send these lines before actually starting (usually the number of test cases)
    initial_input: List[str] = ["# test cases"]
    for line in initial_input:
        IO.judge_sol_queue.put(line)

    # Start judge
    args = [...]  # Args for the judge
    thread = threading.Thread(target=template_judge.RunCases, args=args)
    thread.start()

    # Start solution
    template.main()

    # Wrap up
    IO.done = True
    thread.join()

    # Check the last response
    assert IO.judge_write.mock_calls[-1] != mocker.call(WRONG_ANSWER)
