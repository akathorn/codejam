import sys
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union


T = TypeVar("T")


def solve(N: str) -> int:
    # Build expressions
    states: List[Tuple[str, str]] = [(N[:-1], N[-1])]
    # result = []
    ugly = 0
    while states:
        remaining, exp = states.pop()
        if len(remaining) == 0:
            while exp[0] == "0":
                exp = exp[1:]

            # result.append(eval(exp))

            number = eval(exp)
            for p in [2, 3, 5, 7]:
                if number % p == 0:
                    ugly += 1
                    break
        else:
            states.append((remaining[:-1], remaining[-1] + "+" + exp))
            states.append((remaining[:-1], remaining[-1] + "-" + exp))
            states.append((remaining[:-1], remaining[-1] + exp))

    return ugly


# Exp = NamedTuple(
#     "Expression",
#     [
#         ("left", Union["Exp", str]),
#         ("right", str),
#         ("op", str),
#     ],
# )


# def pprint(exp: Exp):
#     if isinstance(exp.right, str):
#         return f"{exp.left}{exp.op}{exp.right}"
#     else:
#         return f"{exp.left}{exp.op}{pprint(exp.right)}"

# def solve(N: str) -> int:
#     # Build expressions
#     expressions: List[Tuple[str, Exp]] = [(N, Exp("0", "+", ""))]
#     result = []
#     while expressions:
#         remaining, exp = expressions.pop()
#         if remaining == "":
#             result.append(evaluate(exp))
#         else:
#             n, rest = remaining[0], remaining[1:]

#             expressions.append((rest, Exp(exp, "+", n)))
#             expressions.append((rest, Exp(exp, "-", n)))
#             expressions.append((rest, Exp(exp, "-", n)))

#     return 0


# def evaluate(exp: Exp) -> int:
#     left, op, right = exp

#     right = 0 if right == "" else int(right)
#     left = int(left) if isinstance(left, str) else evaluate(left)

#     if op == "+":
#         return left + right
#     else:
#         return left - right


# def rec_solutions(N: str) -> List[str]:
#     if len(N) == 1:
#         return [N]

#     head, tail = N[0], N[1:]
#     rec = rec_solutions(tail)
#     solutions = []
#     for solution in rec:
#         solutions.append(f"({head}) + ({solution})")
#         solutions.append(f"({head}) - ({solution})")
#         solutions.append(head + solution)
#     return solutions


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