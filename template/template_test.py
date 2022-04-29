import template
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
[INPUT]
""")
out_str = ("""
[OUTPUT]
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
SOLUTION_IS_FLOAT = ...


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("template.Input")
    mock_write = mocker.patch("template.Output")
    _ = mocker.patch("template.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    template.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        if SOLUTION_IS_FLOAT:
            expected = float(call[1][0].strip().split()[-1])
            result = float(out.split()[-1])
            assert IsApproximatelyEqual(result, expected, 10 ** -6)
        else:
            assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_profiling():
    ...
