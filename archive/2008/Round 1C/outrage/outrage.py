import sys
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve(P: int, K: int, freqs: List[int]) -> int:
    freqs.sort(reverse=True)

    total_presses = 0
    key = 0
    presses = 1
    for freq in freqs:
        total_presses += freq * presses
        key += 1
        if key == K:
            key = 0
            presses += 1

    return total_presses


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(case: int, result: Union[Any, List[Any]]) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    P, K, _ = readmany(int)
    F = readmany(int)
    result = solve(P, K, F)
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()