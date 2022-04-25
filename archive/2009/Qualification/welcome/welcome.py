import sys
import functools
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve(line: str) -> int:
    return ways("welcome to code jam", line)


@functools.lru_cache(maxsize=None)
def ways(sub: str, line: str) -> int:
    if not sub:
        return 1
    c = sub[0]
    nways = 0
    for i in range(len(line)):
        if line[i] == c:
            nways += ways(sub[1:], line[i + 1 :])
    return nways


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(
    case: int,
    result: Union[Any, List[Any], None],
) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    out_string = out_string.zfill(4)[-4:]

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    line = readstring()
    result = solve(line)
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()