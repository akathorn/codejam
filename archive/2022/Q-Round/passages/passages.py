import sys
import random
from typing import Any, Callable, List, TypeVar, Union


class WrongAnswer(Exception):
    pass


err = lambda s: (sys.stderr.write(str(s) + "\n"), sys.stderr.flush())


class Interactive:
    def __init__(self, N: int, K: int) -> None:
        self.N, self.K = N, K
        self.visited = set()
        self.update_room()

    def update_room(self) -> bool:
        self.room, self.passages = readmany(int)
        if self.room in self.visited:
            return False
        else:
            self.visited.add(self.room)
            return True

    def walk(self) -> bool:
        Output("W")
        return self.update_room()

    def teleport(self, room: int):
        Output(f"T {room}")
        self.update_room()

    def guess(self, E: int):
        Output(f"E {E}")

    # # Jump when reaching a visited room
    # def solve(self):
    #     passages = 0
    #     K = self.K
    #     while K:
    #         K -= 1
    #         passages += self.passages
    #         if not self.walk() and K:
    #             room = random.randint(1, self.N)
    #             while room in self.visited:
    #                 room = random.randint(1, self.N)
    #             self.teleport(room)
    #             K -= 1
    #     passages += self.passages

    #     average_passages = passages / len(self.visited)
    #     self.guess(int((average_passages * self.N) / 2))

    # Don't always jump when reaching a visisted room
    def solve(self):
        passages = 0
        K = self.K
        while K:
            K -= 1
            passages += self.passages
            if not self.walk() and random.random() < 0.9 and K:
                room = random.randint(1, self.N)
                while room in self.visited:
                    room = random.randint(1, self.N)
                self.teleport(room)
                K -= 1
        passages += self.passages

        average_passages = passages / len(self.visited)
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


def Finalize():
    sys.stdout.close()
    sys.stderr.close()


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
        Finalize()


if __name__ == "__main__":
    main()