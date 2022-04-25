import sys
import math
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")

NANO = int(1e9)
tick = 1 / 12 * 1e-10


def solve(A: int, B: int, C: int) -> List[int]:
    # H = (A / NANO / 60 / 60) % 12
    # M = (B / NANO / 60 / 12) % 60
    # S = (C / NANO) % 60
    H = (A * tick) / 360 * 12
    M = (B * tick) / 360 * 60
    S = (C * tick) / 360 * 60

    return list(map(math.floor, [H, M, S, 0]))


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
    A, B, C = readmany(int)

    # Solve
    result = solve(A, B, C)

    # Write solution
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()