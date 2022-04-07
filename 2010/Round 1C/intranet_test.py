import intranet
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
2
3
1 10
5 5
7 7
2
1 1
2 2
""")
out_str = ("""
Case #1: 2
Case #2: 0
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("intranet.Input")
    mock_write = mocker.patch("intranet.Output")
    _ = mocker.patch("intranet.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    intranet.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)