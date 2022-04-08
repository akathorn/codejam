import vestigium
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
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3
""")
out_str = ("""
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("vestigium.Input")
    mock_write = mocker.patch("vestigium.Output")
    _ = mocker.patch("vestigium.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    vestigium.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)