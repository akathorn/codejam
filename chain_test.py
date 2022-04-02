import chain
from chain import Module, Model
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
    model = Model(
        [
            Module(id=0, fun=0, parents=[1, 5], children=[]),
            Module(id=1, fun=3, parents=[2, 3, 4], children=[0]),
            Module(id=2, fun=2, parents=[], children=[1]),
            Module(id=3, fun=1, parents=[], children=[1]),
            Module(id=4, fun=4, parents=[], children=[1]),
            Module(id=5, fun=5, parents=[], children=[0]),
        ]
    )

    assert model.solve() == 14