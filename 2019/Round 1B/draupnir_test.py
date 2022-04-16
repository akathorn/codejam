import math
import queue
import random
import threading
from typing import Optional
import draupnir
import draupnir_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


def generate_case(seed=None):
    random.seed(seed)
    solution = [random.randint(0, 100) for _ in range(6)]
    return generate_days(solution), solution


def generate_days(solution):
    rings = [solution]
    if sum(rings[0]) == 0:
        rings[0][random.randint(0, 5)] = 1

    for day in range(1, 501):
        rings.append(list(rings[-1]))
        for i in range(6):
            if day % (i + 1) == 0:
                rings[-1][i] *= 2

    case = [sum(r) for r in rings]
    return case


class FakeJudge:
    def __init__(self, case, solution) -> None:
        self.case = case
        self.solution = solution
        self.out = []
        self.guess = None

    def input(self, n):
        if isinstance(n, str):
            self.guess = [int(s) for s in n.split()]
            return
        assert 1 <= n <= 500
        self.out.append(self.case[n] % (2 ** 63))

    def output(self):
        if self.guess:
            return 1 if self.guess == self.solution else -1
        else:
            return self.out.pop(0)


def test_random(mocker: MockerFixture):
    seed = None
    case, solution = generate_case(seed)

    judge = FakeJudge(case, solution)
    read = mocker.patch("draupnir.Input", wraps=judge.output)
    write = mocker.patch("draupnir.Output", wraps=judge.input)

    try:
        draupnir.solve_case(6)
    except draupnir.EndInteractive:
        pass

    write.assert_called_with(" ".join([str(r) for r in solution]))

    # calls = map(mocker.call, [4])
    # write.assert_has_calls(calls, any_order=False)


def test_simple(mocker: MockerFixture):
    solution = [1, 1, 1, 1, 1, 1]
    case = generate_days(solution)

    judge = FakeJudge(case, solution)
    read = mocker.patch("draupnir.Input", wraps=judge.output)
    write = mocker.patch("draupnir.Output", wraps=judge.input)

    try:
        draupnir.solve_case(6)
    except draupnir.EndInteractive:
        pass

    write.assert_called_with(" ".join([str(r) for r in solution]))


def test_judge(mocker: MockerFixture):
    done = False
    w = 6
    cases = draupnir_judge.CASES[0]
    initial_input = [f"{len(cases)} {w}"]
    timeout = None

    def Input(q: queue.Queue, timeout: Optional[int] = 3):
        def f():
            if done:
                raise EOFError
            try:
                return str(q.get(timeout=timeout))
            except queue.Empty:
                raise queue.Empty(f"Communication deadlocked after {timeout}s")

        return f

    def Output(q: queue.Queue):
        def f(s):
            return q.put(s)

        return f

    sol_judge_queue = queue.Queue()
    judge_sol_queue = queue.Queue()
    for line in initial_input:
        judge_sol_queue.put(line)

    sol_read = mocker.patch("draupnir.Input", wraps=Input(judge_sol_queue, timeout))
    sol_write = mocker.patch("draupnir.Output", wraps=Output(sol_judge_queue))
    sol_read = mocker.patch("draupnir.Finalize")
    judge_read = mocker.patch(
        "draupnir_judge.Input", wraps=Input(sol_judge_queue, timeout)
    )
    judge_write = mocker.patch("draupnir_judge.Output", wraps=Output(judge_sol_queue))

    thread = threading.Thread(target=draupnir_judge.RunCases, args=[w, cases])
    thread.start()

    draupnir.main()
    done = True
    thread.join()
    assert judge_write.mock_calls[-1] == mocker.call(1)