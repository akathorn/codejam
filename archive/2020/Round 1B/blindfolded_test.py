import queue
import random
import threading
import pytest
from typing import Any, Callable, List, Optional, Tuple
from unittest import mock
import blindfolded
import blindfolded_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


class MockJudge:
    def __init__(self, center: Tuple[int, int], R: int) -> None:
        self.out: List[str] = []  # Put initial messages here
        self.center = center
        self.R = R
        self.hit = False

    def input(self, msg: Any):
        # Process msg
        if msg == f"{self.center[0]} {self.center[1]}":
            response = "CENTER"
            self.hit = True
        else:
            response = "MISS"

        self.out.append(str(response))

    def output(self) -> str:
        return self.out.pop(0)


def test_mock(mocker: MockerFixture):
    center = (random.randint(-5, 5), random.randint(-5, 5))
    # center = (8, 8)
    R = int(10e9 - 5)

    judge = MockJudge(center, R)

    _read: mock.MagicMock = mocker.patch("blindfolded.Input", wraps=judge.output)
    write: mock.MagicMock = mocker.patch("blindfolded.Output", wraps=judge.input)

    try:
        blindfolded.solve_case(R, R)
    except blindfolded.EndInteractive:
        ...

    assert judge.hit

    # calls = ["first call", "second call", ...]
    # write.assert_has_calls([mock.call(c) for c in calls], any_order=False)


def test_wrong_answer(mocker: MockerFixture):
    read: mock.MagicMock = mocker.patch("sys.stdin.readline")
    read.side_effect = ["WRONG"]

    with pytest.raises(blindfolded.EndInteractive):
        blindfolded.solve_case(10, 20)


def test_max_queries(mocker: MockerFixture):
    read: mock.MagicMock = mocker.patch("blindfolded.Input")
    _write: mock.MagicMock = mocker.patch("blindfolded.Output")
    read.side_effect = ["MISS"] * 300

    with pytest.raises(blindfolded.EndInteractive):
        blindfolded.solve_case(10, 10)

    # Resets for next case
    read.side_effect = ["MISS"] * 299 + ["CENTER"]
    blindfolded.solve_case(10, 10)


def test_threads(mocker: MockerFixture):
    done: bool = False

    D = 300
    minr, maxr, cases = (
        blindfolded_judge.MINR[0],
        blindfolded_judge.MAXR[0],
        blindfolded_judge.CASES[0],
    )

    initial_input: List[str] = []  # [f"{len(cases)} ..."]
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

    sol_read = mocker.patch("blindfolded.Input", wraps=Input(judge_sol_queue, timeout))  # type: ignore
    sol_write = mocker.patch("blindfolded.Output", wraps=Output(sol_judge_queue))  # type: ignore
    sol_read = mocker.patch("blindfolded.Finalize")  # type: ignore
    judge_read = mocker.patch("blindfolded_judge.Input", wraps=Input(sol_judge_queue, timeout))  # type: ignore
    judge_write = mocker.patch("blindfolded_judge.Output", wraps=Output(judge_sol_queue))  # type: ignore

    thread = threading.Thread(
        target=blindfolded_judge.RunCases, args=(D, minr, maxr, cases)
    )
    thread.start()

    blindfolded.main()
    done = True
    thread.join()

    assert judge_write.mock_calls[-1] == mocker.call("CENTER")
