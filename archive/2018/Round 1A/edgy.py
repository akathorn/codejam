# 2018 1A - edgy
import itertools
import math
from select import select
import sys
from typing import Any, Callable, List, Sequence, TypeVar, Union, Tuple, Optional


# Used for interactive problems
WRONG_ANSWER = ...

# def solve(P: int, cookies: List[List[int]]) -> float:
#     N = len(cookies)
#     total = sum((h + w) * 2 for h, w in cookies)

#     h, w = cookies[0]
#     diagonal_cut = math.sqrt(h ** 2 + w ** 2) * 2
#     side_cut = min(h, w) * 2

#     cuts = 0
#     while cuts < N and total < P:
#         total += side_cut
#         cuts += 1

#     if total == P:
#         return total
#     elif total > P:
#         total -= side_cut
#         cuts -= 1

#     while cuts > 0 and total < P:
#         total -= side_cut
#         total += min(diagonal_cut, P - total)
#         cuts -= 1

#     return total


def solve(P: int, cookies: List[List[int]]) -> float:
    total = sum((h + w) * 2 for h, w in cookies)

    diagonal_cut = lambda c: math.sqrt(c[0] ** 2 + c[1] ** 2) * 2
    side_cut = lambda c: min(*c) * 2

    min_cut = min(side_cut(c) for c in cookies)
    n_cookies = min((P - total) // min_cut, len(cookies))

    cookies.sort(key=diagonal_cut)
    selected = cookies[-n_cookies:]

    upper_bound = total + sum(diagonal_cut(c) for c in selected)

    return min(upper_bound, P)


def solve_case(case: int):
    # Read data
    N, P = Readmany(int)
    cookies = Readlines(N, int)

    # Solve
    try:
        result = solve(P, cookies)
    except Impossible:
        result = None

    # Write solution
    Print(result, case=case, print_length=False)


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    line = sys.stdin.readline().strip()
    if line == WRONG_ANSWER:
        raise EndInteractive()
    return line


def Output(s: Any):
    sys.stdout.write(str(s) + "\n")
    sys.stdout.flush()


def Talk(s: Any):
    Output(format_output(s))
    return Input()


def Log(*args: Any, **kwargs: Any):
    if "--log" in sys.argv:
        kwargs["file"] = sys.stderr
        print(*args, **kwargs)
        sys.stderr.flush()


def format_output(
    result: Union[Any, Sequence[Any], None], print_length: bool = False
) -> str:
    """Prints the solution for one case.

    The result will be printed according to the type:
    - None:
        Case #{case}: IMPOSSIBLE
    - Single value:
        Case #{case}: {str(result)}
    - List/tuple:
        Case #{case}: {str(result[0]), str(result[1]), str(result[2]), ...}
    - List/tuple of lists/tuples:
        Case #{case}: {#rows if print_length == True}
        {str(result[0][0]), str(result[0][1]), ...}
        {str(result[1][0]), str(result[1][1]), ...}
        {str(result[2][0]), str(result[2][1]), ...}
        ...
    """
    if isinstance(result, Sequence) and not isinstance(result, str):
        if isinstance(result[0], Sequence) and not isinstance(result[0], str):
            out_string = str(len(result)) if print_length else ""
            for row in result:
                out_string += "\n" + " ".join(map(str, row))
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    return out_string


def Print(
    out: Union[Any, List[Any], None],
    case: Optional[int] = None,
    print_length: bool = False,
):
    formatted = format_output(out, print_length)
    out_string = f"Case #{case}: {formatted}" if case else formatted

    Output(out_string)


def Finalize():
    sys.stdout.close()
    sys.stderr.close()


def Read(typ: Callable[[str], T] = str) -> T:
    return typ(Input())


def Readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in Input().split()]


def Readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [Readmany(typ) for _ in range(rows)]


def main():
    try:
        tests = Read(int)
        for case in range(1, tests + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()
