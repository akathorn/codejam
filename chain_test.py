import random
import chain
from chain import Module, Model
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
3
4
60 20 40 50
0 1 1 2
5
3 2 1 4 5
0 1 1 1 0
8
100 100 100 90 80 100 90 100
0 1 2 1 2 3 1 3
""")
out_str = ("""
Case #1: 110
Case #2: 14
Case #3: 490
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    chain.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test1():
    model = Model(
        [
            Module(id=0, fun=0, parents=[1]),
            Module(id=1, fun=60, parents=[2, 3]),
            Module(id=2, fun=20, parents=[4]),
            Module(id=3, fun=40, parents=[]),
            Module(id=4, fun=50, parents=[]),
        ]
    )

    assert model.solve() == 110


def test2():
    model = Model(
        [
            Module(id=0, fun=0, parents=[1, 5]),
            Module(id=1, fun=3, parents=[2, 3, 4]),
            Module(id=2, fun=2, parents=[]),
            Module(id=3, fun=1, parents=[]),
            Module(id=4, fun=4, parents=[]),
            Module(id=5, fun=5, parents=[]),
        ]
    )

    assert model.solve() == 14


def test_random():
    N = 1000
    T = 100

    for _ in range(T):
        funs = [random.randint(1, int(1e9) + 1) for _ in range(N)]
        pointers = [random.randint(0, m - 1) for m in range(1, N + 1)]

        model = chain.create_model(funs, pointers)
        assert model.solve()


def test_random_big():
    N = 10000
    T = 10

    for _ in range(T):
        funs = [random.randint(1, int(1e9) + 1) for _ in range(N)]
        pointers = [random.randint(0, m - 1) for m in range(1, N + 1)]

        model = chain.create_model(funs, pointers)
        assert model.solve()


def test_disjoint():
    funs = [1, 2, 3, 4, 5, 6]
    pointers = [0, 1, 1, 0, 4, 4]

    model = chain.create_model(funs, pointers)
    assert model.solve()


def test_chained():
    funs = [1, 2, 3, 4, 5, 6]
    pointers = [0, 1, 2, 3, 4, 5]

    model = chain.create_model(funs, pointers)
    assert model.solve()


def test_chained_long():
    N = 1000
    funs = [10] * N
    pointers = list(range(N))

    model = chain.create_model(funs, pointers)
    assert model.solve() == 10


def test_blah():
    funs = [0, 2, 3, 4, 5, 6]
    pointers = [0, 0, 2, 2, 2, 2]

    model = chain.create_model(funs, pointers)
    assert model.solve()


def test_one():
    funs = [10]
    pointers = [0]

    model = chain.create_model(funs, pointers)
    assert model.solve() == 10


def test_no_fun():
    funs = [1, 1, 1, 1, 1, 1]
    pointers = [0, 0, 2, 2, 2, 2]

    model = chain.create_model(funs, pointers)
    assert model.solve()