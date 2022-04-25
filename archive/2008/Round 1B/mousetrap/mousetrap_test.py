import mousetrap


def test_sample():
    assert mousetrap.solve(5, [1, 2, 3, 4, 5]) == [1, 3, 2, 5, 4]
    assert mousetrap.solve(15, [3, 4, 7, 10]) == [2, 8, 13, 4]


def test_build_deck():
    assert mousetrap.build_deck(5) == [1, 3, 2, 5, 4]
