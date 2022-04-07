import chess
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
15 20
55555
FFAAA
2AAD5
D552A
2AAD5
D542A
4AD4D
B52B2
52AAD
AD552
AA52D
AAAAA
5AA55
A55AA
5AA55
4 4
0
0
0
0
4 4
3
3
C
C
4 4
6
9
9
6
""")
out_str = ("""
Case #1: 5
6 2
4 3
3 7
2 15
1 57
Case #2: 1
1 16
Case #3: 2
2 1
1 12
Case #4: 1
2 4
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("chess.Input")
    mock_write = mocker.patch("chess.Output")
    _ = mocker.patch("chess.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    chess.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_one():
    # fmt: off
    case = ["0110",
            "1001",
            "1001",
            "0110"]
    # fmt: on
    assert chess.solve(case) == [[2, 4]]