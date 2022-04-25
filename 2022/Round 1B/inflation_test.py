import inflation
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
2
3 3
30 10 40
20 50 60
60 60 50
5 2
1 1000000000
500000000 1000000000
1 1000000000
500000000 1
1 1000000000
""")
out_str = ("""
Case #1: 110
Case #2: 4999999996
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("inflation.Input")
    mock_write = mocker.patch("inflation.Output")
    _ = mocker.patch("inflation.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    inflation.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_random():
    N = 10
    P = 3
    case = [[random.randint(1, 10 ** 9) for _ in range(P)] for _ in range(N)]

    inflation.solve(case)


def test_profiling():
    N = 100
    P = 5
    case = [[random.randint(1, 10 ** 9) for _ in range(P)] for _ in range(N)]

    inflation.solve(case)
