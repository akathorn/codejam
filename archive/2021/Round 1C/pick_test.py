import pick
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
4
3 10
1 3 7
4 10
4 1 7 3
4 3
1 2 3 2
4 4
1 2 4 2
""")
out_str = ("""
Case #1: 0.5
Case #2: 0.4
Case #3: 0.0
Case #4: 0.25
""")
# fmt: on


def test_big():
    K = 50
    pick.solve(K, list(range(K)))


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    pick.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)