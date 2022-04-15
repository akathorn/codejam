import pylons
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
2 2
2 5
""")
out_str = ("""
Case #1: IMPOSSIBLE
Case #2: POSSIBLE
2 3
1 1
2 4
1 2
2 5
1 3
2 1
1 5
2 2
1 4
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("pylons.Input")
    mock_write = mocker.patch("pylons.Output")
    _ = mocker.patch("pylons.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    pylons.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)