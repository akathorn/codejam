import mkdir
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = ("""
3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b
""")
out_str = ("""
Case #1: 4
Case #2: 0
Case #3: 4
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("mkdir.Input")
    mock_write = mocker.patch("mkdir.Output")
    _ = mocker.patch("mkdir.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    mkdir.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_1():
    existing = [
        l.split("/")
        for l in [
            "/a/b/c",
            "/a/d/e",
            "/f/g",
            "/h/i",
        ]
    ]

    create = [
        l.split("/")
        for l in [
            "/j/k/l",
            "/a/b/c/m/n",
            "/f/g",
            "/h/i",
        ]
    ]

    assert mkdir.solve(existing, create) == 5


def test_2():
    existing = [
        l.split("/")
        for l in [
            "/a/b/c",
            "/d/b",
        ]
    ]

    create = [
        l.split("/")
        for l in [
            "/d/b/c",
        ]
    ]

    assert mkdir.solve(existing, create) == 1


# def test_random(mocker: MockerFixture):
#     paths = [chr(i) for i in range(1, 100)]
#     existing = []
#     for _ in range(100):
