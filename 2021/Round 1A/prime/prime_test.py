import random
from prime import solve_bruteforce, solve_cleverer

# fmt: off
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
# fmt: on


def test_sample_bruteforce():
    assert solve_bruteforce([(2, 7)]) == 8
    assert solve_bruteforce([(2, 2), (3, 1)]) == 0
    assert solve_bruteforce([(17, 2)]) == 17
    assert solve_bruteforce([(2, 2), (3, 1), (5, 2), (7, 1), (11, 1)]) == 25


def test_sample_cleverer():
    assert solve_cleverer([(2, 7)]) == 8
    assert solve_cleverer([(2, 2), (3, 1)]) == 0
    assert solve_cleverer([(17, 2)]) == 17
    assert solve_cleverer([(2, 2), (3, 1), (5, 2), (7, 1), (11, 1)]) == 25


def test_big():
    ncards = 1e5
    cards = []
    for p in reversed(primes):
        cards.append((p, random.randint(0, int(ncards / 95))))

    solve_cleverer(cards)