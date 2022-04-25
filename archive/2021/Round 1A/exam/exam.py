from fractions import Fraction
import sys
from typing import List, Tuple


Exam = Tuple[List[bool], int]


def solve(exams: List[Exam]) -> Tuple[List[bool], Fraction]:
    Q = len(exams[0][0])
    return [False] * Q, Fraction(1, 2)


def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        N, _ = [int(s) for s in sys.stdin.readline().split()]
        exams: List[Exam] = []
        for _ in range(N):
            A, S = sys.stdin.readline().split()
            answers = [a == "T" for a in A]
            score = int(S)
            exams.append((answers, score))
        answers, fraction = solve(exams)
        result = "".join("T" if a else "F" for a in answers)
        print(f"Case #{case}: {result} {fraction.numerator}/{fraction.denominator}")
    sys.stdout.close()


if __name__ == "__main__":
    main()