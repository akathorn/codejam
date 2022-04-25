import sys
from math import inf
from typing import Any, Callable, List, NamedTuple, Optional, Tuple, TypeVar, Union


T = TypeVar("T")


Gate = NamedTuple("Gate", [("gate", str), ("changeable", bool)])

Node = NamedTuple(
    "Node",
    [
        ("gate", Optional[Gate]),
        ("value", Optional[bool]),
        ("left", Optional["Node"]),
        ("right", Optional["Node"]),
    ],
)


def solve(
    V: int, interior_nodes: List[Tuple[int, int]], leaf_nodes: List[int]
) -> Optional[int]:
    nodes = interior_nodes + leaf_nodes  # type: ignore
    tree = build_tree(nodes, 1)

    sol = solve_rec(tree)
    res = sol[0] if V == 1 else sol[1]

    if res == inf:
        return None
    else:
        return int(res)


# Returns tuple: (n changes to make it true, n changes to make it false)
def solve_rec(node: Node) -> Tuple[float, float]:
    def combine_AND(left, right) -> Tuple[float, float]:
        # to true
        changes_to_true = left[0] + right[0]
        # to false
        changes_to_false = min(left[1], right[1])

        return (changes_to_true, changes_to_false)

    def combine_OR(left, right) -> Tuple[float, float]:
        # to true
        changes_to_true = min(left[0], right[0])
        # to false
        changes_to_false = left[1] + right[1]

        return (changes_to_true, changes_to_false)

    if node.value is not None:
        if node.value == True:
            return (0, inf)
        else:
            return (inf, 0)

    assert node.left and node.right
    left = solve_rec(node.left)
    right = solve_rec(node.right)

    if not node.gate.changeable:
        if node.gate.gate == "AND":
            return combine_AND(left, right)
        else:
            return combine_OR(left, right)

    # Changeable
    and_gate = combine_AND(left, right)
    or_gate = combine_OR(left, right)

    ### To make a 1
    if and_gate[0] < or_gate[0]:
        best_for_one = "AND"
    elif and_gate[0] > or_gate[0]:
        best_for_one = "OR"
    else:
        best_for_one = node.gate.gate

    # Best one to make a one is an AND
    if best_for_one == "AND":
        if node.gate.gate == "AND":
            changes_to_one = and_gate[0]
        else:
            changes_to_one = and_gate[0] + 1
    # Best one to make a one is an OR
    else:
        if node.gate.gate == "OR":
            changes_to_one = or_gate[0]
        else:
            changes_to_one = or_gate[0] + 1

    ### To make a zero
    if and_gate[1] < or_gate[1]:
        best_for_zero = "AND"
    elif and_gate[1] > or_gate[1]:
        best_for_zero = "OR"
    else:
        best_for_zero = node.gate.gate

    # No way to get there
    # Best one to make a zero is an AND
    if best_for_zero == "AND":
        if node.gate.gate == "AND":
            changes_to_zero = and_gate[1]
        else:
            changes_to_zero = and_gate[1] + 1
    # Best one to make a zero is an OR
    else:
        if node.gate.gate == "OR":
            changes_to_zero = or_gate[1]
        else:
            changes_to_zero = or_gate[1] + 1

    return (changes_to_one, changes_to_zero)


def build_tree(nodes, x):
    if isinstance(nodes[x - 1], int):
        return Node(None, nodes[x - 1], None, None)

    if x * 2 <= len(nodes):
        left = build_tree(nodes, x * 2)
    else:
        left = None

    if x * 2 + 1 <= len(nodes):
        right = build_tree(nodes, x * 2 + 1)
    else:
        right = None

    gate = Gate("AND" if nodes[x - 1][0] == 1 else "OR", nodes[x - 1][1])
    return Node(gate, None, left, right)


def readint() -> int:
    return int(sys.stdin.readline())


def readfloat() -> float:
    return float(sys.stdin.readline())


def readstring() -> str:
    return sys.stdin.readline().strip()


def readmany(typ: Callable[[str], T]) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    print(f"Case #%d: %s" % (case, out_string))


def solve_case(case: int):
    M, V = readmany(int)

    interior_nodes = []
    for _ in range((M - 1) // 2):
        G, C = readmany(int)
        interior_nodes.append((True if G == 1 else False, True if C == 1 else False))

    leaf_nodes = []
    for _ in range((M + 1) // 2):
        leaf_nodes.append(readint())

    result = solve(V, interior_nodes, leaf_nodes)
    writesolution(case, result)


def main():
    T = readint()
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()