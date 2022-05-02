import squary
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
2 1
-2 6
2 1
-10 10
1 1
0
3 1
2 -2 2
""")
out_str = ("""
Case #1: 3
Case #2: IMPOSSIBLE
Case #3: -1000000000000000000
Case #4: 2
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
    mock_read = mocker.patch("squary.Input")
    mock_write = mocker.patch("squary.Output")
    _ = mocker.patch("squary.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    squary.main()

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
    assert squary.solve([-10, 10], 1) == None


def test_random():
    s = 0
    for _ in range(10000):
        N = 100
        E = [random.randint(0, 10) for _ in range(N)]
        K = squary.solve(E, 1)
        if K:
            s += 1
            E.extend(K)
            assert sum(E) ** 2 == sum(e ** 2 for e in E)


def test_profiling():
    ...
