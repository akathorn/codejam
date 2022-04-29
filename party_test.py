import party
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
2 2 2
1 2 3
1 1 2
2 2 2
1 2 3
2 1 2
3 4 5
2 3 3
2 1 5
2 4 2
2 2 4
2 5 1
""")
out_str = ("""
Case #1: 5
Case #2: 4
Case #3: 7
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("party.Input")
    mock_write = mocker.patch("party.Output")
    _ = mocker.patch("party.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    party.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    robots = 2
    bits = 2
    cashiers = [(1, 1, 2), (1, 2, 3)]
    assert party.solve(robots, bits, cashiers) == 5


def test_profiling():
    ...
