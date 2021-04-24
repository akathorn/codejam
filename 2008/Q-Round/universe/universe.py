import sys
from typing import List


def solve(engines: List[str], queries: List[str]) -> int:
    index = max_prefix(engines, queries)
    changes = 0
    while index < len(queries):
        index += max_prefix(engines, queries[index:])
        changes += 1

    return changes


def max_prefix(engines: List[str], queries: List[str]) -> int:
    m = 0
    for engine in engines:
        index = queries.index(engine) if engine in queries else len(queries)
        m = max(index, m)
    return m


def main():
    N = int(sys.stdin.readline())
    for case in range(1, N + 1):
        # Engines
        S = int(sys.stdin.readline())
        engines: List[str] = []
        for _ in range(S):
            engines.append(sys.stdin.readline().strip())

        # Queries
        Q = int(sys.stdin.readline())
        queries: List[str] = []
        for _ in range(Q):
            queries.append(sys.stdin.readline().strip())

        print(f"Case #{case}: {solve(engines, queries)}")
    sys.stdout.close()


if __name__ == "__main__":
    main()