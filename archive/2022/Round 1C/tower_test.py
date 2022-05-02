import tower
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
6
5
CODE JAM MIC EEL ZZZZZ
6
CODE JAM MIC EEL ZZZZZ EEK
2
OY YO
2
HASH CODE
6
A AA BB A BA BB
2
CAT TAX
""")
out_str = ("""
Case #1: ZZZZZJAMMICCODEEEL
Case #2: IMPOSSIBLE
Case #3: IMPOSSIBLE
Case #4: IMPOSSIBLE
Case #5: BBBBBAAAAA
Case #6: IMPOSSIBLE
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
    mock_read = mocker.patch("tower.Input")
    mock_write = mocker.patch("tower.Output")
    _ = mocker.patch("tower.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    tower.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        if SOLUTION_IS_FLOAT:
            expected = float(call[1][0].strip().split()[-1])
            result = float(out.split()[-1])
            assert IsApproximatelyEqual(result, expected, 10 ** -6)
        else:
            assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_3():
    assert not tower.solve(["OY", "YO"])


def test_is_megatower():
    assert tower.is_megatower("AAABBBCCC") == True
    assert tower.is_megatower("AAABCBBCCC") == False


def test_profiling():
    L = 2
    N = 30
    towers = [
        "".join(chr(random.randint(65, 65 + 26)) for _ in range(L)) for _ in range(N)
    ]
    tower.solve(towers)
