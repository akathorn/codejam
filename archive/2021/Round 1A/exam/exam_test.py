from fractions import Fraction
from fractions import Fraction
from exam import solve


def test_sample1():
    answers, fraction = solve([([False, False, True], 3)])
    result = "".join("T" if a else "F" for a in answers)
    assert result == "FFT"
    assert fraction == Fraction(3, 1)
