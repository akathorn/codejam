import snapper
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""4
1 0
1 1
4 0
4 47"""
)
out_str = (
"""Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON"""
)
# fmt: on


def test_sample():
    assert snapper.solve(1, 0) == False
    assert snapper.solve(1, 1) == True
    assert snapper.solve(4, 0) == False
    assert snapper.solve(4, 47) == True


def test_big():
    snapper.solve(30, 1000)


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    snapper.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())