import queue
import random
import threading
import pytest
from typing import Any, Callable, List, Optional
from unittest import mock
import arrangers
import arrangers_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


# Value used by the judge to indicate a wrong answer/interaction


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

    _read: mock.MagicMock = mocker.patch("arrangers.Input", wraps=judge.output)
    write: mock.MagicMock = mocker.patch("arrangers.Output", wraps=judge.input)

    try:
        arrangers.solve_case(...)
    except arrangers.EndInteractive:
        ...

    calls = ["first call", "second call", ...]
    write.assert_has_calls([mock.call(c) for c in calls], any_order=False)


def test_wrong_answer(mocker: MockerFixture):
    read: mock.MagicMock = mocker.patch("sys.stdin.readline")
    read.side_effect = [arrangers.WRONG_ANSWER]

    with pytest.raises(arrangers.EndInteractive):
        arrangers.solve_case(...)


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
        self.sol_read = mocker.patch("arrangers.Input", wraps=Input(self.judge_sol_queue, timeout))  # type: ignore
        self.sol_write = mocker.patch("arrangers.Output", wraps=Output(self.sol_judge_queue))  # type: ignore
        self.sol_read = mocker.patch("arrangers.Finalize")  # type: ignore
        self.judge_read = mocker.patch("arrangers_judge.Input", wraps=Input(self.sol_judge_queue, timeout))  # type: ignore
        self.judge_write = mocker.patch("arrangers_judge.Output", wraps=Output(self.judge_sol_queue))  # type: ignore


def test_threads(mocker: MockerFixture):
    random.seed(1)

    IO = FakeIO(mocker, timeout=None)
    test_number = 0

    # The judge will send these lines before actually starting (usually the number of test cases)
    # initial_input: List[str] = []
    # for line in initial_input:
    #     IO.judge_sol_queue.put(line)

    # # Start judge
    # args = [test_number, arrangers_judge.IO()]  # Args for the judge
    # thread = threading.Thread(target=arrangers_judge.JudgeAllCases, args=args)

    initial_input: List[str] = ["1 1000"]
    for line in initial_input:
        IO.judge_sol_queue.put(line)

    case = arrangers_judge.JudgeSingleCase(1000, arrangers_judge.IO())
    thread = threading.Thread(target=case.Judge)
    thread.start()

    # Start solution
    arrangers.main()

    # Wrap up
    IO.done = True
    thread.join()

    # Check the last response
    assert IO.judge_write.mock_calls[-1] != mocker.call(arrangers.WRONG_ANSWER)
