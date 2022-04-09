import itertools
import sys
import functools
from typing import Any, Callable, List, Set, Tuple, TypeVar, Union, Generator


@functools.lru_cache()
def value(r: int, k: int) -> int:
    if k == 1 or k == r:
        return 1
    return value(r - 1, k - 1) + value(r - 1, k)


@functools.lru_cache()
def neighbours(r: int, k: int) -> Set[Tuple[int, int]]:
    result = set()
    for i in (1, 0, -1):
        for j in (0, 1, -1):
            r2, k2 = r + i, k + j
            if (i != 0 or j != 0) and (r2 > 1) and (i * j != -1) and (0 < k2 <= r2 - 1):
                result.add((r2, k2))
    return result


def solve_rec(
    current: Tuple[int, int], visited: Set[Tuple[int, int]], total: int, N: int
) -> List[Tuple[int, int]]:
    new_total = total + value(*current)
    if new_total == N:
        return [current]
    if new_total > N:
        return []

    visited.add(current)
    for neighbour in neighbours(*current) - visited:
        res = solve_rec(neighbour, visited, new_total, N)
        if res:
            return [current] + res

    visited.remove(current)
    return []


# def solve_non_rec(N: int) -> List[Tuple[int, int]]:
#     path = [(1, 1)]
#     total = 1

#     while total != N:
#         if total < N:
#             for neighbour in neighbours(path[-1]):
#                 if neighbour not in path:
#                     path.append()


#     return path


def solve(N: int) -> List[List[int]]:
    return [list(s) for s in solve_rec((1, 1), set(), 0, N)]


def solve_case(case: int):
    # Read data
    N = read(int)

    # Solve
    try:
        result = solve(N)
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
        if isinstance(result[0], list):
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
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()