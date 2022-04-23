import sys
from typing import Any, Callable, List, TypeVar, Union, Tuple, Optional


# def solve(X: int, Y: int, M: str) -> Optional[int]:
#     if len(set(M)) > 2:
#         return None

#     if Y < 0:
#         Y *= -1
#         d = -1
#     else:
#         d = 1
#     route = [d if m == "N" else -d for m in reversed(M)]

#     steps = 0
#     X = abs(X)
#     x = 0
#     while x != X:
#         if not route:
#             return None
#         Y += route.pop()
#         x += 1
#         steps += 1

#     y = 0
#     while y != Y:
#         if not route:
#             return None
#         steps += 1
#         Y += route.pop()
#         if y < Y:
#             y += 1

#     return steps


def solve(X: int, Y: int, M: str) -> Optional[int]:
    pos = [X, Y]
    minute = 0
    for step in M:
        minute += 1
        if step == "N":
            pos[1] += 1
        if step == "S":
            pos[1] -= 1
        if step == "E":
            pos[0] += 1
        if step == "W":
            pos[0] -= 1
        d = abs(pos[0]) + abs(pos[1])
        if d <= minute:
            return minute
    return None


def solve_case(case: int):
    # Read data
    X, Y, M = readmany(str)
    X = int(X)
    Y = int(Y)

    # Solve
    try:
        result = solve(X, Y, M)
    except Impossible:
        result = None

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


def Output(s: Any):
    sys.stdout.write(str(s) + "\n")
    sys.stdout.flush()


def Log(*args: Any, **kwargs: Any):
    if "--log" in sys.argv:
        kwargs["file"] = sys.stderr
        print(*args, **kwargs)


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
    case: int, result: Union[Any, List[Any], None], print_length: bool = False
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
    if isinstance(result, list) or isinstance(result, tuple):
        if isinstance(result[0], list) or isinstance(result[0], tuple):
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
        tests = read(int)
        for case in range(1, tests + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()
