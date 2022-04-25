from collections import defaultdict
import sys
from typing import Any, Callable, List, Optional, TypeVar, Union
import itertools


class Impossible(Exception):
    pass


def mark(i: int, current: str, intersections: List[List[int]], result: List[str]):
    if result[i] == "":
        result[i] = current
    elif result[i] == current:
        return
    else:
        raise Impossible

    new = "C" if current == "J" else "J"
    for j in intersections[i]:
        mark(j, new, intersections, result)


def solve(schedule) -> Optional[str]:
    intersections = [[] for _ in range(len(schedule))]
    for (i, (a, c)), (j, (b, d)) in itertools.combinations(enumerate(schedule), 2):
        if (a < b) and (c > b) or (b < a) and (d > a):
            intersections[i].append(j)
            intersections[j].append(i)

    result = [""] * len(schedule)
    for i in range(len(schedule)):
        if result[i] != "":
            continue
        else:
            mark(i, "C", intersections, result)

    return "".join(result)


def solve_case(case: int):
    # Read data
    N = read(int)
    schedule = readlines(N, int)

    # Solve
    try:
        result = solve(schedule)
    except Impossible:
        result = None

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
    sys.stdout.close()
    sys.stderr.close()


def read(typ: Callable[[str], T] = str) -> T:
    return typ(Input())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in Input().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(
    case: int, result: Union[Any, List[Any], None], print_length=False
) -> None:
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = str(len(result)) if print_length else ""
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
        pass
    Finalize()


if __name__ == "__main__":
    main()