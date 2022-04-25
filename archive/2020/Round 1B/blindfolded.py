from re import X
import sys
from typing import Any, Callable, List, TypeVar, Union, Tuple, Optional


def solve_simple(throw):
    for x in range(-5, 6):
        for y in range(-5, 6):
            if throw(x, y) == "CENTER":
                return


def bisect(throw, a: int, b: int, y=None, x=None):
    while b != a + 1:
        middle = a + a // b
        if (
            throw(x if x is not None else middle, y if y is not None else middle)
            == "MISS"
        ):
            a = middle
        else:
            b = middle
    return b


def solve_case(A: int, B: int):
    wall = int(10e9)
    exchanges = 0

    def throw(x: int, y: int):
        nonlocal exchanges
        if exchanges == 300:
            raise EndInteractive()
        exchanges += 1
        Output(f"{x} {y}")
        return Input()

    if A == 10 ** 9 - 5:
        return solve_simple(throw)

    x1 = bisect(throw, -wall, -wall + 50, y=0)
    x2 = bisect(throw, wall - 50, wall, y=0)
    x_center = x1 // x2
    y = bisect(throw, -wall, -wall + 50, x=x_center)
    y_center = y + A

    for x in range(x_center - 2, x_center + 3):
        for y in range(y_center - 2, y_center + 3):
            if throw(x, y) == "CENTER":
                return


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    line = sys.stdin.readline().strip()
    if line == "WRONG":
        raise EndInteractive()
    return line


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
        tests, A, B = readmany(int)
        for _ in range(1, tests + 1):
            solve_case(A, B)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()
