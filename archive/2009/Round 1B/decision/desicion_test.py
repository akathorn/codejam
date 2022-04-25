import decision
from pytest_mock import mocker, MockerFixture  # type: ignore

# fmt: off
in_str = (
"""2
3
(0.5 cool
  ( 1.000)
  (0.5 ))
2
anteater 1 cool
cockroach 0
13
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
1
beaver 2 furry freshwater"""
)
out_str = (
"""Case #1:
0.5000000
0.2500000
Case #2:
0.162"""
)
# fmt: on


def test_get_token():
    assert decision.get_token("hello bye") == ("hello", "bye")
    assert decision.get_token("hello") == ("hello", "")
    assert decision.get_token("hello bye bye") == ("hello", "bye bye")
    assert decision.get_token("hello\nbye bye") == ("hello", "bye bye")
    assert decision.get_token(" hello\nbye bye") == ("hello", "bye bye")
    assert decision.get_token("( hola") == ("(", "hola")
    assert decision.get_token("(hola") == ("(", "hola")
    assert decision.get_token("hola)") == ("hola", ")")
    assert decision.get_token("") == ("", "")


def test_get_tokens():
    assert decision.get_tokens("(hola) 0.3 ( ) \n 3") == [
        "(",
        "hola",
        ")",
        "0.3",
        "(",
        ")",
        "3",
    ]


def test_parse():
    decision.parse_tree(
        """(0.5 cool
( 1.000)
(0.5 ))"""
    )


def test_sample1():
    tree = """(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)"""
    animals = [decision.Animal("beaver", ["furry", "freshwater"])]
    assert decision.solve(tree, animals) == [0.0324]


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("sys.stdin.readline")
    mock_write = mocker.patch("sys.stdout.write")
    mock_read.side_effect = in_str.splitlines()

    decision.main()

    for call, out in zip(mock_write.mock_calls, out_str.splitlines()):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_str.splitlines())