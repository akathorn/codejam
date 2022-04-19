import math
import sys
from typing import Any, Callable, List, Tuple, TypeVar, Union


# def neighbours(stalls: List[bool], n: int) -> Tuple[int, int]:
#     left = 0
#     for i in range(n - 1, -1, -1):
#         if not stalls[i]:
#             left += 1
#         else:
#             break
#     right = 0
#     for i in range(n + 1, len(stalls)):
#         if not stalls[i]:
#             right += 1
#         else:
#             break
#     return left, right


# def solve_bruteforce(nstalls: int, people: int) -> Tuple[int, int]:
#     stalls = [True] + [False for _ in range(nstalls)] + [True]
#     best = stalls[1:].index(True)
#     best_left, best_right = neighbours(stalls, best)
#     while people:
#         for stall in [
#             stall for stall, occupied in enumerate(stalls[2:], 2) if not occupied
#         ]:
#             left, right = neighbours(stalls, stall)
#             if (left == best_left and right > best_right) or (left > best_left):
#                 best = stall
#                 best_left, best_right = left, right
#         people -= 1
#         stalls[best] = True
#         best = stalls[1:].index(True)
#         best_left, best_right = neighbours(stalls, best)
#     return max(best_left, best_right), min(best_left, best_right)


def solve1(stalls: int, people: int) -> Tuple[int, int]:
    stalls_left = math.ceil(stalls / 2)
    stalls_right = math.floor(stalls / 2)
    people_left = math.ceil(people / 2)
    people_right = math.floor(people / 2)

    # Base case
    if people == 1:
        return stalls_right, stalls_left - 1

    if people_left > people_right or stalls_left > stalls_right:
        return solve(stalls_left, people_left)
    else:
        return solve(stalls_right, people_right)


# @functools.lru_cache()
def solve(stalls: int, people: int) -> Tuple[int, int]:
    res1 = stalls / (2 ** (people - 1))
    res2 = res1 / 2
    return round(res2), round(res2) - (1 if math.ceil(res1) % 2 == 0 else 0)


def solve_case(case: int):
    # Read data
    N, K = readmany(int)

    # Solve
    try:
        result = solve(N, K)
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