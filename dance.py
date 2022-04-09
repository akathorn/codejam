import sys
from typing import Any, Callable, Dict, List, TypeVar, Union, Tuple

Position = Tuple[int, int]


class Dancers:
    def __init__(self, skills: List[List[int]]) -> None:
        self.R, self.C = len(skills), len(skills[0])
        self._skills: Dict[Position, int] = {
            (i, j): skills[i][j] for j in range(self.C) for i in range(self.R)
        }
        self._neighbours: Dict[Position, Dict[Position, Position]] = {}
        for i in range(self.R):
            for j in range(self.C):
                self._neighbours[(i, j)] = {}
                for d in -1, 1:
                    if 0 <= i + d < self.R:
                        self._neighbours[(i, j)][(d, 0)] = (i + d, j)
                    if 0 <= j + d < self.C:
                        self._neighbours[(i, j)][(0, d)] = (i, j + d)

        self.interest = sum(self._skills.values())

    # def neighbours(self, dancer: Position) -> Dict[Position, Position]:
    #     i, j = dancer
    #     for d in -1, 1:
    #         if 0 <= i + d < R:
    #             self._neighbours[(i, j)][(d, 0)] = (i + d, j)
    #         if 0 <= j + d < C:
    #             self._neighbours[(i, j)][(0, d)] = (i, j + d)

    def next_round(self) -> bool:
        eliminate: List[Position] = []
        for dancer in self._skills.keys():
            neighbours = self._neighbours[dancer].values()
            if not neighbours:
                continue
            average = sum(self._skills[neighbour] for neighbour in neighbours) / len(
                neighbours
            )
            if self._skills[dancer] < average:
                eliminate.append(dancer)
        for dancer in eliminate:
            self._eliminate_dancer(dancer)
        return len(eliminate) > 0

    def _eliminate_dancer(self, dancer: Position):
        neighbours = self._neighbours[dancer]
        for d1 in neighbours.keys():
            d2 = (d1[0] * -1, d1[1] * -1)
            if d2 in neighbours:
                self._neighbours[neighbours[d1]][d2] = neighbours[d2]
            else:
                del self._neighbours[neighbours[d1]][d2]
        self.interest -= self._skills[dancer]
        del self._neighbours[dancer]
        del self._skills[dancer]

    def run(self) -> int:
        total_interest = self.interest
        while self.next_round():
            total_interest += self.interest
        return total_interest


def solve(skills: List[List[int]]) -> int:
    dancers = Dancers(skills)
    interest = dancers.run()

    return interest


def solve_case(case: int):
    # Read data
    R, _ = readmany(int)
    dancers = readlines(R, int)

    # Solve
    try:
        result = solve(dancers)
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