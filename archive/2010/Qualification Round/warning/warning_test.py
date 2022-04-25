import warning
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""3
3 26000000 11000000 6000000
3 1 10 11
2 800000000000000000001 900000000000000000001"""
)
out_str = (
"""Case #1: 4000000
Case #2: 0
Case #3: 99999999999999999999"""
)
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    warning.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())