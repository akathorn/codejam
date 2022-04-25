import sys
import itertools
import math
from typing import List, Tuple


def solve(n, A, B, C, D, x0, y0, M) -> int:
    trees = generate_trees(n, A, B, C, D, x0, y0, M)
    return solve_math(trees)


def solve_math(trees: List[Tuple[int, int]]) -> int:
    trees_by_module = {}
    for modules in itertools.product(range(3), range(3)):
        trees_by_module[modules] = 0

    for tree in trees:
        xmod = tree[0] % 3
        ymod = tree[1] % 3
        trees_by_module[(xmod, ymod)] += 1

    result = 0
    for x, y, z in itertools.combinations(trees_by_module.keys(), 3):
        if (x[0] + y[0] + z[0]) % 3 == 0 and (x[1] + y[1] + z[1]) % 3 == 0:
            result += trees_by_module[x] * trees_by_module[y] * trees_by_module[z]

    for m in itertools.product(range(3), range(3)):
        n = trees_by_module[m]
        if n > 2:
            result += math.factorial(n) / (6 * math.factorial(n - 3))

    return int(result)


def solve_bruteforce(trees: List[Tuple[int, int]]) -> int:
    solutions = 0

    for x, y, z in itertools.combinations(trees, 3):
        center_x, center_y = triangle_center(x, y, z)
        if center_x.is_integer() and center_y.is_integer():
            solutions += 1

    return solutions


def triangle_center(x, y, z):
    return ((x[0] + y[0] + z[0]) / 3, (x[1] + y[1] + z[1]) / 3)


def generate_trees(n, A, B, C, D, x0, y0, M):
    X, Y = x0, y0
    trees = [(X, Y)]
    for _ in range(n - 1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X, Y))
    return trees


def main():
    N = int(sys.stdin.readline())
    for case in range(1, N + 1):
        n, A, B, C, D, x0, y0, M = [int(x) for x in sys.stdin.readline().split()]

        print(f"Case #{case}: {solve(n, A, B, C, D, x0, y0, M)}")
    sys.stdout.close()


if __name__ == "__main__":
    main()