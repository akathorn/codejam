import rank
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
2
5
6
""")
out_str = ("""
Case #1: 5
Case #2: 8
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("rank.Input")
    mock_write = mocker.patch("rank.Output")
    _ = mocker.patch("rank.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    rank.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_2():
    assert rank.solve(6) == 8