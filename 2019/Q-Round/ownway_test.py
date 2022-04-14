import random
from typing import Dict, Tuple
import ownway
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
2
2
SE
5
EESSSESE
""")
out_str = ("""
Case #1: ES
Case #2: SEEESSES
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("ownway.Input")
    mock_write = mocker.patch("ownway.Output")
    _ = mocker.patch("ownway.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    ownway.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_random():
    direction: Dict[str, Tuple[int, int]] = {"S": (0, 1), "E": (1, 0)}
    N = 10
    for _ in range(10):
        lydia = ["S"] * N + ["E"] * N
        random.shuffle(lydia)
        lydia = "".join(lydia)
        own = ownway.solve(lydia, N)
        lydia_path = set()
        pos = (0, 0)
        for s in lydia[1:]:
            new_pos = pos[0] + direction[s][0], pos[1] + direction[s][1]
            lydia_path.add((pos, new_pos))
            pos = new_pos

        pos = (0, 0)
        for s in own[1:]:
            new_pos = pos[0] + direction[s][0], pos[1] + direction[s][1]
            assert (pos, new_pos) not in lydia_path
            pos = new_pos
