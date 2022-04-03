import roaring
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
4
2020
2021
68000
101
""")
out_str = ("""
Case #1: 2021
Case #2: 2122
Case #3: 78910
Case #4: 123
""")
# fmt: on


def test_2():
    assert roaring.solve("1") == "2"
    assert roaring.solve("9") == "10"
    assert roaring.solve("10") == "11"


def test_sample():
    assert roaring.solve("2020") == "2021"
    assert roaring.solve("2021") == "2122"
    assert roaring.solve("68000") == "78910"
    assert roaring.solve("101") == "123"


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    roaring.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)