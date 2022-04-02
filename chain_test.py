import chain
from chain import Module
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
3
4
60 20 40 50
0 1 1 2
5
3 2 1 4 5
0 1 1 1 0
8
100 100 100 90 80 100 90 100
0 1 2 1 2 3 1 3
""")
out_str = ("""
Case #1: 110
Case #2: 14
Case #3: 490
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()[1:]

    chain.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test2():
    model = [
        Module(id=0, fun=0, pointers=[1, 5]),
        Module(id=1, fun=3, pointers=[2, 3, 4]),
        Module(id=2, fun=2, pointers=[]),
        Module(id=3, fun=1, pointers=[]),
        Module(id=4, fun=4, pointers=[]),
        Module(id=5, fun=5, pointers=[]),
    ]

    assert chain.solve(model) == 14