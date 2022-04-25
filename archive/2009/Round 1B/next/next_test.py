import next
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""3
115
1051
6233"""
)
out_str = (
"""Case #1: 151
Case #2: 1105
Case #3: 6323"""
)
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    next.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())


def test_sample():
    assert next.solve("115") == "151"
    assert next.solve("1051") == "1105"
    assert next.solve("6233") == "6323"