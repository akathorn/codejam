import parenting
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
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440
""")
out_str = ("""
Case #1: CJC
Case #2: IMPOSSIBLE
Case #3: JCCJJ
Case #4: CC
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("parenting.Input")
    mock_write = mocker.patch("parenting.Output")
    _ = mocker.patch("parenting.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    parenting.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    case = [[99, 150], [1, 100], [100, 301], [2, 5], [150, 250]]
    assert parenting.solve(case) == "CJJCC"  # or parenting.solve(case) == "CJJCC"
