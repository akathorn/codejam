import sys
import itertools
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    Union,
)


T = TypeVar("T")


# O(sqrt(n))
def factorization(n: int, P: int) -> List[int]:
    primfac = []
    d = 2  # TODO: d = P ?
    while d * d <= n:
        while (n % d) == 0:
            if d >= P:
                primfac.append(d)
            n //= d
        d += 1
    if n > 1 and n >= P:
        primfac.append(n)
    return primfac


def solve(A: int, B: int, P: int) -> int:
    # n = B - A

    n_sets = 0

    factors = []
    # O(n * sqrt(n))
    for number in range(A, B + 1):
        # O(sqrt(n))
        fact = factorization(number, P)
        if fact:
            factors.append(fact)
        else:
            n_sets += 1

    # O(len(factors))
    sets: Dict[int, Tuple[int, Set[int]]] = {
        i: (i, set([i])) for i in range(len(factors))
    }

    for a, b in itertools.combinations(range(len(factors)), 2):
        for factor in factors[a]:
            if factor in factors[b]:
                # Merge the two sets, a into b
                sets[b][1].update(sets[a][1])
                for number in sets[a][1]:
                    sets[number] = sets[b]
                    # sets[b][1].add(number)
                break

    n_sets += len(set(s[0] for s in sets.values()))
    return n_sets


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(case: int, result: Union[Any, List[Any]]) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def main():
    T = readint()
    for case in range(1, T + 1):
        A, B, P = readmany(int)
        result = solve(A, B, P)
        writesolution(case, result)


if __name__ == "__main__":
    main()