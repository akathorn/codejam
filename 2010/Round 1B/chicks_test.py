import chicks
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
3
5 3 10 5
0 2 5 6 7
1 1 1 1 4
5 3 10 5
0 2 3 5 7
2 1 1 1 4
5 3 10 5
0 2 3 4 7
2 1 1 1 4
""")
out_str = ("""
Case #1: 0
Case #2: 2
Case #3: IMPOSSIBLE
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("chicks.Input")
    mock_write = mocker.patch("chicks.Output")
    _ = mocker.patch("chicks.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    chicks.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)