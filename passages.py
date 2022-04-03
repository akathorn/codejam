import sys
from typing import Any, Callable, List, TypeVar, Union


class WrongAnswer(Exception):
    pass


err = lambda s: sys.stderr.write(str(s) + "\n")


class Interactive:
    def __init__(self, N: int, K: int) -> None:
        self.N, self.K = N, K
        self.update_room()

    def update_room(self):
        self.room, self.passages = readmany(int)
        err(f"room: {self.room}, passages: {self.passages}")

    def walk(self):
        sys.stdout.write("W\n")
        self.update_room()

    def teleport(self, room: int):
        sys.stdout.write(f"T {room}\n")
        self.update_room()

    def guess(self, E: int):
        sys.stdout.write(f"E {E}\n")

    def solve(self):
        self.teleport(1)
        self.guess(0)


def solve_case(case: int):
    # Solve
    N, K = readmany(int)
    Interactive(N, K).solve()


############################ Template code ###############################

T = TypeVar("T")


def next_line() -> str:
    line = sys.stdin.readline().strip()
    err(line)
    return line


def read(typ: Callable[[str], T] = str) -> T:
    return typ(next_line())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in next_line().split()]


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
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except WrongAnswer:
        pass


if __name__ == "__main__":
    main()