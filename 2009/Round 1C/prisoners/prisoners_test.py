import prisoners
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""2
8 1
3
20 3
3 6 14"""
)
out_str = (
"""Case #1: 7
Case #2: 35"""
)
# fmt: on


def test_solve():
    assert prisoners.solve(8, [3]) == 7
    assert prisoners.solve(1, [1]) == 0
    assert prisoners.solve(10, [1, 2, 3]) == 10
    assert prisoners.solve(5, [1, 2, 4]) == 6
    assert prisoners.solve(10, [7, 8, 9]) == 12
    assert prisoners.solve(3, [1, 2, 3]) == 3


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    prisoners.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())