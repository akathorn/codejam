import random

import pytest
import dance
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
4
1 1
15
3 3
1 1 1
1 2 1
1 1 1
1 3
3 1 2
1 3
1 2 3
""")
out_str = ("""
Case #1: 15
Case #2: 16
Case #3: 14
Case #4: 14
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("dance.Input")
    mock_write = mocker.patch("dance.Output")
    _ = mocker.patch("dance.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    dance.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_random():
    N, C = 3, 4
    case = [[random.randint(1, 1000) for _ in range(C)] for _ in range(N)]
    assert dance.solve(case)


def test_random_big():
    N, C = 1000, 1000

    assert dance.solve(case)


def test_random_very_big():
    N, C = 5000, 5000
    case = [[random.randint(1, 1000) for _ in range(C)] for _ in range(N)]
    assert dance.solve(case)