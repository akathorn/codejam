import sys
from itertools import combinations, combinations_with_replacement
from typing import List


def product(v1: List[int], v2: List[int]) -> int:
    return sum(x * y for x, y in zip(v1, v2))


# def best_permute(v1: List[int], v2: List[int]) -> None:
#     best_value = product(v1, v2)
#     best_permutation = 0, 0
#     for x, y in combinations(range(len(v1)), 2):
#         v1[x], v1[y] = v1[y], v1[x]
#         p = product(v1, v2)
#         if p < best_value:
#             best_value = p
#             best_permutation = x, y
#         v1[x], v1[y] = v1[y], v1[x]

#     x, y = best_permutation
#     v1[x], v1[y] = v1[y], v1[x]


# def solve(v1: List[int], v2: List[int]) -> int:
#     best_permute(v1, v2)
#     best_permute(v1, v2)
#     return product(v1, v2)


def swap(v: List[int], x: int, y: int) -> None:
    v[x], v[y] = v[y], v[x]


def solve(v1: List[int], v2: List[int]) -> int:
    n = range(len(v1))
    best_value = product(v1, v2)
    for x, y in combinations_with_replacement(n, 2):
        swap(v1, x, y)
        best_value = min(product(v1, v2), best_value)
        for i, j in combinations_with_replacement(n, 2):
            swap(v1, i, j)
            best_value = min(product(v1, v2), best_value)
            swap(v1, i, j)
        swap(v1, x, y)

    return best_value


def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        _ = sys.stdin.readline()
        v1: List[int] = [int(x) for x in sys.stdin.readline().split()]
        v2: List[int] = [int(x) for x in sys.stdin.readline().split()]

        print(f"Case #{case}: {solve(v1, v2)}")
    sys.stdout.close()


if __name__ == "__main__":
    main()