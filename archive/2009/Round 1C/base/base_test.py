import base
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""3
11001001
cats
zig"""
)
out_str = (
"""Case #1: 201
Case #2: 75
Case #3: 11"""
)
# fmt: on


def test_to_minimum():
    assert base.to_minimum("123") == ("102", 3)
    assert base.to_minimum("aba1815") == ("1012324", 5)


def test_to_base_10():
    assert base.to_base_10("123", 10) == 123
    assert base.to_base_10("100", 2) == 4
    assert base.to_base_10("f", 16) == 15


def test_solve():
    assert base.solve("012") == 11
    assert base.solve("1023456789abcdefghijklmnopqrstuvwxyz")


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    base.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())