import sys
import random
from typing import Any, Callable, List, TypeVar, Union


class WrongAnswer(Exception):
    pass


err = lambda s: (sys.stderr.write(str(s) + "\n"), sys.stderr.flush())


class Interactive:
    def __init__(self, N: int, K: int) -> None:
        self.N, self.K = N, K
        self.update_room()

    def update_room(self):
        self.room, self.passages = readmany(int)

    def walk(self):
        Output("W")
        self.update_room()

    def teleport(self, room: int):
        Output(f"T {room}")
        self.update_room()

    def guess(self, E: int):
        Output(f"E {E}")

    def solve(self):
        passages = self.passages
        rooms = list(range(1, self.N + 1))
        random.shuffle(rooms)
        for room in rooms[: self.K]:
            self.teleport(room)
            passages += self.passages

        average_passages = passages / self.K
        self.guess(int((average_passages * self.N) / 2))


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
        pass
    finally:
        sys.stdout.close()
        sys.stderr.close()


if __name__ == "__main__":
    main()