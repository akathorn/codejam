import saving
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
6
1 CS
2 CS
1 SS
6 SCCSSC
2 CC
3 CSCSS
""")
out_str = ("""
Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 2
Case #5: 0
Case #6: 5
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("saving.Input")
    mock_write = mocker.patch("saving.Output")
    _ = mocker.patch("saving.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    saving.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_a():
    assert saving.solve(1, list("CCCS")) == 3
    assert saving.solve(1, list("CCCSS")) == None
    assert saving.solve(4, list("CCCS")) == 1
    assert saving.solve(4, list("CCCC")) == 0
    assert saving.solve(4, list("SSSS")) == 0
    assert saving.solve(4, list("SSSSS")) == None


def test_b():
    assert saving.solve(8, list("CCSCS")) == 1


def test_profiling():
    ...
