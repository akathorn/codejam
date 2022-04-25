import sys
from typing import Any, Callable, List, Tuple, TypeVar, Union


T = TypeVar("T")


def solve(symbols: str) -> int:
    new_symbols, base = to_minimum(symbols)

    return to_base_10(new_symbols, base)


def to_base_10(symbols: str, base: int) -> int:
    result = 0
    exp = 0
    for c in reversed(symbols):
        if c in [str(d) for d in range(10)]:
            value = int(c)
        else:
            value = ord(c) - 87
        result += value * (base ** exp)
        exp += 1
    return result


def to_minimum(symbols: str) -> Tuple[str, int]:
    result_str = "1"
    mapping = {symbols[0]: "1"}
    counter = 0
    for c in symbols[1:]:
        if c not in mapping:
            if counter == 0:
                mapping[c] = "0"
                counter = 2
            elif counter < 10:
                mapping[c] = str(counter)
                counter += 1
            else:
                mapping[c] = chr(counter)
                counter += 1
        result_str += mapping[c]

    return result_str, max(counter, 2)


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
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def solve_case(case: int):
    # Read data
    symbols = readstring()

    # Solve
    result = solve(symbols)

    # Write solution
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()