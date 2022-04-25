import expogo
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
2 3
-2 -3
3 0
-1 1
""")
out_str = ("""
Case #1: SEN
Case #2: NWS
Case #3: EE
Case #4: IMPOSSIBLE
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("expogo.Input")
    mock_write = mocker.patch("expogo.Output")
    _ = mocker.patch("expogo.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    expogo.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_a():
    assert expogo.solve(2, 3) == "SEN"


def test_b():
    assert expogo.solve(-2, -3) == "NWS"


def test_c():
    assert expogo.solve(3, 0) == "EE"


def test_d():
    assert expogo.solve(-1, 1) == None


def test_profiling():
    ...
