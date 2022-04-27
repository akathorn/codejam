import trouble
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
5
5 6 8 4 3
3
8 9 7
""")
out_str = ("""
Case #1: OK
Case #2: 1
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("trouble.Input")
    mock_write = mocker.patch("trouble.Output")
    _ = mocker.patch("trouble.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    trouble.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_profiling():
    N = 10 ** 5
    L = [random.randint(0, 10 ** 9) for _ in range(N)]
    trouble.solve(L)
