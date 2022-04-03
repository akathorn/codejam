import sys
import itertools
from typing import Any, Callable, List, TypeVar, Union


def solve(K: int, tickets: List[int]) -> float:
    best = 0.0
    for a, b in itertools.combinations(range(1, K + 1), 2):
        prob = sum(win(a, b, c, tickets) for c in range(1, K + 1)) / K
        best = max(best, prob)

    return best


def win(a: int, b: int, c: int, tickets: List[int]) -> bool:
    distances = [abs(c - t) for t in tickets]
    da = abs(c - a)
    db = abs(c - b)
    return all(da < d for d in distances) or all(db < d for d in distances)


def solve_case(case: int):
    # Read data
    _, K = readmany(int)
    tickets = readmany(int)

    # Solve
    result = solve(K, tickets)

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