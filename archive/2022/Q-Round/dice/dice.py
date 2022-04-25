import sys
from typing import Any, Callable, List, TypeVar, Union


def solve(dice: List[int]) -> int:
    straight = 0
    remaining = list(sorted(dice, reverse=True))
    while remaining:
        if remaining.pop() > straight:
            straight += 1
    return straight


def solve_case(case: int):
    # Read data
    read(str)

    # Solve
    result = solve(readmany(int))

    # Write solution
    writesolution(case, result)


############################ Template code ###############################

T = TypeVar("T")


def read(typ: Callable[[str], T] = str) -> T:
    return typ(sys.stdin.readline().strip())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
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


def main():
    T = read(int)
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()