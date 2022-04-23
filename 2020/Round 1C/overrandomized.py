import itertools
import sys
from typing import Any, Callable, Dict, List, Set, TypeVar, Union, Tuple, Optional


def init_letters(queries: List[Tuple[int, str]]) -> Dict[str, int]:
    letters = set()
    for _, r in queries:
        letters.update(set(r))
    letters = list(letters)
    letters.sort()
    letters = {l: i for i, l in enumerate(letters)}
    return letters


def solve(U: int, queries: List[Tuple[int, str]]) -> str:
    letters = init_letters(queries)

    skip: Tuple[int, int] = (-1, -1)
    mapping = [0] * 10
    for mapping in itertools.permutations(range(10)):
        if mapping[skip[0]] == skip[1]:
            continue

        found = True
        for m, r in queries:
            n = 0
            i = 0
            for l in reversed(r):
                n += 10 ** i * mapping[letters[l]]
                i += 1
            if n > m or n == 0:
                found = False
                if m >= 10 ** (i - 1):
                    skip = (mapping.index(letters[l]), mapping[letters[l]])
                break
        if found:
            break

    if not found:
        raise Exception()

    result = [""] * 10
    for k, v in letters.items():
        result[mapping[v]] = k

    return "".join(result)


def solve_case(case: int):
    # Read data
    U = read(int)
    queries = [(int(q), r) for q, r in readlines(10000)]

    # Solve
    try:
        result = solve(U, queries)
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
