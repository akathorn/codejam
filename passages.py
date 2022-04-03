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
        # err(f"room: {self.room}, passages: {self.passages}")

    def walk(self):
        Output("W\n")

    def teleport(self, room: int):
        Output(f"T {room}\n")

    def guess(self, E: int):
        Output(f"E {E}\n")

    def solve(self):
        self.guess(0)


def solve_case(case: int):
    # Solve
    N, K = readmany(int)
    Interactive(N, K).solve()


############################ Template code ###############################

T = TypeVar("T")


def Input() -> str:
    line = sys.stdin.readline().strip()
    # err(line)
    return line


def Output(s: str):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def read(typ: Callable[[str], T] = str) -> T:
    return typ(Input())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in Input().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except WrongAnswer:
        sys.stdout.close()


if __name__ == "__main__":
    main()