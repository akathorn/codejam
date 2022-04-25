import broken
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""3
0 0 0
0 21600000000000 23400000000000
1476000000000 2160000000000 3723000000000"""
)
out_str = (
"""Case #1: 0 0 0 0
Case #2: 6 30 0 0
Case #3: 1 2 3 0"""
)
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    broken.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == out_str.splitlines()


def test_sample():
    assert broken.solve(0, 0, 0) == [0, 0, 0, 0]
    assert broken.solve(0, 21600000000000, 23400000000000) == [6, 30, 0, 0]
    assert broken.solve(1476000000000, 2160000000000, 3723000000000) == [1, 2, 3, 0]