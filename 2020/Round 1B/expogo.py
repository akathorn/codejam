import sys
from typing import Any, Callable, List, NamedTuple, Optional, TypeVar, Union


def match_end(a: int, b: int) -> bool:
    l = min(len(bin(a)), len(bin(b))) - 2
    return bin(a)[-l:] == bin(b)[-l:]


def solve(X: int, Y: int) -> Optional[str]:
    State = NamedTuple(
        "State",
        [
            ("step", int),
            ("path", str),
            ("x_current", int),
            ("y_current", int),
        ],
    )

    if X < 0:
        X *= -1
        x_pos, x_neg = "W", "E"
    else:
        x_pos, x_neg = "E", "W"

    if Y < 0:
        Y *= -1
        y_pos, y_neg = "S", "N"
    else:
        y_pos, y_neg = "N", "S"

    states = [State(0, "", 0, 0)]
    while states:
        step, path, x_current, y_current = states.pop(0)
        jump = 2 ** step
        x_pos_match = match_end(x_current + jump, X)
        x_neg_match = match_end(x_current - jump, X - 2 ** (step + 1))
        y_pos_match = match_end(y_current + jump, Y)
        y_neg_match = match_end(y_current - jump, Y - 2 ** (step + 1))
        if x_current == X and y_current == Y:
            return path
        if x_current != X:
            if x_pos_match and not (y_pos_match or y_neg_match):
                states.append(
                    State(step + 1, path + x_pos, x_current + jump, y_current)
                )
            if x_neg_match and not (y_pos_match or y_neg_match):
                states.append(
                    State(step + 1, path + x_neg, x_current - jump, y_current)
                )
        if y_current != Y:
            if y_pos_match and not (x_pos_match or x_neg_match):
                states.append(
                    State(step + 1, path + y_pos, x_current, y_current + jump)
                )
            if y_neg_match and not (x_pos_match or x_neg_match):
                states.append(
                    State(step + 1, path + y_neg, x_current, y_current - jump)
                )

    return None


def solve_case(case: int):
    # Read data
    X, Y = readmany(int)

    # Solve
    try:
        result = solve(X, Y)
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
