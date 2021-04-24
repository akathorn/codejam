import sys
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve() -> int:
    ...
    return 0


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
                out_string += "\n"
                for value in row:
                    out_string += str(value)
                    out_string += " "
                out_string.strip()
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    ...
    result = solve()
    writesolution(case, result)


def main():
    v = read2D(3, int)
    print(v)
    writesolution(1, v)
    quit()
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()