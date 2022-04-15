import collections
import sys
from typing import Any, Callable, Dict, List, NamedTuple, Tuple, TypeVar, Union


if not "--log" in sys.argv:

    def fake_print(*args, **kwargs):
        return None

    print = fake_print


Person = Tuple[int, int]
Interval = List[int]


def solve_axis(persons: List[Person], Q: int) -> int:
    # TODO: optimize by saving as intervals
    count = [0] * (Q + 1)
    for person in persons:
        intersection = person[0] + person[1]
        while 0 <= intersection <= Q:
            count[intersection] += 1
            intersection = intersection + person[1]
    return count.index(max(count))


# TODO: this version works for the samples, very efficiently, but fails on the test set
# def solve_axis(persons: List[Person], Q: int) -> int:
#     intervals: List[Interval] = [[0, Q, 0]]

#     max_interval = intervals[0]
#     for p, d in persons:
#         if d == 1:
#             i = 0
#             while intervals[i][0] > p:
#                 i += 1
#             if intervals[i][0] < p:
#                 start = intervals[i][0]
#                 end = p
#                 count = intervals[i][2]
#                 intervals.insert(i, [start, end, count])
#                 intervals[i + 1][0] = p + 1
#             for interval in intervals[i + 1 :]:
#                 interval[2] += 1
#                 if interval[2] > max_interval[2]:
#                     max_interval = interval
#                 elif interval[2] == max_interval[2] and interval[0] < max_interval[0]:
#                     max_interval = interval
#         else:
#             i = -1
#             while intervals[i][1] < p:
#                 i -= 1
#             if intervals[i][1] > p:
#                 start = p
#                 end = intervals[i][1]
#                 count = intervals[i][2]
#                 intervals.insert(len(intervals) + i + 1, [start, end, count])
#                 intervals[i - 1][1] = p - 1
#             for interval in reversed(intervals[:i]):
#                 interval[2] += 1
#                 if interval[2] > max_interval[2]:
#                     max_interval = interval
#                 elif interval[2] == max_interval[2] and interval[0] < max_interval[0]:
#                     max_interval = interval

#     return max_interval[0]


def solve(persons: List[List[str]], Q: int) -> Tuple[int, int]:
    NS = []
    EW = []
    for x, y, d in persons:
        if d in ("N", "S"):
            NS.append((int(y), 1 if d == "N" else -1))
        else:
            EW.append((int(x), 1 if d == "E" else -1))

    return (solve_axis(EW, Q), solve_axis(NS, Q))


def solve_case(case: int):
    # Read data
    P, Q = readmany(int)

    # Solve
    try:
        result = solve(readlines(P), Q)
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