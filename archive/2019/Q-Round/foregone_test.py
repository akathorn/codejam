import random
import foregone
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
4
940
4444
""")
out_str = ("""
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("foregone.Input")
    mock_write = mocker.patch("foregone.Output")
    _ = mocker.patch("foregone.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    foregone.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_random():
    for _ in range(10):
        a = random.randint(2, 100)
        b = random.randint(2, 100)
        assert sum(foregone.solve(a + b)) == a + b


def test_random_big():
    for _ in range(100):
        N = random.randint(2, 1000000000)
        a = random.randint(2, 1000000000)
        b = N - a
        assert sum(foregone.solve(a + b)) == a + b