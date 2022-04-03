import sys
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def toggle(index: int, snappers: List[bool]) -> None:
    snappers[index] = False if snappers[index] else True


def solve(nsnappers: int, nsnaps: int) -> bool:
    return bin(nsnaps)[-nsnappers:] == bin(2 ** nsnappers - 1)[-nsnappers:]

    # state = [False] * nsnappers
    # powered = [False] * (nsnappers + 1)

    # result = False
    # for i in range(nsnaps):
    #     index = 1
    #     powered[0] = True
    #     while index < len(powered):
    #         if powered[index - 1] and state[index - 1]:
    #             powered[index] = True
    #         else:
    #             powered[index] = False
    #         index += 1

    #     index = 0
    #     while index < nsnappers and powered[index]:
    #         toggle(index, state)
    #         index += 1

    # powered[0] = True
    # index = 1
    # while index < len(powered):
    #     if powered[index - 1] and state[index - 1]:
    #         powered[index] = True
    #     else:
    #         powered[index] = False
    #     index += 1

    # return powered[-1]


def read(typ: Callable[[str], T] = str) -> T:
    return typ(sys.stdin.readline().strip())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if result:
        out_string = "ON"
    else:
        out_string = "OFF"

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def solve_case(case: int):
    # Read data
    N, K = readmany(int)  # TODO: delete

    # Solve
    result = solve(N, K)

    # Write solution
    writesolution(case, result)


def main():
    T = read(int)
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()