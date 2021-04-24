import sys


def solve(f, R, t, r, g) -> float:
    inner_radius = R - t
    outer_radius = R
    size = int(1e2)

    on_racket = 0
    off_racket = 0
    for x in range(-size, size + 1):
        for y in range(-size, size + 1):
            # Border
            if (x ** 2 + y ** 2) > outer_radius:
                continue
            if (x ** 2 + y ** 2) + f > inner_radius:
                on_racket += 1
                continue

            # Strings
            string = 0
            on_string = False
            while not on_string and string < inner_radius:
                if (string - r) < abs(x) < (string + r):
                    on_string = True
                elif (string - r + f) < abs(y) < (string + r - f):
                    on_string = True
                string += 2 * r + g

            if on_string:
                on_racket += 1
            else:
                off_racket += 1

    print(on_racket)
    print(off_racket)
    prob = on_racket / (on_racket + off_racket)
    return round(prob, 6)


def main():
    N = int(sys.stdin.readline())
    for case in range(1, N + 1):
        f, R, t, r, g = [float(x) for x in sys.stdin.readline().split()]

        print(f"Case #{case}: {solve(f, R, t, r, g)}")
    sys.stdout.close()


if __name__ == "__main__":
    main()