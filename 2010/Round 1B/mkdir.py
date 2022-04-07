from collections import defaultdict
import sys
from typing import Any, Callable, List, TypeVar, Union


def solve(existing: List[List[str]], create: List[List[str]]) -> int:
    tree = defaultdict(list)
    for dir in existing:
        path = ""
        for p, c in zip(dir, dir[1:]):
            path += p
            tree[path].append(c)

    ops = 0
    for new in create:
        path = ""
        for p, c in zip(new, new[1:]):
            path += p
            if c not in tree[path]:
                ops += 1
                tree[path].append(c)

    return ops


def solve_case(case: int):
    # Read data
    N, M = readmany(int)
    existing = [l[0].split("/") for l in readlines(N)]
    create = [l[0].split("/") for l in readlines(M)]

    # Solve
    result = solve(existing, create)

    # Write solution
    writesolution(case, result)


############################ Template code ###############################

T = TypeVar("T")


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


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    Output(f"Case #{case}: {out_string}")


class EndInteractive(Exception):
    pass


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    finally:
        Finalize()


if __name__ == "__main__":
    main()