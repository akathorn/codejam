# 2022 1C - tower
from collections import defaultdict
import itertools
import sys
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Sequence,
    Set,
    TypeVar,
    Union,
    Tuple,
    Optional,
)


# Used for interactive problems
WRONG_ANSWER = ...

sys.setrecursionlimit(10000)


def is_megatower(tower) -> bool:
    seen = []
    i = 0
    while i < len(tower):
        letter = tower[i]
        if letter in seen:
            return False
        seen.append(letter)
        while i < len(tower) and tower[i] == letter:
            i += 1
    return True


def choices(towers: List[str]):
    for i in range(len(towers)):
        yield towers[i], towers[:i] + towers[i + 1 :]


def solve_bruteforce(towers: List[str]) -> Optional[str]:
    if not all(is_megatower(t) for t in towers):
        return None
    states: List[Tuple[str, List[str]]] = [("", towers)]
    while states:
        mega, remaining = states.pop()
        if not remaining:
            return mega

        for tower, rest in choices(remaining):
            new = mega + tower
            if is_megatower(new):
                states.append((new, rest))

    return None


# def build_tower(
#     acc: str,
#     towers: List[str],
#     graph: Dict[str, Set[str]],
#     no_intersect: Dict[str, Set[str]],
# ) -> Optional[str]:
#     if towers == []:
#         return acc

#     for other in graph[acc[-1]]:
#         if other in towers:
#             towers.remove(other)
#             res = build_tower(acc + other, towers, graph, no_intersect)
#             if res:
#                 return res
#             towers.append(other)

#     for other in no_intersect[]:
#         if other in towers:
#             towers.remove(other)
#             res = build_tower(acc + other, towers, graph, no_intersect)
#             if res:
#                 return res
#             towers.append(other)

#     return None


# def solve(towers: List[str]) -> Optional[str]:
#     if not all(is_megatower(t) for t in towers):
#         return None

#     graph = defaultdict(set)
#     no_intersect = defaultdict(set)

#     for a, b in itertools.combinations(towers, 2):
#         if set(a).intersection(b):
#             if a[-1] == b[0]:
#                 graph[a[-1]].add(b)
#             if b[-1] == a[0]:
#                 graph[b[-1]].add(a)
#             if a[-1] != b[0] and b[-1] != a[0]:
#                 return None
#         else:
#             no_intersect[a].add(b)
#             no_intersect[b].add(a)

#     for tower, rest in choices(towers):
#         res = build_tower(tower, rest, graph, no_intersect)
#         if res:
#             return "".join(res)

#     return None


def solve(towers: List[str]) -> Optional[str]:
    if not all(is_megatower(t) for t in towers):
        return None

    merged = [set(towers)]
    done = False
    while not done:
        done = True
        for tows in merged:
            remove = False
            for a, b in itertools.combinations(tows, 2):
                if set(a).intersection(b):
                    done = False
                    remove = True
                    if a[-1] == b[0]:
                        if is_megatower(a + b):
                            new_tows = set(tows)
                            new_tows.remove(a)
                            new_tows.remove(b)
                            new_tows.add(a + b)
                            merged.append(new_tows)
                    if b[-1] == a[0]:
                        if is_megatower(b + a):
                            new_tows = set(tows)
                            new_tows.remove(a)
                            new_tows.remove(b)
                            new_tows.add(b + a)
                            merged.append(new_tows)
                    continue
            if remove:
                merged.remove(tows)

    if merged:
        return "".join(merged[0])
    else:
        return None


def solve_case(case: int):
    # Read data
    N = Read(int)
    towers = Readmany()

    # Solve
    try:
        result = solve(towers)
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
