from typing import List
import rotate
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
4
7 3
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
6 4
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
4 4
R...
BR..
BR..
BR..
3 3
B..
RB.
RB.
""")
out_str = ("""
Case #1: Neither
Case #2: Both
Case #3: Red
Case #4: Blue
""")
# fmt: on


def make_board(board: str) -> List[List[str]]:
    result: List[List[str]] = []
    for line in board[1:].splitlines():
        result.append([c for c in line])
    return result


def test_horizontal():
    # fmt: off
    board = make_board("""
rrrr
....
....
....
""")
    # fmt: on
    assert rotate.connect_K(4, 4, "r", board)
    assert not rotate.connect_K(4, 4, "b", board)


def test_vertical():
    # fmt: off
    board = make_board("""
......
r..b..
r..b..
r..b..
r.....
r.....
""")
    # fmt: on
    assert rotate.connect_K(5, 6, "r", board)
    assert rotate.connect_K(3, 6, "b", board)


def test_diagonal1():
    # fmt: off
    board = make_board("""
b..
.b.
..b
""")
    # fmt: on
    assert rotate.connect_K(3, 3, "b", board)

    # fmt: off
    board = make_board("""
......
r..b..
.r..b.
..r..b
...r..
......
""")
    # fmt: on
    assert rotate.connect_K(4, 6, "r", board)
    assert rotate.connect_K(3, 6, "b", board)
    assert not rotate.connect_K(4, 6, "b", board)
    assert not rotate.connect_K(5, 6, "r", board)


def test_diagonal2():
    # fmt: off
    board = make_board("""
..b
.b.
b..
""")
    # fmt: on
    assert rotate.connect_K(3, 3, "b", board)
    assert not rotate.connect_K(3, 3, "r", board)

    # fmt: off
    board = make_board("""
......
...r..
..r...
.r....
r...b.
...b..
""")
    # fmt: on
    assert rotate.connect_K(4, 6, "r", board)
    assert rotate.connect_K(2, 6, "b", board)
    assert not rotate.connect_K(4, 6, "b", board)
    assert not rotate.connect_K(5, 6, "r", board)


def test_rotate():
    # fmt: off
    board = make_board("""
..b
.b.
b..
""")
    result = make_board("""
b..
b..
b..
""")
    # fmt: on
    assert rotate.rotate(board) == result
    # fmt: off
    board = make_board("""
r..
r..
b..
""")
    result = make_board("""
r..
r..
b..
""")
    # fmt: on
    assert rotate.rotate(board) == result


def test_rotate2():
    # fmt: off
    board = make_board("""
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
""")
    result = make_board("""
......
......
RR....
RBB...
RRBR..
RBBBB.
""")
    # fmt: on
    assert rotate.rotate(board) == result


def test_rotate3():
    # fmt: off
    board = make_board("""
.......
.......
.......
...R...
...RB..
..BRB..
.RBBR..
""")
    result = make_board("""
.......
.......
.......
R......
BB.....
BRR....
RBBR...
""")
    # fmt: on
    assert rotate.rotate(board) == result


def test_sample():
    # fmt: off
    board = make_board("""
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
""")
    # fmt: on
    rotated = rotate.rotate(board)
    assert not rotate.connect_K(3, 7, "R", rotated)
    assert not rotate.connect_K(3, 7, "B", rotated)

    # fmt: off
    board = make_board("""
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
""")
    # fmt: on
    rotated = rotate.rotate(board)
    assert rotate.connect_K(4, 6, "R", rotated)
    assert rotate.connect_K(4, 6, "B", rotated)


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    rotate.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)