from collections import defaultdict
import random
import itertools
import sys
from typing import Any, Callable, List, TypeVar, Union, Tuple, Optional

all_bits = ["".join(bits) for bits in itertools.product("01", repeat=8)]
bits_to_ones = {bits: bits.count("1") for bits in all_bits}
ones_to_bits = defaultdict(list)
for bits in all_bits:
    ones_to_bits[bits.count("1")].append(bits)


def possible_sums(a: str, b: str):
    res = set()
    for r in range(8):
        rotated = b[r:] + b[:r]
        res.add(bin(int(a, base=2) ^ int(rotated, base=2))[2:].zfill(8))
    return res


def solve_case(case: int):
    def send(bits: str) -> int:
        assert len(bits) == 8
        Output(bits)
        res = int(Input())
        if res == -1:
            raise EndInteractive()
        return res

    current = send("00000000")
    candidates = {bits for bits in all_bits if bits_to_ones[bits] == current}
    while current != 0:
        attempt = random.sample(candidates, 1)[0]
        current = send(attempt)
        new_candidates = set()
        for candidate in candidates:
            for result in possible_sums(candidate, attempt):
                if bits_to_ones[result] == current:
                    new_candidates.add(result)
        candidates = new_candidates


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    return sys.stdin.readline().strip()


def Output(s: Any):
    sys.stdout.write(str(s) + "\n")
    sys.stdout.flush()


def Log(*args: Any, **kwargs: Any):
    if "--log" in sys.argv:
        kwargs["file"] = sys.stderr
        print(*args, **kwargs)


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
    case: int, result: Union[Any, List[Any], None], print_length: bool = False
) -> str:
    """Prints the solution for one case.

    The result will be printed according to the type:
    - None:
        Case #{case}: IMPOSSIBLE
    - Single value:
        Case #{case}: {str(result)}
    - List/tuple:
        Case #{case}: {str(result[0]), str(result[1]), str(result[2]), ...}
    - List/tuple of lists/tuples:
        Case #{case}: {#rows if print_length == True}
        {str(result[0][0]), str(result[0][1]), ...}
        {str(result[1][0]), str(result[1][1]), ...}
        {str(result[2][0]), str(result[2][1]), ...}
        ...
    """
    if isinstance(result, list) or isinstance(result, tuple):
        if isinstance(result[0], list) or isinstance(result[0], tuple):
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
        tests = read(int)
        for case in range(1, tests + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()
