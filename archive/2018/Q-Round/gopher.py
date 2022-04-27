# 2018 Q-Round - gopher
from collections import defaultdict
import math
import sys
from typing import (
    Any,
    Callable,
    Counter,
    Dict,
    List,
    Sequence,
    Set,
    TypeVar,
    Union,
    Tuple,
    Optional,
)


# Used for interactive problems
WRONG_ANSWER = "-1 -1"


def hood(i: int, j: int) -> Set[Tuple[int, int]]:
    return {(i + a, j + b) for a in (0, -1, 1) for b in (0, -1, 1)}


def solve_case(case: int):
    A = Read(int)

    cells: Dict[Tuple[int, int], Set[Tuple[int, int]]] = {}
    side_x = math.floor(math.sqrt(A))
    while A / side_x % 1 != 0:
        side_x -= 1
    side_x = int(side_x)
    side_y = A // side_x

    for i in range(2, side_x):
        for j in range(2, side_y):
            cells[i, j] = hood(i, j)

    all_cells = set()
    for cell in cells.values():
        all_cells.update(cell)
    Log(all_cells)
    Log(len(all_cells))
    Log(len(cells))
    prepared = set()
    i = -1

    for i in range(1, side_x + 2):
        for j in range(1, side_y + 2):
            Log("#" if (i, j) in cells else ".", end="")
        Log()

    while i != 0:
        next_cell = max(cells, key=lambda k: len(cells[k]))
        i, j = [int(s) for s in Talk(next_cell).split()]
        for cell in cells:
            cells[cell] -= {(i, j)}
        prepared.add((i, j))
        # Log(prepared)
        Log(len(prepared))
        for x in range(1, side_x + 2):
            for y in range(1, side_y + 2):
                if (x, y) == (i, j):
                    Log("X", end="")
                elif (x, y) == next_cell:
                    Log("O", end="")
                elif (x, y) in prepared:
                    Log("#", end="")
                else:
                    Log(".", end="")
            Log()


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
