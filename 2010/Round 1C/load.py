import sys
import math
from typing import Any, Callable, List, TypeVar, Union


def solve(supports: int, overloads: int, C: int) -> int:
    if supports * C >= overloads:
        return 0

    # We test overload / C / C
    operations = 1
    next = overloads / C / C

    # Case 1: next SUPPORTS
    # a) next*C supports -> (next*C)*C = overload -> found!
    # b) next*C overloads -> (next*C) supports and (next*C)*C doesn't -> found!
    # This is the best case, so we ignore it

    # Case 2: next OVERLOADS
    if supports * C >= next:
        return operations

    # Worst case: we call recursively
    return operations + solve(supports, math.floor(next), C)


def solve_case(case: int):
    # Read data
    L, P, C = readmany(int)

    # Solve
    result = solve(L, P, C)

    # Write solution
    writesolution(case, result)


############################ Template code ###############################

T = TypeVar("T")


def Input() -> str:
    return sys.stdin.readline().strip()


def Output(s: str):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def Finalize():
    sys.stdout.flush()
    sys.stderr.flush()
    sys.stdout.close()
    sys.stderr.close()


def read(typ: Callable[[str], T] = str) -> T:
    return typ(Input())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in Input().split()]


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

    Output(f"Case #{case}: {out_string}")


class EndInteractive(Exception):
    pass


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        Finalize()

    Finalize()


if __name__ == "__main__":
    main()