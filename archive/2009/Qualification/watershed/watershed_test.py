import watersheds
import random


def test_sample1():
    _map = [[9, 6, 3], [5, 9, 6], [3, 5, 9]]
    assert watersheds.solve(3, 3, _map) == [
        ["a", "b", "b"],
        ["a", "a", "b"],
        ["a", "a", "a"],
    ]


def test_1():
    # fmt: off
    _map = [
        [1, 2, 1], 
        [2, 3, 2], 
        [1, 2, 1]]
    # fmt: on
    assert watersheds.solve(3, 3, _map) == [
        ["a", "a", "b"],
        ["a", "a", "b"],
        ["c", "c", "d"],
    ]


def test_2():
    # fmt: off
    _map = [
        [3]
    ]
    # fmt: on
    assert watersheds.solve(1, 1, _map) == [["a"]]


def test_random():
    random.seed(52)
    H, W = 100, 100
    _map = []
    for _ in range(H):
        row = []
        _map.append(row)
        for _ in range(W):
            row.append(random.randint(1, 100000))
    watersheds.solve(H, W, _map)