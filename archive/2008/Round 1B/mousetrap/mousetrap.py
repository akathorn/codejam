import sys
from typing import Any, Callable, List, TypeVar, Union


T = TypeVar("T")


def solve(K: int, indices: List[int]) -> List[int]:
    indices_left = set(indices)
    result = [0] * len(indices)

    k = K
    i = 0
    for card in range(1, K + 1):
        position = card % k + 1

        if position in indices_left:
            indices_left.remove(position)
            result[position - 1] = card

        i += 1
        k -= 1

    # result = []

    # for index in indices:
    #     k = K  # current deck size
    #     for card in range(1, K + 1):
    #         for count in range(1, K + 1):
    #             if count == card and :

    return result


def build_deck(K) -> List[int]:
    deck = []
    number = K
    while number > 0:
        position = number % (len(deck) + 1) - 1
        if position == -1:
            position = len(deck)
        deck.insert(position, number)
        number -= 1
    return deck


# def top_card(K, S) -> int:
#     if S == 1:
#         return 0
#     else:
#         rec = top_card(K, S-1)


# def solve_rec(K: int, index: int) -> int:
#     if K == 1:
#         return 1
#     else:
#         rec = solve_rec(K - 1, index)
#         position_k =


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(case: int, result: Union[Any, List[Any]]) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    K = readint()
    _, *indices = readmany(int)
    result = solve(K, indices)
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()