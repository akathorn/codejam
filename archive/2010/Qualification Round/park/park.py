import sys
from collections import deque
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve(rides: int, capacity: int, groups: List[int]) -> int:
    queue = deque(groups)

    moneys = 0
    riders: List[int] = []
    for _ in range(rides):
        nriders = 0
        riders.clear()
        while len(queue) > 0 and (nriders + queue[0] <= capacity):
            group = queue.popleft()
            riders.append(group)
            nriders += group
        moneys += sum(riders)
        queue.extend(riders)

    return moneys


def solve_case(case: int):
    # Read data
    R, k, _ = readmany(int)
    groups = readmany(int)

    # Solve
    result = solve(R, k, groups)

    # Write solution
    writesolution(case, result)


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