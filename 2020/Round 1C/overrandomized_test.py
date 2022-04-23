import overrandomized
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

out_str = ("""
Case #1: TPFOXLUSHB
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    with open("overrandomized.sample", "r") as f:
        in_str = "\n" + f.read()

    mock_read = mocker.patch("overrandomized.Input")
    mock_write = mocker.patch("overrandomized.Output")
    _ = mocker.patch("overrandomized.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    overrandomized.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_profiling(mocker: MockerFixture):
    mock_read = mocker.patch("overrandomized.Input")
    mock_write = mocker.patch("overrandomized.Output")
    _ = mocker.patch("overrandomized.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    overrandomized.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)
