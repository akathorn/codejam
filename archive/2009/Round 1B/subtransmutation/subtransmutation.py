import sys
import math
from typing import Any, Callable, List, Optional, TypeVar, Union


T = TypeVar("T")


def solve(A: int, B: int, U: List[int]) -> Optional[int]:
    best = math.inf
    states = [{i + 1: U[i] for i in range(len(U))}]
    while states:
        state = states.pop()
        for x in state.keys():
            if state[x] < 1:
                continue
            new_state = state.copy()
            new_metal = x + A
            if new_metal >= best:
                continue
            new_state[x] -= 1

            y = new_metal - B
            if y > 0:
                new_state[y] = new_state.get(y, 0) - 1

            # We reach a solution
            if all(new_state[x] <= 0 for x in range(1, len(U) + 1)):
                best = min(new_metal, best)
            # We add this to the search
            else:
                new_state[new_metal] = new_state.get(new_metal, 0) + 1
                states.append(new_state)

    return int(best) if best != math.inf else None


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
    _, A, B = readmany(int)
    U = readmany(int)

    # Solve
    result = solve(A, B, U)

    # Write solution
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()