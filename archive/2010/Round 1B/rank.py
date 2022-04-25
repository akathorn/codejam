import sys
import math
from typing import Any, Callable, List, TypeVar, Union, Tuple


def sequences(x: int, rank: int, n: int) -> List[List[Tuple[int, int]]]:
    # Base case?
    if x == n:
        return [[(n, rank)]]

    # General case
    seqs = []
    for y in range(x + 1, n + 1):
        if y - x > rank:
            for seq in sequences(y, y - x, n):
                seqs.append([(x, rank)] + seq)

    return seqs


def fill_numbers(sequences: List[List[Tuple[int, int]]]) -> int:
    total: int = 0
    for sequence in sequences:
        total_sequence = 1
        for gap in zip(sequence, sequence[1:]):
            (a, rank_a), (b, rank_b) = gap
            gap_size = rank_b - rank_a - 1
            if gap_size == 0:
                continue
            n_elements = b - a - 1
            total_sequence *= math.factorial(n_elements) / (
                math.factorial(gap_size) * math.factorial(n_elements - gap_size)
            )
            # total_sequence *= math.factorial(n_elements) / (
            #     math.factorial(gap_size) * math.factorial(n_elements - gap_size)
            # )
        total += int(total_sequence)
    return total


def solve(n: int) -> int:
    seqs = sequences(1, 0, n)
    print(seqs)

    return fill_numbers(seqs) % 100003


def solve_case(case: int):
    # Read data
    n = read(int)

    # Solve
    result = solve(n)

    # Write solution
    writesolution(case, result)


############################ Template code ###############################

T = TypeVar("T")


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

    Output(f"Case #{case}: {out_string}")


class EndInteractive(Exception):
    pass


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    finally:
        Finalize()


if __name__ == "__main__":
    main()