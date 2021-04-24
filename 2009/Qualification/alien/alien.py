import sys
import re
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve(needle: str, dictionary: List[str]) -> int:
    r = re.compile(needle.replace("(", "[").replace(")", "]"))

    count = 0
    for word in dictionary:
        if re.match(r, word):
            count += 1

    return count


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int, words: List[str]):
    word = readstring()
    result = solve(word, words)
    writesolution(case, result)


def main():
    _, D, N = readmany(int)
    words = []
    for _ in range(D):
        words.append(readstring())
    for case in range(1, N + 1):
        solve_case(case, words)


if __name__ == "__main__":
    main()