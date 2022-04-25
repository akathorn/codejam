import deque
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
2
1 5
4
1 4 2 3
5
10 10 10 10 10
4
7 1 3 1000000
""")
out_str = ("""
Case #1: 2
Case #2: 3
Case #3: 5
Case #4: 2
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("deque.Input")
    mock_write = mocker.patch("deque.Output")
    _ = mocker.patch("deque.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    deque.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_4():
    assert deque.solve([7, 1, 3, 1000000]) == 2


def test_profiling():
    N = 100000
    case = [random.randint(1, 10 ** 6) for _ in range(N)]
    deque.solve(case)
