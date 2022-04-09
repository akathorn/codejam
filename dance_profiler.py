import cProfile
import dance
import dance_generate_samples
import os

N, C = 1000, 1000
path: str = f"dance_{N}x{C}.sample"
force = False


def main():
    global N, C, path, force
    if not os.path.exists(path) or force:
        print("Generating file")
        dance_generate_samples.generate(N, C)

    print("Reading file")
    case = []
    with open(path, "r") as f:
        f.readline()
        N, _ = f.readline().split()
        for _ in range(int(N)):
            case.append([int(s) for s in f.readline().split()])

    print("Solving")
    cProfile.runctx("dance.solve(case)", globals=globals(), locals={"case": case})


if __name__ == "__main__":
    main()