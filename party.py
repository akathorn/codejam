# 2018 1A - party
import itertools
import math
import sys
from typing import (
    Any,
    Callable,
    List,
    NamedTuple,
    Sequence,
    TypeVar,
    Union,
    Tuple,
    Optional,
)


# Used for interactive problems
WRONG_ANSWER = ...


def total_time(bits: int, cashier: Tuple[int, int, int]) -> int:
    bits = min(bits, cashier[0])
    return bits * cashier[1] + cashier[2]


def solve_bruteforce(
    robots: int, bits: int, cashiers: List[Tuple[int, int, int]]
) -> int:
    best_time = math.inf
    for n in range(1, robots + 1):
        for selected in itertools.permutations(cashiers, r=n):
            solutions = [[0] * len(selected)]
            while solutions:
                solution = solutions.pop()
                if sum(solution) == bits:
                    longest = max(
                        b * cashier[1] + cashier[2]
                        for b, cashier in zip(solution, selected)
                    )
                    best_time = min(longest, best_time)
                else:
                    for i, cashier in enumerate(selected):
                        if solution[i] + 1 <= cashier[0]:
                            new_sol = list(solution)
                            new_sol[i] += 1
                            solutions.append(new_sol)
    return int(best_time)


# maximum, scan time, payment time
Cashier = NamedTuple("Cashier", [("m", int), ("s", int), ("p", int)])


def solve(robots: int, bits: int, cashiers_tuples: List[Tuple[int, int, int]]) -> int:
    # return solve_bruteforce(robots, bits, cashiers)
    cashiers: List[Cashier] = [Cashier(*c) for c in cashiers_tuples]
    C = len(cashiers)

    b = [0] * C
    i = 0
    while bits:
        b[i] += min(cashiers[i].m, bits)
        bits -= min(cashiers[i].m, bits)
        i += 1
        robots -= 1

    cost = lambda i: b[i] * cashiers[i].s + cashiers[i].p

    done = False
    max_cost = math.inf
    while not done:
        done = True
        i = max(range(C), key=lambda i: b[i] * cashiers[i].s + cashiers[i].p)
        max_cost = cost(i)
        for j in range(C):
            if i == j:
                continue

            if b[j] == 0 and not robots:
                b[i], b[j] = b[j], b[i]
                if cost(j) < max_cost:
                    done = False
                    break
                b[i], b[j] = b[j], b[i]
                continue

            change = (cost(i) - cost(j)) / (cashiers[i].s + cashiers[j].s)
            change = min(b[i], round(change), cashiers[j].m - b[j])
            if not change:
                continue

            b[i] -= change
            b[j] += change
            if b[i] == 0:
                if cost(j) < max_cost:
                    robots += 1
                    done = False
                    break
            elif cost(j) < max_cost:
                done = False
                break
            b[i] += change
            b[j] -= change

    return int(max_cost)


def solve_case(case: int):
    # Read data
    robots, bits, C = Readmany(int)
    cashiers = [(m, s, p) for (m, s, p) in Readlines(C, int)]

    # Solve
    try:
        result = solve(robots, bits, cashiers)
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
