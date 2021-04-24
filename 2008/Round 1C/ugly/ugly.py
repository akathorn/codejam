import sys
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union
from collections import deque

T = TypeVar("T")


def evaluate(s: str):
    result = 0
    number = 0
    op = "+"
    for c in s:
        if c == "+" or c == "-":
            if op == "+":
                result += number
            else:
                result -= number
            number = 0
            op = c
        else:
            number = number * 10 + int(c)
    if op == "+":
        result += number
    else:
        result -= number
    return result


def solve(N: str) -> int:
    # Build expressions
    states = deque()

    states.append((N[:-1], N[-1]))
    ugly = 0
    while states:
        remaining, exp = states.pop()
        if len(remaining) == 0:
            number = evaluate(exp)
            for p in [2, 3, 5, 7]:
                if number % p == 0:
                    ugly += 1
                    break
        else:
            states.append((remaining[:-1], remaining[-1] + exp))
            states.append((remaining[:-1], remaining[-1] + "+" + exp))
            states.append((remaining[:-1], remaining[-1] + "-" + exp))

    return ugly


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
    N = readstring()
    result = solve(N)
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()