import fight
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
4 0
1 1 1 8
8 8 8 8
3 0
0 1 1
1 1 0
1 0
3
3
5 0
0 8 0 8 0
4 0 4 0 4
3 0
1 0 0
0 1 2
5 2
1 2 3 4 5
5 5 5 5 10
""")
out_str = ("""
Case #1: 4
Case #2: 4
Case #3: 1
Case #4: 0
Case #5: 1
Case #6: 7
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("fight.Input")
    mock_write = mocker.patch("fight.Output")
    _ = mocker.patch("fight.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    fight.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_profiling():
    N = 1000
    K = random.randint(0, 100000)
    C = [random.randint(0, 100000) for _ in range(N)]
    D = [random.randint(0, 100000) for _ in range(N)]
    fight.solve(C, D, K)