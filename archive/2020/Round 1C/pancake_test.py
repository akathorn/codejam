import pancake
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
4
1 3
1
5 2
10 5 359999999999 123456789 10
2 3
8 4
3 2
1 2 3
""")
out_str = ("""
Case #1: 2
Case #2: 0
Case #3: 1
Case #4: 1
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("pancake.Input")
    mock_write = mocker.patch("pancake.Output")
    _ = mocker.patch("pancake.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    pancake.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_profiling():
    ...
