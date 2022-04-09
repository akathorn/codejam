import functools
import sys
from typing import Any, Callable, List, Optional, TypeVar, Union


def solve(patterns: List[str]) -> Optional[str]:
    left_patterns = [p.split("*")[0][::-1] for p in patterns]
    right_patterns = [p.split("*")[1] for p in patterns]

    left = solve_right(left_patterns)[::-1]
    right = solve_right(right_patterns)

    i = 1
    common = 0
    # suffix = left[-i:]
    # prefix = right[:i]
    # while i <= min(len(left), len(right)):
    #     if prefix == suffix:
    #         common = i
    #     i += 1
    #     suffix = left[-i:]
    #     prefix = right[:i]

    result = left + right[common:]

    if len(result) > 1e4:
        return None
    else:
        return result


def solve_right(patterns: List[str]) -> str:
    patterns.sort(key=lambda p: len(p), reverse=True)
    name = patterns[0]
    for p in patterns:
        if p and name[len(name) - len(p) :] != p:
            raise Impossible()
    return name


# def join_patterns(p1: str, p2: str) -> str:
#     if not p1:
#         return p2
#     elif not p2:
#         return p1
#     elif p1[0] == p2[0]:
#         if p1[0] != "*":
#             return p1[0] + join_patterns(p1[1:], p2[1:])
#         else:


#     elif p1[0] == "*":
#         return p2[0] + join_patterns(p1, p2[1:])
#     elif p2[0] == "*":
#         return p1[0] + join_patterns(p1, p2[1:])
#     else:
#         raise Impossible()


# def solve(patterns: List[str]) -> Optional[str]:
#     return functools.reduce(join_patterns, patterns).replace("*", "")


def solve_case(case: int):
    # Read data
    patterns = [l[0] for l in readlines(read(int))]

    # Solve
    try:
        result = solve(patterns)
    except Impossible:
        result = "*"

    # Write solution
    Output(writesolution(case, result))


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    return sys.stdin.readline().strip()


def Output(s: str):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def Finalize():
    sys.stdout.close()
    sys.stderr.close()


def read(typ: Callable[[str], T] = str) -> T:
    return typ(Input())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in Input().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(
    case: int, result: Union[Any, List[Any], None], print_length=False
) -> str:
    """Prints the solution for one case.

    The result will be printed according to the type:
    - None:
        Case #{case}: IMPOSSIBLE
    - Single value:
        Case #{case}: {str(result)}
    - List:
        Case #{case}: {str(result[0]), str(result[1]), str(result[2]), ...}
    - List of lists:
        Case #{case}: {#rows if print_length == True}
        {str(result[0][0]), str(result[0][1]), ...}
        {str(result[1][0]), str(result[1][1]), ...}
        {str(result[2][0]), str(result[2][1]), ...}
        ...
    """
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = str(len(result)) if print_length else ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    return f"Case #{case}: {out_string}"


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()