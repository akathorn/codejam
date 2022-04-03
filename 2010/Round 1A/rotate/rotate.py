import sys
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union


def solve(K: int, N: int, board: List[List[str]]) -> Tuple[bool, bool]:
    rotated = rotate(board)
    blue = connect_K(K, N, "B", rotated)
    red = connect_K(K, N, "R", rotated)
    result = blue, red
    return result


def rotate(board: List[List[str]]) -> List[List[str]]:
    N = len(board)

    board2 = [["." for _ in range(N)] for _ in range(N)]
    for i in range(N):
        new_j = 0
        for j in range(N - 1, -1, -1):
            if board[i][j] != ".":
                board2[i][new_j] = board[i][j]
                new_j += 1

    board3 = [["." for _ in range(N)] for _ in range(N)]
    for j in range(N):
        new_i = N - 1
        for i in range(N - 1, -1, -1):
            if board2[i][j] != ".":
                board3[new_i][j] = board2[i][j]
                new_i -= 1
    return board3


def connect_K(K: int, N: int, player: str, board: List[List[str]]) -> bool:
    # Horizontal
    for i in range(N):
        connected = 0
        for j in range(N):
            if board[i][j] == player:
                connected += 1
            else:
                connected = 0
            if connected == K:
                return True

    # Vertical
    for j in range(N):
        connected = 0
        for i in range(N):
            if board[i][j] == player:
                connected += 1
            else:
                connected = 0
            if connected == K:
                return True

    # Diagonal \
    connected = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == player:
                if i < 1 or j < 1:
                    connected[i][j] = 1
                else:
                    connected[i][j] = connected[i - 1][j - 1] + 1
            if connected[i][j] == K:
                return True

    # Diagonal /
    connected = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == player:
                if i < 1 or j == N - 1:
                    connected[i][j] = 1
                else:
                    connected[i][j] = connected[i - 1][j + 1] + 1
            if connected[i][j] == K:
                return True

    return False


def solve_case(case: int):
    # Read data
    N, K = readmany(int)
    board: List[List[str]] = []
    for _ in range(N):
        row: List[str] = []
        board.append(row)
        for c in read(str):
            row.append(c)

    # Solve
    result = solve(K, N, board)

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


def writesolution(case: int, result: Tuple[bool, bool]) -> None:
    blue, red = result
    if blue and red:
        out_string = "Both"
    elif blue:
        out_string = "Blue"
    elif red:
        out_string = "Red"
    else:
        out_string = "Neither"

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def main():
    T = read(int)
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()