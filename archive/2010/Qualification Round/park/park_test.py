import park
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3"""
)
out_str = (
"""Case #1: 21
Case #2: 100
Case #3: 20"""
)
# fmt: on


def test_sample():
    assert park.solve(4, 6, [1, 4, 2, 1]) == 21
    assert park.solve(100, 10, [1]) == 100
    assert park.solve(5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3]) == 20


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    park.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())