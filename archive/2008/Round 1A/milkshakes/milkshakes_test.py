from milkshakes import solve
import random


def test_sample1():
    assert (
        solve(
            5,
            [
                [(1, True)],
                [(1, False), (2, False)],
                [(5, False)],
            ],
            set([(1, False), (2, False), (5, False)]),
            set([(1, True)]),
        )
        == [1, 0, 0, 0, 0]
    )


def test_sample2():
    assert (
        solve(
            1,
            [
                [(1, False)],
                [(1, True)],
            ],
            set([(1, False)]),
            set([(1, True)]),
        )
        == None
    )


def test_performance1():
    costumers = []
    malted = set()
    unmalted = set()
    N = 2000
    for _ in range(N):
        costumer = []
        costumers.append(costumer)
        for flavor in random.sample(range(1, N + 1), random.randint(1, N)):
            costumer.append((flavor, False))
            unmalted.add((flavor, False))
        malted_flavor = (random.randint(1, N), True)
        costumer.append(malted_flavor)
        malted.add(malted_flavor)

    for _ in range(5):
        solve(
            N,
            costumers,
            unmalted,
            malted,
        )


# def test_performance_impossible():
#     costumers = []
#     malted = set()
#     unmalted = set()
#     N = 100
#     for c in range(N):
#         costumer = []
#         costumers.append(costumer)
#         for flavor in random.sample(range(1, N + 1), random.randint(1, N)):
#             costumer.append((flavor, False))
#             unmalted.add((flavor, False))

#     for _ in range(5):
#         assert (
#             solve(
#                 N,
#                 costumers,
#                 unmalted,
#                 malted,
#             )
#             == None
#         )


def test_four():
    assert (
        solve(
            3,
            [
                [(2, True)],
                [(3, True)],
            ],
            set(),
            set([(2, True), (3, True)]),
        )
        == [0, 1, 1]
    )
