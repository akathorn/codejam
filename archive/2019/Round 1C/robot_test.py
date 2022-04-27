import robot
import random
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
# in_str = ("""
# 3
# 3 2
# 1 2
# 4 2
# """)
# out_str = ("""
# Case #1: 0
# Case #2: 0
# Case #3: 0
# """)
in_str = ("""
3
1
RS
3
R
P
S
7
RS
RS
RS
RS
RS
RS
RS
""")
out_str = ("""
Case #1: RSRSRSP
Case #2: IMPOSSIBLE
Case #3: P
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("robot.Input")
    mock_write = mocker.patch("robot.Output")
    _ = mocker.patch("robot.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    robot.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    sol = robot.solve(["RS"])
    assert sol
    assert robot.compare_program(sol, "RS") == 1


def test_2():
    assert robot.solve(["R", "P", "S"]) == None


def test_3():
    programs = ["RS"] * 7
    sol = robot.solve(programs)
    assert sol
    assert all(robot.compare_program(sol, program) == 1 for program in programs)


def test_too_big():
    programs = ["P" * 100, "P" * 100]
    sol = "R" * 100
    all(robot.compare_program(sol, program) == 1 for program in programs)
    sol = robot.solve(programs)
    assert sol == None


def test_random_small():
    random.seed(5)
    for _ in range(10000):
        programs = []
        for _ in range(7):
            program = "".join(
                [["R", "P", "S", ""][random.randint(0, 3)] for _ in range(5)]
            )
            if program:
                programs.append(program)
        sol = robot.solve(programs)
        if sol:
            assert all(robot.compare_program(sol, program) == 1 for program in programs)


def test_random():
    programs = [
        "".join([["R", "P", "S"][random.randint(0, 2)] for _ in range(500)])
        for _ in range(255)
    ]
    sol = robot.solve(programs)
    if sol:
        assert all(robot.compare_program(sol, program) == 1 for program in programs)


def test_profiling():
    ...
