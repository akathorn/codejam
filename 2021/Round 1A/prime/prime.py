import sys
import itertools
from operator import mul
from functools import reduce
from typing import Callable, List, TypeVar


T = TypeVar("T")


def prod(numbers):
    return reduce(mul, numbers)


def solve(cards) -> int:
    return solve_cleverer(cards)


def solve_bruteforce(cards) -> int:
    deck = []
    for card in cards:
        deck.extend([card[0]] * card[1])

    best = 0
    for size_sum in range(1, len(deck)):
        for sum_indexes in itertools.combinations(range(len(deck)), size_sum):
            prod_indexes = [i for i in range(len(deck)) if i not in sum_indexes]
            s = sum(deck[i] for i in sum_indexes)
            p = prod(deck[i] for i in prod_indexes)

            if s == p and s > best:
                best = s

    return best


def solve_cleverer(cards) -> int:
    # Prepare numbers
    primes = []
    quantity = []
    for card in cards:
        primes.append(card[0])
        quantity.append(card[1])

    # Create first pair of hands
    hands = []
    for i in range(len(quantity)):
        left = list(quantity)
        left[i] -= 1
        right = [0] * len(quantity)
        right[i] = 1
        hands.append((left, right))

    best = 0
    iterations = 0
    # Check all hands
    while hands:
        iterations += 1
        left, right = hands.pop()
        if not any(left) or not any(right):
            continue

        # Sum and mult
        s, p = 0, 1
        for i in range(len(quantity)):
            s += primes[i] * left[i]
            p *= primes[i] ** right[i]

        # In case this is the first iteration and we have a solution
        if s == p:
            best = max(best, s)

        for i in range(len(quantity)):
            if not left[i]:
                continue
            new_s = s - primes[i]
            new_p = p * primes[i]

            # Base cases
            if new_s < best:
                continue
            elif new_p == new_s:
                best = max(best, new_s)
            elif new_p > new_s:
                continue
            # General case
            else:
                new_left = list(left)
                new_right = list(right)
                new_left[i] -= 1
                new_right[i] += 1
                hands.append((new_left, new_right))

    return best


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def main():
    T = readint()
    for case in range(1, T + 1):
        # Process data
        M = readint()
        cards = []
        for _ in range(M):
            Pi, Ni = readmany(int)
            cards.append((Pi, Ni))
        # Solve and print
        result: str = str(solve(cards))
        print(f"Case #%d: %s" % (case, result))


if __name__ == "__main__":
    main()