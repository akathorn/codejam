import load
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
4
50 700 2
19 57 3
1 1000 2
24 97 2
""")
out_str = ("""
Case #1: 2
Case #2: 0
Case #3: 4
Case #4: 2
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("load.Input")
    mock_write = mocker.patch("load.Output")
    _ = mocker.patch("load.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    load.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)