import universe


def test_one():
    engines = [
        "Yeehaw",
        "NSM",
        "Dont Ask",
        "B9",
        "Googol",
    ]

    queries = [
        "Yeehaw",
        "Yeehaw",
        "Googol",
        "B9",
        "Googol",
        "NSM",
        "B9",
        "NSM",
        "Dont Ask",
        "Googol",
    ]

    assert universe.solve(engines, queries) == 1


def test_two():
    engines = [
        "Yeehaw",
        "NSM",
        "Dont Ask",
        "B9",
        "Googol",
    ]

    queries = [
        "Googol",
        "Dont Ask",
        "NSM",
        "NSM",
        "Yeehaw",
        "Yeehaw",
        "Googol",
    ]

    assert universe.solve(engines, queries) == 0


def test_three():
    engines = [
        "A",
        "B",
        "C",
    ]

    queries = [
        "A",
        "B",
        "C",
    ]

    assert universe.solve(engines, queries) == 1
    assert universe.solve2(engines, queries) == 1


def test_four():
    engines = [
        "A",
        "B",
        "C",
        "D",
    ]

    queries = [
        "A",
        "B",
        "C",
        "D",
        "A",
        "B",
        "C",
        "D",
    ]

    assert universe.solve2(engines, queries) == 2
    assert universe.solve(engines, queries) == 2


def test_five():
    engines = [
        "A",
        "B",
        "C",
    ]

    queries = [
        "B",
        "B",
        "B",
    ]

    assert universe.solve(engines, queries) == 0


def test_six():
    engines = [
        "A",
        "B",
        "C",
    ]

    queries = [
        "A",
        "B",
        "A",
        "C",
    ]

    assert universe.solve2(engines, queries) == 1
    assert universe.solve(engines, queries) == 1


def test_seven():
    engines = [
        "A",
        "B",
        "C",
    ]

    queries = [
        "A",
        "A",
        "C",
        "A",
        "B",
    ]

    assert universe.solve2(engines, queries) == 1
    # assert universe.solve(engines, queries) == 1


def test_eight():
    engines = [
        "A",
        "B",
    ]

    queries = [
        "A",
        "B",
        "A",
        "B",
    ] * 2

    assert universe.solve2(engines, queries) == 6


def test_nine():
    engines = [
        "A",
        "B",
        "C",
        "D",
        "E",
    ]

    queries = [
        "A",
        "B",
        "C",
        "D",
        "E",
    ] * 100

    # assert universe.solve(engines, queries) == 1
    assert universe.solve2(engines, queries) == 100
