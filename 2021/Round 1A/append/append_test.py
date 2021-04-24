from append import solve


def test_sample1():
    assert solve([100, 7, 10]) == 4
    assert solve([10, 10]) == 1
    assert solve([4, 19, 1]) == 2
    assert solve([1, 2, 3]) == 0


def test_1():
    assert solve([7, 7, 7]) == 2
    assert solve([10, 1, 3]) == 2
    assert solve([699, 7]) == 2
    assert solve([699, 5]) == 3
    assert solve([698, 6]) == 2
    assert solve([603, 60]) == 1


def test_2():
    assert solve([17, 1, 1, 1]) == 4
    assert solve([10, 1, 1, 1]) == 3
    assert solve([10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    #                10 11 12 13 14 15 16 17 18 19 100