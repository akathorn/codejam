# 2019 1C - robot
import sys
from typing import Any, Callable, List, Sequence, TypeVar, Union, Tuple, Optional


def winner_move(hand: str) -> str:
    if hand == "P":
        return "S"
    if hand == "S":
        return "R"
    else:
        return "P"


def compare_moves(a: str, b: str) -> int:
    """1 if a wins, 1 if b wins, 0 if tie"""
    if winner_move(a) == b:
        return -1
    if winner_move(b) == a:
        return 1
    return 0


def compare_program(a: str, b: str) -> int:
    """1 if a wins, 1 if b wins, 0 if tie"""
    i = 0
    first = True
    while first or not (i % len(a) == 0 and i % len(b) == 0):
        first = False
        winner = compare_moves(a[i % len(a)], b[i % len(b)])
        if winner:
            return winner
        i += 1
    return 0


def solve(programs: List[str]) -> Optional[str]:
    # (solution, program index)
    states: List[Tuple[str, int]] = [("R", 0), ("P", 0), ("S", 0)]
    while states:
        sol, i = states.pop()
        if len(sol) > 500:
            continue
        if i == len(programs):
            return sol

        program = programs[i]

        if compare_program(sol, program) == 1:
            states.append((sol, i + 1))
        elif compare_program(sol, program) == 0:
            for hand in "S", "P", "R":
                if compare_program(sol + hand, program) > 1:
                    states.append((sol + hand, i + 1))

    return None


def solve_case(case: int):
    # Read data
    programs = [l[0] for l in Readlines(Read(int))]

    # Solve
    try:
        result = solve(programs)
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
    return line


def Output(s: Any):
    sys.stdout.write(str(s) + "\n")
    sys.stdout.flush()


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
