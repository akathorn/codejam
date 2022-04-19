import math
import queue
import random
import threading
import pytest
from typing import Any, Callable, List, Optional, Tuple
from unittest import mock
import guess

# import guess_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


class MockJudge:
    def __init__(self, A: int, B: int, N: int, solution: int) -> None:
        self.out: List[str] = [f"{A} {B}", f"{N}"]
        self.A = A
        self.B = B
        self.N = N
        self.remaining = N
        self.solution = solution
        self.done = False

    def input(self, msg: Any):
        if self.done:
            raise Exception("Tried to guess after being done")

        if self.remaining <= 0:
            raise Exception(f"Too many guesses: {self.N}")

        # Process msg
        if msg == self.solution:
            response = "CORRECT"
            self.remaining = 0
        elif msg < self.solution:
            response = "TOO_SMALL"
        else:
            response = "TOO_BIG"

        self.out.append(str(response))
        self.remaining -= 1

    def output(self) -> str:
        if self.done:
            raise Exception("Tried to guess after being done")

        return self.out.pop(0)


def test_mock(mocker: MockerFixture):
    A = 0
    B = int(1e9)
    N = math.ceil(math.log(B - A)) + 2
    solution = random.randint(A, B)
    # solution = 0

    judge = MockJudge(A, B, N, solution)

    _read: mock.MagicMock = mocker.patch("guess.Input", wraps=judge.output)
    write: mock.MagicMock = mocker.patch("guess.Output", wraps=judge.input)

    try:
        guess.solve_case()
    except guess.EndInteractive:
        ...

    # calls = ["first call", "second call", ...]
    # write.assert_has_calls([mock.call(c) for c in calls], any_order=False)
    write.assert_called_with(solution)


def test_wrong_answer(mocker: MockerFixture):
    read: mock.MagicMock = mocker.patch("sys.stdin.readline")
    read.side_effect = ["1 10", "5", "TOO_SMALL", "WRONG_ANSWER"]

    with pytest.raises(guess.EndInteractive):
        guess.solve_case()


# def test_threads(mocker: MockerFixture):
#     done: bool = False

#     cases: Any = ...
#     initial_input: List[str] = [f"{len(cases)} ..."]
#     ## Set timeout to None to disable it
#     timeout: Optional[int] = 3

#     def Input(q: "queue.Queue[str]", timeout: Optional[int]) -> Callable[..., str]:
#         def f() -> str:
#             if done:
#                 raise EOFError
#             try:
#                 return q.get(timeout=timeout)
#             except queue.Empty:
#                 raise queue.Empty(f"Communication deadlocked after {timeout}s")

#         return f

#     def Output(q: "queue.Queue[str]") -> Callable[..., None]:
#         def f(s: Any):
#             return q.put(str(s))

#         return f

#     sol_judge_queue: "queue.Queue[str]" = queue.Queue()
#     judge_sol_queue: "queue.Queue[str]" = queue.Queue()
#     for line in initial_input:
#         judge_sol_queue.put(line)

#     sol_read = mocker.patch("guess.Input", wraps=Input(judge_sol_queue, timeout))  # type: ignore
#     sol_write = mocker.patch("guess.Output", wraps=Output(sol_judge_queue))  # type: ignore
#     sol_read = mocker.patch("guess.Finalize")  # type: ignore
#     judge_read = mocker.patch("guess_judge.Input", wraps=Input(sol_judge_queue, timeout))  # type: ignore
#     judge_write = mocker.patch("guess_judge.Output", wraps=Output(judge_sol_queue))  # type: ignore

#     thread = threading.Thread(target=guess_judge.RunCases)
#     thread.start()

#     guess.main()
#     done = True
#     thread.join()

#     assert judge_write.mock_calls[-1] == mocker.call(1)