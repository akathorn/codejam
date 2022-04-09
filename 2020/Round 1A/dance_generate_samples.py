import random


def generate(N, C):
    with open(f"dance_{N}x{C}.sample", "w") as f:
        f.write(f"1\n{N} {C}\n")
        for _ in range(N):
            for _ in range(C):
                f.write(str(random.randint(1, 1000)) + " ")
            f.write("\n")


if __name__ == "__main__":
    N, C = 500, 500
    generate(N, C)
