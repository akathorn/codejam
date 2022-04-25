import random
from typing import List
import pascal
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
# in_str = ("""
# 3
# 3 2
# 1 2
# 4 2
# """)
# out_str = ("""
# Case #1: 0
# Case #2: 0
# Case #3: 0
# """)
in_str = ("""
3
1
4
19
""")
out_str = ("""
Case #1:
1 1
Case #2:
1 1
2 1
2 2
3 3
Case #3:
1 1
2 2
3 2
4 3
5 3
5 2
4 1
3 1
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("pascal.Input")
    mock_write = mocker.patch("pascal.Output")
    _ = mocker.patch("pascal.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    pascal.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def total(path: List[List[int]]):
    return sum(pascal.value(*r) for r in path)


def validate_path(path: List[List[int]]):
    for a, b in zip(path, path[1:]):
        if not (
            (a[1] <= a[0])
            or (b[1] <= b[0])
            or (-1 < a[0] - b[0] < 1)
            or (-1 < a[1] - b[1] < 1)
        ):
            return False

    return True


def test_4():
    assert total(pascal.solve(4)) == 4


def test_19():
    assert total(pascal.solve(19)) == 19


def test_big():
    path = pascal.solve(10000000000)
    assert validate_path(path)
    assert total(path) == 10000000000


def test_random():
    for _ in range(100):
        N = random.randint(10000, 1000000000)
        path = pascal.solve(N)
        assert validate_path(path)
        assert total(path) == N