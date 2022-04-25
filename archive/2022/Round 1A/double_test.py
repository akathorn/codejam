import double
import random
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
# in_str = ("""
# 3
# 3 2
# 1 2
# 4 2
# """)
# out_str = ("""
# Case #1: 0
# Case #2: 0
# Case #3: 0
# """)
in_str = ("""
3
PEEL
AAAAAAAAAA
CODEJAMDAY
""")
out_str = ("""
Case #1: PEEEEL
Case #2: AAAAAAAAAA
Case #3: CCODDEEJAAMDAAY
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("double.Input")
    mock_write = mocker.patch("double.Output")
    _ = mocker.patch("double.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    double.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_3():
    assert double.solve("CODEJAMDAY") == "CCODDEEJAAMDAAY"


def test_profiling():
    ...
