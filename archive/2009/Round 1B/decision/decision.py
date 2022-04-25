import sys
from typing import Any, Callable, List, NamedTuple, Optional, Tuple, TypeVar, Union


T = TypeVar("T")

Animal = NamedTuple("Animal", [("name", str), ("features", List[str])])
# Decision = NamedTuple(
#     "Children", [("feature", str), ("true", "Tree"), ("false", "Tree")]
# )
# Tree = NamedTuple("Tree", [("weight", float), ("decision", Optional[Decision])])

# ParsedTree = NamedTuple("ParsedTree", [("children", List[Union["str", "ParsedTree"]])])

Tree = List[Union[str, "Tree"]]


def get_token(string: str) -> Tuple[str, str]:
    if len(string) < 1:
        return "", ""

    token, *rest = string.split()

    if len(token) > 1 and token[0] == "(":
        rest.insert(0, token[1:])
        token = "("
    if len(token) > 1 and token[-1] == ")":
        rest.insert(0, ")")
        token = token[:-1]

    return token, " ".join([s for s in rest if s])


def get_tokens(string: str) -> List[str]:
    tokens: List[str] = []
    rest = string
    while rest:
        token, rest = get_token(rest)
        tokens.append(token)
    return tokens


def parse_tree(tree_str: str) -> Tree:
    tokens = get_tokens(tree_str)
    tree: Tree = []
    stack: List[Tree] = []
    while tokens:
        token = tokens.pop(0)
        if token == "(":
            new_tree: Tree = []
            tree.append(new_tree)
            stack.append(tree)
            tree = new_tree
        elif token == ")":
            tree = stack.pop()
        else:
            tree.append(token)

    return tree[0]


def solve(tree_str: str, animals: List[Animal]) -> List[float]:
    tree = parse_tree(tree_str)
    return [decision(animal, tree) for animal in animals]


def decision(animal: Animal, tree: Tree) -> float:
    if len(tree) == 1:
        # Leaf
        return float(tree[0])  # type: ignore
    else:
        weight, feature, true_branch, false_branch = tree
        if feature in animal.features:
            return float(weight) * decision(animal, true_branch)  # type: ignore
        else:
            return float(weight) * decision(animal, false_branch)  # type: ignore


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def read2D(rows: int, typ: Callable[[str], T]) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def solve_case(case: int):
    # Read data
    L = readint()
    tree = ""
    for _ in range(L):
        tree = tree + readstring() + "\n"

    A = readint()
    animals: List[Animal] = []
    for _ in range(A):
        name, _, *features = readmany(str)
        animals.append(Animal(name, features))

    # Solve
    result = solve(tree, animals)

    # Write solution
    out_string = ""
    for prob in result:
        out_string += "\n"
        out_string += str(prob)

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()