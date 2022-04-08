import nesting
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
0000
101
111000
1
""")
out_str = ("""
Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("nesting.Input")
    mock_write = mocker.patch("nesting.Output")
    _ = mocker.patch("nesting.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    nesting.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    assert nesting.solve([5, 1, 6, 8]) == "(((((5))))1(((((6((8))))))))"