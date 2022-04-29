# 2018 1A - choppers
import sys
import numpy as np
from typing import Any, Callable, List, Sequence, TypeVar, Union, Tuple, Optional


# Used for interactive problems
WRONG_ANSWER = ...


def solve(waffle_str: List[str], H: int, V: int) -> bool:
    waffle = np.array([[c == "@" for c in line] for line in waffle_str])

    if waffle.sum() % ((H + 1) * (V + 1)) != 0:
        return False

    chips_horizontal = waffle.sum() // (H + 1)
    cuts = []
    i, j = 0, 1
    while len(cuts) < H and j < waffle.shape[0]:
        slize = waffle[i:j, :]
        if slize.sum() > chips_horizontal:
            return False
        if slize.sum() == chips_horizontal:
            i = j
            cuts.append(slize)
        j += 1

    cuts.append(waffle[i:, :])

    chips_vertical = chips_horizontal // (V + 1)
    i, j = 0, 1
    ncuts = V
    while ncuts and j < waffle.shape[1]:
        slizes = [cut[:, i:j] for cut in cuts]
        if any(slize.sum() > chips_vertical for slize in slizes):
            return False
        if all(slize.sum() == chips_vertical for slize in slizes):
            i = j
            ncuts -= 1
        j += 1
    if ncuts:
        return False

    return True


def solve_case(case: int):
    # Read data
    R, C, H, V = Readmany(int)
    waffle = [line[0] for line in Readlines(R)]

    # Solve
    try:
        result = solve(waffle, H, V)
    except Impossible:
        result = None

    result = "POSSIBLE" if result else "IMPOSSIBLE"

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
