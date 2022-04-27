# 2018 Q-Round - saving
import math
import sys
from typing import Any, Callable, List, Sequence, TypeVar, Union, Tuple, Optional


# Used for interactive problems
WRONG_ANSWER = ...


# def damage(P: List[str]) -> int:
#     d = 1
#     total = 0
#     for a in P:
#         if a == "S":
#             total += d
#         else:
#             d *= 2
#     return total


# def solve(D: int, P: List[str]) -> Optional[int]:
#     # We can survive P
#     if damage(P) <= D:
#         return 0
#     # We can't hack anything
#     elif "C" not in P:
#         return None
#     # All C's are at the end
#     elif "S" not in P[P.index("C") :]:
#         return None
#     else:
#         i = P.index("C")
#         while P[i + 1] != "S":
#             i += 1
#         P[i], P[i + 1] = "S", "C"
#         res = solve(D, P)
#         return res + 1 if res is not None else None


def solve(D: int, P: List[str]) -> Optional[int]:
    damages = [0]
    for c in P:
        if c == "S":
            damages[-1] += 1
        else:
            damages.append(0)

    damage = lambda ds: sum(d * 2 ** i for i, d in enumerate(ds))
    hacks = 0
    while any(damages[1:]) and damage(damages) > D:
        best = math.inf
        best_list = []
        for i in range(1, len(damages)):
            if damages[i]:
                ds = list(damages)
                ds[i - 1] += 1
                ds[i] -= 1
                if damage(ds) < best:
                    best_list = ds
        damages = best_list
        hacks += 1

    return hacks if damage(damages) <= D else None


def solve_case(case: int):
    # Read data
    D, P = Readmany()
    D = int(D)
    P = list(P)

    # Solve
    try:
        result = solve(D, P)
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
    Output(s)
    return Input()


def Log(*args: Any, **kwargs: Any):
    if "--log" in sys.argv:
        kwargs["file"] = sys.stderr
        print(*args, **kwargs)


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
