import sys
from typing import Any, Callable, List, Optional, TypeVar, Union


def solve(
    K: int, B: int, T: int, locations: List[int], speeds: List[int]
) -> Optional[int]:
    t = 0
    chicks = list(zip(locations, speeds))
    chicks.sort(reverse=True)

    swaps = 0
    can_reach = 0
    cant_reach = 0
    for location, speed in chicks:
        if (B - location) / speed > T:
            cant_reach += 1
        else:
            can_reach += 1
            swaps += cant_reach
        if can_reach == K:
            break

    return swaps if (can_reach == K) else None


def solve_case(case: int):
    # Read data
    N, K, B, T = readmany(int)
    locations = readmany(int)
    speeds = readmany(int)

    # Solve
    result = solve(K, B, T, locations, speeds)

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