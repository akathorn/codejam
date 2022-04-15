from collections import Counter
import itertools
import sys
from typing import Any, Callable, List, TypeVar, Union


if not "--log" in sys.argv:

    def fake_print(*args, **kwargs):
        return None

    print = fake_print


# Bruteforce
def solve(C: List[int], D: List[int], K: int) -> int:
    choices = 0
    for L in range(len(C)):
        for R in range(L, len(C)):
            if abs(max(C[L : R + 1]) - max(D[L : R + 1])) <= K:
                choices += 1
    return choices


# def max_skill(counter: Counter) -> int:


# def within_K(c_counter: Counter, d_counter: Counter, K: int) -> bool:


# def solve(C: List[int], D: List[int], K: int) -> int:
#     choices = 0
#     c_counter = Counter()
#     d_counter = Counter()
#     for L in range(len(C)):
#         for R in range(L, len(C)):
#             c_counter[C[R]] += 1
#             d_counter[D[R]] += 1
#             within_K(c_counter, d_counter, K)
#         c_counter = Counter()
#         d_counter = Counter()
#     return choices


def solve_case(case: int):
    # Read data
    _, K = readmany(int)
    C = readmany(int)
    D = readmany(int)

    # Solve
    try:
        result = solve(C, D, K)
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
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()