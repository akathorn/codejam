import sys
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union

Segment = NamedTuple(
    "Segment", [("start", int), ("end", int), ("length", int), ("color", str)]
)


def row_to_segments(row: str) -> List[Segment]:
    segments = []
    start = 0
    color = row[0]
    for i, (color1, color2) in enumerate(zip(row, row[1:])):
        if color1 == color2:
            segments.append(Segment(start, i + 1, i - start + 1, color))
            start = i + 1
            color = color2
    segments.append(
        Segment(start, len(row), len(row) - start, color)
    )  # Close the last one
    return segments


def solve(rows_lines: List[str]) -> List[List[int]]:
    result = []

    for row in rows_lines:
        print(row)

    rows = [row_to_segments(r) for r in rows_lines]
    segment_length = lambda segment: segment.length
    biggest_segment = [max(row, key=segment_length) for row in rows]
    max_segment = max(biggest_segment, key=segment_length)
    current_length = max_segment.length

    # Find a candidate of a certain size
    while current_length > 1:
        rows_with_length = []
        for i, row in enumerate(rows):
            if any(segment.length >= current_length for segment in row):
                rows_with_length.append(i)
        candidates = []
        streak = [rows_with_length[0]]
        for row1, row2 in zip(rows_with_length, rows_with_length[1:]):
            if row1 + 1 == row2:
                streak.append(row2)
            elif len(streak) >= current_length:
                candidates.append(streak)
                streak = []
            else:
                streak = []
        if len(streak) >= current_length:
            candidates.append(streak)

        current_length -= 1

    result.append([1, sum(len(row) for row in rows)])

    return result  # [[1, 4], [5, 6], [5, 6]]


def solve_case(case: int):
    # Read data
    M, N = readmany(int)

    def str_to_row(s: str) -> str:
        binary = bin(int(s, base=16))
        binary = binary[2:].zfill(N)
        return binary
        # return [int(b) for b in binary]

    rows = [read(str_to_row) for _ in range(M)]

    # Solve
    result = solve(rows)

    # Write solution
    writesolution(case, result, print_length=True)


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


def writesolution(
    case: int, result: Union[Any, List[Any], None], print_length=False
) -> None:
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
    Finalize()


if __name__ == "__main__":
    main()