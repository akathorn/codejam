import rounding
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
3 2
1 1
10 3
1 3 2
6 2
3 1
9 8
1 1 1 1 1 1 1 1
""")
out_str = ("""
Case #1: 100
Case #2: 100
Case #3: 101
Case #4: 99
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
SOLUTION_IS_FLOAT = False


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("rounding.Input")
    mock_write = mocker.patch("rounding.Output")
    _ = mocker.patch("rounding.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    rounding.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        if SOLUTION_IS_FLOAT:
            expected = float(call[1][0].strip().split()[-1])
            result = float(out.split()[-1])
            assert IsApproximatelyEqual(result, expected, 10 ** -6)
        else:
            assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_2():
    assert rounding.solve(10, [1, 3, 2]) == 100


def test_profiling():
    N = 10 ** 5 + 1
    C = [1]
    rounding.solve(N, C)
