import choppers
import random
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
6
3 6 1 1
.@@..@
.....@
@.@.@@
4 3 1 1
@@@
@.@
@.@
@@@
4 5 1 1
.....
.....
.....
.....
4 4 1 1
..@@
..@@
@@..
@@..
3 4 2 2
@.@@
@@.@
@.@@
3 4 1 2
.@.@
@.@.
.@.@
""")
out_str = ("""
Case #1: POSSIBLE
Case #2: IMPOSSIBLE
Case #3: POSSIBLE
Case #4: IMPOSSIBLE
Case #5: POSSIBLE
Case #6: IMPOSSIBLE
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("choppers.Input")
    mock_write = mocker.patch("choppers.Output")
    _ = mocker.patch("choppers.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    choppers.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    waffle = """.@@..@
.....@
@.@.@@""".split()
    assert choppers.solve(waffle, 1, 1)


def test_4():
    waffle = """..@@
..@@
@@..
@@..""".split()
    assert not choppers.solve(waffle, 1, 1)


def test_a():
    waffle = """
@..@
....
....
@..@"""[
        1:
    ].split()
    assert choppers.solve(waffle, 1, 1)


def test_b():
    waffle = """
@..@..@.
@..@..@."""[
        1:
    ].split()
    assert choppers.solve(waffle, 1, 2)


def test_profiling():
    ...
