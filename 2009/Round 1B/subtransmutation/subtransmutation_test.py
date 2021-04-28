import subtransmutation
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""3
2 1 2
1 2
5 1 2
2 0 0 0 1
3 1 2
1 1 1"""
)
out_str = (
"""Case #1: 4
Case #2: 6
Case #3: 5"""
)
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    subtransmutation.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())


def test_sample():
    assert subtransmutation.solve(1, 2, [1, 2]) == 4
    assert subtransmutation.solve(1, 2, [2, 0, 0, 0, 1]) == 6
    assert subtransmutation.solve(1, 2, [1, 1, 1]) == 5