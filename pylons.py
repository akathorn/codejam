import math
import sys
from typing import (
    Any,
    Callable,
    Dict,
    List,
    NamedTuple,
    Optional,
    Set,
    TypeVar,
    Union,
    Tuple,
)


if not "--log" in sys.argv:

    def fake_print(*args, **kwargs):
        return None

    print = fake_print

Cell = Tuple[int, int]
State = NamedTuple("State", [("visited", Set[Cell]), ("path", List[Cell])])


def are_connected(c1, c2):
    # fmt: off
    if (c1[0] == c2[0]) or \
        (c1[1] == c2[1]) or \
        (c1[0] + c1[1] == c2[0] + c2[1]) or \
        (c1[0] - c1[1] == c2[0] - c2[1]):
        return True
    # fmt: on


def solve(R: int, C: int) -> Optional[List[Cell]]:
    cells: List[Cell] = [(i + 1, j + 1) for i in range(R) for j in range(C)]
    graph: Dict[Cell, Set[Cell]] = {}
    for cell in cells:
        graph[cell] = {other for other in cells if not are_connected(cell, other)}

    states: List[State] = [State({start}, [start]) for start in cells]
    while states:
        current = states.pop()
        if len(current.path) == len(cells):
            return current.path
        for other in graph[current.path[-1]] - current.visited:
            new_visited = set(current.visited)
            new_visited.add(other)
            states.append(State(new_visited, current.path + [other]))

    return None


def solve_case(case: int):
    # Read data
    R, C = readmany(int)

    # Solve
    try:
        result = solve(R, C)
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


def Output(s: str):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


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
    case: int, result: Union[Any, List[Any], None], print_length=False
) -> str:
    """Prints the solution for one case.

    The result will be printed according to the type:
    - None:
        Case #{case}: IMPOSSIBLE
    - Single value:
        Case #{case}: {str(result)}
    - List:
        Case #{case}: {str(result[0]), str(result[1]), str(result[2]), ...}
    - List of lists:
        Case #{case}: {#rows if print_length == True}
        {str(result[0][0]), str(result[0][1]), ...}
        {str(result[1][0]), str(result[1][1]), ...}
        {str(result[2][0]), str(result[2][1]), ...}
        ...
    """
    if isinstance(result, list):
        if isinstance(result[0], list) or isinstance(result[0], tuple):
            out_string = str(len(result)) if print_length else ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        return f"Case #{case}: IMPOSSIBLE"
    else:
        out_string = str(result)

    return f"Case #{case}: POSSIBLE{out_string}"


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()