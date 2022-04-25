import random
import senate
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
2 2
3
3 2 2
3
1 1 2
3
2 3 1
""")
out_str = ("""
Case #1: AB BA
Case #2: AA BC C BA
Case #3: C C AB
Case #4: BA BB CA
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("senate.Input")
    mock_write = mocker.patch("senate.Output")
    _ = mocker.patch("senate.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    senate.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_random():
    random.seed(1)

    for _ in range(100):
        N = 25
        P = [random.randint(1, 1000) for _ in range(N)]

        assert senate.solve(P)


def test_profiling():
    ...