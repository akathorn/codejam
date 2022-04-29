import edgy
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
4
1 7
1 1
2 920
50 120
50 120
1 32
7 4
3 240
10 20
20 30
30 10
""")
out_str = ("""
Case #1: 6.828427
Case #2: 920.000000
Case #3: 32.000000
Case #4: 240.000000
""")
# fmt: on


def IsApproximatelyEqual(x, y, epsilon):
    """Returns True if y is within relative or absolute 'epsilon' of x."""
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return -epsilon <= (x - y) / x <= epsilon or -epsilon <= (x - y) / y <= epsilon


# How to parse the sample input/output (e.g. str(), float()...)
SOLUTION_IS_FLOAT = True


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("edgy.Input")
    mock_write = mocker.patch("edgy.Output")
    _ = mocker.patch("edgy.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    edgy.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        if SOLUTION_IS_FLOAT:
            expected = float(call[1][0].strip().split()[-1])
            result = float(out.split()[-1])
            assert IsApproximatelyEqual(result, expected, 10 ** -6)
        else:
            assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_set_1_random():
    W = random.randint(1, 250)
    H = random.randint(1, 250)


def test_profiling():
    ...
