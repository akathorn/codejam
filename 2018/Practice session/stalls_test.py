import stalls
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
4 2
5 2
6 2
1000 1000
1000 1
""")
out_str = ("""
Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("stalls.Input")
    mock_write = mocker.patch("stalls.Output")
    _ = mocker.patch("stalls.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    stalls.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    assert stalls.solve(4, 2) == (1, 0)


def test_3():
    assert stalls.solve(6, 2) == (1, 1)


def test_a():
    assert stalls.solve(100, 1) == (50, 49)
    assert stalls.solve(11, 2) == (3, 2)
    assert stalls.solve(101, 2) == (25, 25)
    assert stalls.solve(1, 1) == (0, 0)
    assert stalls.solve(100, 100) == (0, 0)
    assert stalls.solve(3, 2) == (1, 0)
    assert stalls.solve(10, 2) == (1, 0)
    assert stalls.solve(10, 3) == (1, 0)


def test_b():
    s, p = 100, 3
    assert stalls.solve(s, p) == stalls.solve1(s, p)
    s, p = 100, 100
    assert stalls.solve(s, p) == stalls.solve1(s, p)
    s, p = 452, 5
    assert stalls.solve(s, p) == stalls.solve1(s, p)


def test_profiling():
    ...