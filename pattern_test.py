import pattern
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
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ
""")
out_str = ("""
Case #1: COCONUTS
Case #2: *
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("pattern.Input")
    mock_write = mocker.patch("pattern.Output")
    _ = mocker.patch("pattern.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    pattern.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_a():
    # fmt: off
    case = ["*abc",
            "*abc",
            "*bc",
            "*c",
            "*fabc"]
    # fmt: on
    assert pattern.solve(case) == "fabc"


def test_b():
    # fmt: off
    case1 = [
        "*abc",
        "*bc",
        "*c",
        "a*c",
        "ab*",
        "a*",
    ]
    # fmt: on
    assert pattern.solve(case1) == "abc"

    # fmt: off
    case2 = [
        "*abc",
        "abf*",
        "*bc",
        "*bc",
    ]
    # fmt: on
    assert pattern.solve(case2) == "abfabc"


def test_c():
    # fmt: off
    case1 = ["*abcd",
            "ab*cd"]
    # fmt: on
    assert pattern.solve(case1) == "ababcd"


def test_d():
    # fmt: off
    case = [
        "*abc",
        "*bc",
        "*c",
        "a*c",
        "ab*",
        "a*",
        "*b*",
        "*b*",
    ]
    # fmt: on
    assert pattern.solve(case) == "ababc"