import sys
from typing import List


def ndigits(number: int) -> int:
    return len(str(number))


def diff(x: int, y: int) -> int:
    return ndigits(x) - ndigits(y)


def solve(numbers: List[int]) -> int:
    operations = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            continue

        d = diff(numbers[i - 1], numbers[i])
        if d == 0:
            numbers[i] *= 10
            operations += 1
            continue

        # last_x = numbers[i] % 10
        # last_y = (numbers[i - 1] % (10 ** (d + 1))) // (10 ** (d))

        last_x = numbers[i]
        last_y = (numbers[i - 1] // (10 ** d)) % (10 ** ndigits(numbers[i]))

        if last_x > last_y:
            numbers[i] *= 10 ** d
            operations += d
        elif last_x < last_y:
            numbers[i] *= 10 ** (d + 1)
            operations += d + 1
        # elif last_x == 0 and last_y == 0:
        #     numbers[i] *= 10 ** (d + 1)
        #     operations += d + 1
        else:
            diff_digits = numbers[i - 1] % (10 ** d)
            new_digits = diff_digits + 1
            if new_digits == 10 ** d:  # It was all 9's
                numbers[i] *= 10 ** (d + 1)
                operations += d + 1
                continue
            else:
                numbers[i] *= 10 ** d
                numbers[i] += new_digits
                operations += d
                continue

    return operations


def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        _ = sys.stdin.readline().split()
        numbers = [int(s) for s in sys.stdin.readline().split()]
        print(f"Case #{case}: {solve(numbers)}")
    sys.stdout.close()


if __name__ == "__main__":
    main()