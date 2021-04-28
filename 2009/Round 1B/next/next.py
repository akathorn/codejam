import sys
import itertools
import math
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def to_int(digits: List[str]) -> int:
    return int("".join(digits))


def solve(N: str) -> str:
    number = [int(c) for c in reversed(N)]
    digits = set(number)
    digits = sorted(digits, reverse=True)

    numbers = solve_rec(number)
    return "".join([str(n) for n in reversed(numbers)])


def solve_rec(number: List[int]) -> List[int]:
    if number[0] == max(number):
        for i in range(1, len(number)):
            if number[i] < number[0]:
                head = number[i]
                rest = number[1:]
                rest[i] = number[0]
                return [head] + solve_rec(rest)
    else:
        for i in range(1, len(number)):
            if number[i] == min(number[1:]):
                number[i], number[0] = number[0], number[i]
                return number


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
    N = readstring()

    # Solve
    result = solve(N)

    # Write solution
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()