import dice
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
4
4
6 10 12 8
6
5 4 5 4 4 4
10
10 10 7 6 7 4 4 5 7 4
1
10
""")
out_str = ("""
Case #1: 4
Case #2: 5
Case #3: 9
Case #4: 1
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    dice.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    case = sorted([6, 10, 12, 8])
    assert dice.solve(case) == 4


def test_2():
    case = sorted([5, 4, 5, 4, 4, 4])
    assert dice.solve(case) == 5


def test_3():
    case = sorted([10, 10, 7, 6, 7, 4, 4, 5, 7, 4])
    assert dice.solve(case) == 9