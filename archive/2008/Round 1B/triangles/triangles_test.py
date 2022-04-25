import random
from triangles import solve_bruteforce, solve_math, generate_trees


def test_sample1():
    assert solve_math(generate_trees(4, 10, 7, 1, 2, 0, 1, 20)) == 1
    assert solve_math(generate_trees(6, 2, 0, 2, 1, 1, 2, 11)) == 2


def test_random():
    random.seed(42)

    params = [random.randint(1, 20) for _ in range(8)]
    trees = generate_trees(*params)
    assert solve_math(trees) == solve_bruteforce(trees)

    params = [random.randint(1, 100) for _ in range(8)]
    trees = generate_trees(*params)
    assert solve_math(trees) == solve_bruteforce(trees)

    random.seed(4242)
    for i in range(10):
        # print(i)
        params = [random.randint(0, 1e9) for _ in range(8)]
        params[0] = random.randint(100, 200)
        params[-1] = random.randint(1, 1e9)
        trees = generate_trees(*params)
        assert solve_math(trees) == solve_bruteforce(trees)