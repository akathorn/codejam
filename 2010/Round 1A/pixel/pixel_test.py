import pixel
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
2
6 6 2 3
1 7 5
100 1 5 3
1 50 7
""")
out_str = ("""
Case #1: 4
Case #2: 17
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    pixel.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)