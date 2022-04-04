import sys
from typing import Any, Callable, List, TypeVar, Union, Optional


def solve(printers) -> Optional[List[int]]:
    ink = [min(i) for i in zip(*printers)]
    if sum(ink) < 1e6:
        return None

    remaining = 1e6
    result = []
    for i in ink:
        add = min(i, remaining)
        result.append(int(add))
        remaining -= add

    return result


def solve2(printers):
    printer_1 = printers[0]
    printer_2 = printers[1]
    printer_3 = printers[2]

    min_cyan = min(printer_1[0], printer_2[0], printer_3[0])
    min_magenta = min(printer_1[1], printer_2[1], printer_3[1])
    min_yellow = min(printer_1[2], printer_2[2], printer_3[2])
    min_black = min(printer_1[3], printer_2[3], printer_3[3])

    total = min_cyan + min_magenta + min_yellow + min_black

    if total == 1000000:
        return [min_cyan, min_magenta, min_yellow, min_black]

    elif total > 1000000:
        difference = total - 1000000

        if min_cyan >= difference:
            min_cyan -= difference
            return [min_cyan, min_magenta, min_yellow, min_black]
        else:
            difference -= min_cyan
            min_cyan = 0
        if min_magenta >= difference:
            min_magenta -= difference
            return [min_cyan, min_magenta, min_yellow, min_black]
        else:
            difference -= min_magenta
            min_magenta = 0
        if min_yellow >= difference:
            min_yellow -= difference
            return [min_cyan, min_magenta, min_yellow, min_black]
        else:
            difference -= min_yellow
            min_yellow = 0
        min_black -= difference
        return [min_cyan, min_magenta, min_yellow, min_black]

    return None


def solve_case(case: int):
    # Read data
    printers = readlines(3, int)

    # Solve
    result = solve(printers)

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
    T = read(int)
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()