import sys
import math
from typing import Any, Callable, List, Optional, Tuple, TypeVar, Union


def to_bin(s: str) -> int:
    result = 0
    exp = 0
    for c in reversed(s):
        result += int(c) * 2 ** exp
        exp += 1
    return result


def solve(S: str, E: str) -> Optional[int]:
    target = to_bin(E)
    best = math.inf
    states: List[Tuple[int, float]] = [(to_bin(S), 0)]
    visited = {to_bin(S): 0.0}
    while states:
        number, operations = states.pop()
        if number == target:
            best = min(operations, best)
            continue

        operations += 1
        if operations >= best or number > 0xFFFFFFFF:
            continue

        # Shift
        shifted = number << 1
        if shifted in visited and operations < visited[shifted]:
            visited[shifted] = operations
            states.append((shifted, operations))
        elif shifted not in visited:
            visited[shifted] = operations
            states.append((shifted, operations))

        # Not
        notted = number ^ 0xFFFFFFFF

        if notted in visited and operations < visited[notted]:
            visited[notted] = operations
            states.append((notted, operations))
        elif notted not in visited:
            visited[notted] = operations
            states.append((notted, operations))

    return int(best) if best != math.inf else None


# def trim_left(n: str) -> str:
#     nozeroes: List[str] = []
#     left = True
#     for i in range(len(n)):
#         if n[i] == "0" and left:
#             pass
#         else:
#             left = False
#             nozeroes.append(n[i])
#     result = "".join(nozeroes)
#     if len(result) == 0:
#         result = "0"
#     return result


# def solve(S: str, target: str) -> Optional[int]:
#     best = math.inf
#     states: List[Tuple[str, float]] = [(S, 0)]
#     visited = {S: 0.0}
#     while states:
#         number, operations = states.pop()
#         if number == target:
#             best = min(operations, best)
#             continue

#         operations += 1
#         if operations >= best or operations > len(target) ** 2:
#             continue

#         # Shift
#         shifted = trim_left(number + "0")
#         if shifted in visited and operations < visited[shifted]:
#             visited[shifted] = operations
#             states.append((shifted, operations))
#         elif shifted not in visited:
#             visited[shifted] = operations
#             states.append((shifted, operations))

#         # Not
#         notted = ""
#         for c in number:
#             notted += "1" if c == "0" else "0"
#         notted = trim_left(notted)

#         if notted in visited and operations < visited[notted]:
#             visited[notted] = operations
#             states.append((notted, operations))
#         elif notted not in visited:
#             visited[notted] = operations
#             states.append((notted, operations))

#     return int(best) if best != math.inf else None


def solve_case(case: int):
    # Read data
    S, E = readmany()

    # Solve
    result = solve(S, E)

    # Write solution
    writesolution(case, result)


############################ Template code ###############################

T = TypeVar("T")


def read(typ: Callable[[str], T] = str) -> T:
    return typ(sys.stdin.readline().strip())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


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

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def main():
    T = read(int)
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()