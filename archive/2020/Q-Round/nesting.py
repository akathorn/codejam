import sys
from typing import Any, Callable, List, NamedTuple, Optional, TypeVar, Union


P = NamedTuple(
    "P", [("parent", "P"), ("children", Union[int, List["P"]]), ("depth", int)]
)


def to_string(p: P) -> str:
    res = ""
    for child in p.children:
        if isinstance(child, int):
            res += str(child)
        else:
            res += f"({to_string(child)})"
    return res


def solve(S) -> str:
    root = P(None, [], 0)  # type: ignore
    current = root
    for s in S:
        while current.depth != s:
            if current.depth > s:
                current = current.parent
            else:
                new = P(current, [], current.depth + 1)
                current.children.append(new)  # type: ignore
                current = new
        current.children.append(s)  # type: ignore

    return to_string(root)


def solve_case(case: int):
    # Read data
    S = [int(c) for c in read(str)]

    # Solve
    result = solve(S)

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


def writesolution(
    case: int, result: Union[Any, List[Any], None], print_length=False
) -> None:
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
    Finalize()


if __name__ == "__main__":
    main()