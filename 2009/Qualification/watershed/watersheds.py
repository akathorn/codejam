import sys
import itertools
from typing import Any, Callable, List, Tuple, TypeVar, Union


T = TypeVar("T")


def map_neighbors(
    i: int, j: int, H: int, W: int, _map: List[List[int]]
) -> List[Tuple[int, Tuple[int, int]]]:
    n = []
    if i > 0:
        n.append((_map[i - 1][j], (i - 1, j)))
    if j > 0:
        n.append((_map[i][j - 1], (i, j - 1)))
    if i < H - 1:
        n.append((_map[i + 1][j], (i + 1, j)))
    if j < W - 1:
        n.append((_map[i][j + 1], (i, j + 1)))

    return n


def solve(H: int, W: int, _map: List[List[int]]) -> List[List[str]]:
    if H == 1 and W == 1:
        return [["a"]]

    upstream = {(i, j): [] for i in range(H) for j in range(W)}
    sinks = set(upstream.keys())

    for i in range(H):
        for j in range(W):
            neighbors = map_neighbors(i, j, H, W, _map)
            down = min(neighbors)
            if down[0] < _map[i][j]:
                sinks.discard((i, j))
                upstream[down[1]].append((i, j))

    basin = {}
    for sink in sinks:
        points = [sink]
        while points:
            point = points.pop()
            basin[point] = sink
            points.extend(upstream[point])

    result = []
    sink_name = {}
    c = 97
    for i in range(H):
        row = []
        result.append(row)
        for j in range(W):
            b = basin[(i, j)]
            if b not in sink_name:
                sink_name[b] = chr(c)
                c += 1
            row.append(sink_name[b])

    return result


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    H, W = readmany(int)
    _map = []
    for _ in range(H):
        _map.append(readmany(int))

    result = solve(H, W, _map)

    result_str = ""
    for row in result:
        result_str += "\n"
        for point in row:
            result_str += str(point)
            result_str += " "
        result_str.strip()

    writesolution(case, result_str)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()