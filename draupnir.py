import math
import sys
from typing import Any, Callable, List, TypeVar, Union


def solve_case(W: int):
    if W == 2:
        raise EndInteractive()
    R = [0, 0, 0, 0, 0, 0, 0]
    total = lambda day: sum(r * 2 ** math.floor(day / i) for i, r in enumerate(R, 1))

    for i in range(6, 0, -1):
        day = max(63 * (i - 1), 1)
        Output(day)
        t = read(int) - total(day)
        R[i] = int(t / (2 ** math.floor(day / i)))

    Output(" ".join([str(r) for r in R[1:]]))

    if read(int) == -1:
        raise EndInteractive


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    l = sys.stdin.readline().strip()
    if l == "-1":
        raise EndInteractive
    return l


def Output(s: Any):
    sys.stdout.write(str(s) + "\n")
    sys.stdout.flush()


def Finalize():
    sys.stdout.close()
    sys.stderr.close()


def Log(*args, **kwargs):
    if "--log" in sys.argv:
        kwargs["file"] = sys.stderr
        print(*args, **kwargs)


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
        T, W = readmany(int)
        for _ in range(1, T + 1):
            solve_case(W)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()