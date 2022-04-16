import random
import crepe
from pytest_mock import mocker, MockerFixture  # type: ignore

# pytest_plugins = ["pytest_profiling"]

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
1 10
5 5 N
4 10
2 4 N
2 6 S
1 5 E
3 5 W
8 10
0 2 S
0 3 N
0 3 N
0 4 N
0 5 S
0 5 S
0 8 S
1 5 W
""")
out_str = ("""
Case #1: 0 6
Case #2: 2 5
Case #3: 0 4
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("crepe.Input")
    mock_write = mocker.patch("crepe.Output")
    _ = mocker.patch("crepe.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    crepe.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_a():
    # fmt: off
    case_txt = \
"""
5 5 N
"""
    case = [line.split() for line in case_txt.strip().split("\n")]
    # fmt: on
    assert crepe.solve(case, 10) == (0, 6)


def test_b():
    # fmt: off
    case_txt = \
"""
2 4 N
2 6 S
1 5 E
3 5 W
"""
    case = [line.split() for line in case_txt.strip().split("\n")]
    # fmt: on
    assert crepe.solve(case, 10) == (2, 5)


def test_c():
    # fmt: off
    case_txt = \
"""
0 2 S
0 3 N
0 3 N
0 4 N
0 5 S
0 5 S
0 8 S
1 5 W
"""
    case = [line.split() for line in case_txt.strip().split("\n")]
    # fmt: on
    crepe.solve(case, 10)


def test_random():
    random.seed(1)
    Q = 10
    P = 2
    persons = []
    crepes_x = random.randint(0, Q)
    crepes_y = random.randint(0, Q)
    for _ in range(P):
        x, y = random.randint(0, Q), random.randint(0, Q)
        while (x, y) == (crepes_x, crepes_y):
            x, y = random.randint(0, Q), random.randint(0, Q)
        if random.random() < 0:
            d = ["N", "S", "W", "E"][random.randint(0, 3)]
        elif random.random() < 0.5:
            d = "W" if crepes_x < x else "E"
        else:
            d = "S" if crepes_y < y else "N"
        persons.append([x, y, d])
    assert crepe.solve(persons, Q) == (crepes_x, crepes_y)


def test_profiling():
    Q = 100000
    dirs = ["N", "S", "W", "E"]
    persons = []
    for _ in range(500):
        x, y = str(random.randint(0, Q)), str(random.randint(0, Q))
        d = dirs[random.randint(0, 3)]
        persons.append([x, y, d])
    crepe.solve(persons, Q)