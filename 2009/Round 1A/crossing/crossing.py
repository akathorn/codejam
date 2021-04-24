import sys
import math
from typing import Any, Callable, Dict, List, NamedTuple, Tuple, TypeVar, Union


T = TypeVar("T")
class Intersection():
    def __init__(self, s: int, w: int, t: int, i: int, j: int) -> None:
        self.s = s
        self.w = w
        self.t = t
        self.i = i
        self.j = j
        self.state = "ew"
        # TODO: traffic light i starts a cycle by turning green in the north-south direction at t=Ti
        # minutes. There are cycles before t=Ti as well.
        self.time_left = self.t
        self.neighbors: Dict[str, Intersection] = {}


    def set_neighbours(self, N: int, M: int, intersections: List[List["Intersection"]]):
        if self.i > 0:
            self.neighbors["north"] = intersections[self.i-1][self.j]
        if self.i < N - 1:
            self.neighbors["south"] = intersections[self.i+1][self.j]
        if self.j > 0:
            self.neighbors["west"] = intersections[self.i][self.j-1]
        if self.j < M - 1:
            self.neighbors["east"] = intersections[self.i][self.j+1]

    def tick(self):
        self.time_left -=1
        if self.time_left == 0:
            if self.state == "ew":
                self.state = "ns"
                self.time_left = self.s
            else:
                self.state = "ew"
                self.time_left = self.w
            



def solve(N: int, M: int, intersections_input: List[List[Tuple[int, int, int]]]) -> int:
    intersections_map: List[List[Intersection]] = []
    for i in range(N):
        row = []
        intersections_map.append(row)
        for j in range(M):
            s, w, t = intersections_input[i][j]
            row.append(Intersection(s, w, t, i, j))

    for i in range(N):
        for j in range(M):
            intersections_map[i][j].set_neighbours(N, M, intersections_map)
    
    intersections = []
    for row in intersections_map:
        intersections.extend(row)

    positions = [(0, "sw", N-1, 0)]
    next_positions = []
    solution = math.inf
    while positions:
        positions
        next_positions = []
        for distance, corner, i, j in positions:
            if i == 0 and j == M-1:
                solution = min(distance, solution)
                continue
            elif distance > solution:
                continue
            # Stay
            next_positions.append((distance+1, corner, i, j))

            # Cross
            inter = intersections_map[i][j]
            if corner == "nw" and inter.state == "ew":
                next_positions.append((distance + 1, "ne", i, j))
            elif corner == "nw" and inter.state == "ns":
                next_positions.append((distance + 1, "sw", i, j))
            elif corner == "ne" and inter.state == "ew":
                next_positions.append((distance + 1, "ne", i, j))
            elif corner == "nw" and inter.state == "ns":
                next_positions.append((distance + 1, "sw", i, j))

            for direction, nbr_inter in inter.neighbors.items():
                if corner = "sw" and 
                if inter.state == "ew" and direction == "east" or direction == "west":
                    next_positions.append((distance + ))

        positions = next_positions
        for inter in intersections:
            inter.tick()
            


    return min(finished)


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def read2D(rows: int, typ: Callable[[str], T]) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = ""
            for row in result:
                out_string += "\n"
                for value in row:
                    out_string += str(value)
                    out_string += " "
                out_string.strip()
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    N, M = readmany(int)

    intersections = []
    for _ in range(N):
        row = []
        intersections.append(row)
        intersection_data = readmany(int)
        while intersection_data:
            S, W, T, *intersection_data = intersection_data
            row.append((S, W, T))

    result = solve(N, M, intersections)
    writesolution(case, result)


if __name__ == "__main__":
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)
