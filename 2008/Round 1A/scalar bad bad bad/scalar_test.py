from scalar import solve, product


def test_product():
    assert product([1, 3, -5], [-2, 4, 1]) == 5
    assert product([1, 2, 3, 4, 5], [1, 0, 1, 0, 1]) == 9


def test_sample1():
    assert solve([1, 3, -5], [-2, 4, 1]) == -25


def test_sample2():
    assert solve([1, 2, 3, 4, 5], [1, 0, 1, 0, 1]) == 6


def test_other():
    assert solve([5, 4, 1], [2, 4, 1]) == 17
    assert solve([6, 4, 1], [1, 5, 2]) == 19
    assert solve([5, 4], [2, 1]) == 13
    assert solve([1], [5]) == 5
    assert solve([1, 2, 3, 4, 5], [1, -1, 1, -1, 1]) == -3
    assert solve([-1, 0], [0, -1]) == 0
    assert solve([0], [0]) == 0
    assert solve([-5, -20], [-5, -2]) == 65
    # assert solve([], []) ==
