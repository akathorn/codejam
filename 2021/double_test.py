import double
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
6
10001 111
1011 111
1010 1011
0 1
0 101
1101011 1101011
""")
out_str = ("""
Case #1: 4
Case #2: 3
Case #3: 2
Case #4: 1
Case #5: IMPOSSIBLE
Case #6: 0
""")
# fmt: on


def test_simple():
    assert double.solve("1", "10") == 1


def test_sample():
    assert double.solve("1101011", "1101011") == 0
    assert double.solve("10001", "111") == 4
    # assert double.solve("1011", "111") == 3
    # assert double.solve("0", "1") == 1
    # assert double.solve("0", "101") == None
    # assert double.solve("1010", "1011") == 2


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    double.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)