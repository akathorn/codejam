import sys
import itertools
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve(cells: int, release: List[int]) -> int:
    release = [prisoner - 1 for prisoner in release]

    coins_left = 0
    rel = release.copy()
    last_cell = cells - 1
    while rel:
        # Left
        prisoner = rel.pop()
        coins_left += last_cell
        last_cell = prisoner - 1

    coins_right = 0
    rel = release.copy()
    last_cell = 0
    while rel:
        # Right
        prisoner = rel.pop(0)
        coins_right += cells - last_cell - 1
        last_cell = prisoner + 1

    return min(coins_left, coins_right)


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def read2D(rows: int, typ: Callable[[str], T]) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def solve_case(case: int):
    # Read data
    P, _ = readmany(int)
    release = readmany(int)

    # Solve
    result = solve(P, release)

    # Write solution
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()