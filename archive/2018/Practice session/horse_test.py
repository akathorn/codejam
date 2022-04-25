import horse
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
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
""")
out_str = ("""
Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("horse.Input")
    mock_write = mocker.patch("horse.Output")
    _ = mocker.patch("horse.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    horse.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_profiling():
    ...