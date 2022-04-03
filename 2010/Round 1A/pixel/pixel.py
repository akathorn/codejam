import sys
import math
from typing import Any, Callable, List, Tuple, TypeVar, Union


def solve(D: int, I: int, M: int, pixels: List[int]) -> int:
    states = [[]]
    best = math.inf
    while states:
        operations: List[Tuple[str, int, int]] = states.pop()
        pix = pixels.copy()
        cost = 0
        for operation in operations:
            if operation[0] == "d":
                cost += D
                pix.pop(operation[1])
            elif operation[0] == "i":
                cost += I
                pix.insert(operation[1], operation[2])
            elif operation[0] == "m":
                cost += abs(pix[operation[1]] - operation[2])
                pix[operation[1]] = operation[2]

        if is_smooth(M, pix):
            best = min(cost, best)
            continue

        for i in range(len(pix)):
            states.append(operations + [("d", i)])

        for i in range(len(pix) + 1):
            for j in range(256):
                states.append(operations + [("i", i, j)])

        for i in range(len(pix)):
            for j in range(256):
                states.append(operations + [("m", i, j)])

    return best


def is_smooth(M: int, pixels: List[int]) -> bool:
    for i in range(1, M):
        if abs(pixels[i] - pixels[-1]) > M:
            return False
    return True


def solve_case(case: int):
    # Read data
    D, I, M, N = readmany(int)
    pixels = readmany(int)

    # Solve
    result = solve(D, I, M, pixels)

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