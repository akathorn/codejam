import fan
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
5
4 4 SSSS
3 0 SNSS
2 10 NSNNSN
0 1 S
2 7 SSSSSSSS
""")
out_str = ("""
Case #1: 4
Case #2: IMPOSSIBLE
Case #3: IMPOSSIBLE
Case #4: 1
Case #5: 5
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("fan.Input")
    mock_write = mocker.patch("fan.Output")
    _ = mocker.patch("fan.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    fan.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    assert fan.solve(4, 4, "SSSS") == 4


def test_2():
    assert not fan.solve(3, 0, "SNSS")


def test_3():
    assert not fan.solve(2, 10, "NSNNSN")


def test_4():
    assert fan.solve(0, 1, "S") == 1


def test_profiling():
    ...
