import math
import sys
import itertools
from typing import Any, Callable, List, NamedTuple, TypeVar, Union, Tuple, Optional


def cost(start: int, a: int, b: int, c: int):
    return abs(start - a) + abs(a - b) + abs(b - c)


def solve_simple(P: List[List[int]]) -> int:
    if len(P[0]) < 3:
        for costumer in P:
            costumer.append(costumer[-1])

    states: List[Tuple[int, int, List[List[int]]]] = [(0, 0, P)]
    min_cost = math.inf
    while states:
        pressure, cst, costumers = states.pop()
        if not costumers:
            min_cost = min(min_cost, cst)
            continue
        costumer, *costumers = costumers
        a, b, c = costumer
        states.append(
            (c, cst + min(cost(pressure, a, b, c), cost(pressure, b, a, c)), costumers)
        )
        states.append(
            (b, cst + min(cost(pressure, a, c, b), cost(pressure, c, a, b)), costumers)
        )
        states.append(
            (a, cst + min(cost(pressure, b, c, a), cost(pressure, c, b, a)), costumers)
        )

    return int(min_cost)


def solve(P: List[List[int]]) -> int:
    if len(P[0]) <= 3:
        return solve_simple(P)

    # i = 0
    # total = 0
    # current = 0
    # for customer in P:
    #     a, b = min(customer), max(customer)
    #     if i % 2 == 1:
    #         a, b = b, a
    #     total += abs(current - a)
    #     total += abs(a - b)
    #     current = b
    #     i += 1

    # return total


def solve_case(case: int):
    # Read data
    N, _ = readmany(int)
    P = readlines(N, int)

    # Solve
    try:
        result = solve(P)
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
