# 2022 1A
import sys
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Sequence,
    TypeVar,
    Union,
    Tuple,
    Optional,
)


A1 = [2 ** i for i in range(30)]
A2 = [2 ** i + 1 for i in range(1, 30)]
i = 5
while len(A2) < 70:
    if i not in A2 and i not in A1:
        A2.append(i)
    i += 2

A2.sort()
A = A1 + A2


def solve_case(_):
    N = read(int)
    Print(A)
    B = readmany(int)
    target = sum(A + B) // 2

    B.sort()
    total = 0
    C = []
    fillings = list(A2)
    while (target - total) > (2 ** 29 - 1):
        take_from = B or fillings
        if not fillings:
            a = 3
        if take_from[0] + total <= target:
            total += take_from[0]
            C.append(take_from.pop(0))
        else:
            total -= C[-1]
            C.pop()
    remaining = target - total
    bits = bin(remaining)[2:]
    for i, b in enumerate(reversed(bits)):
        if b == "1":
            C.append(2 ** i)

    Print(C)

    return


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    line = sys.stdin.readline().strip()
    if line == "-1":
        Log("-1 received, stopping")
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
