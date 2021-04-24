import sys
import itertools
from typing import Dict, List, NamedTuple, Optional, Set, Tuple

Flavor = NamedTuple("Milkshake", [("flavor", int), ("malted", bool)])


def flavors_set(
    costumers: List[List[Flavor]],
) -> Tuple[Set[Flavor], Set[Flavor], Set[Flavor]]:
    flavors: Set[Flavor] = set()
    for costumer in costumers:
        for milkshake in costumer:
            flavors.add(milkshake)
    unmalted = {flavor for flavor in flavors if not flavor.malted}
    malted = {flavor for flavor in flavors if flavor.malted}
    return flavors, unmalted, malted


def is_covered(flavors: Set[Flavor], costumers: List[List[Flavor]]) -> bool:
    covered: List[bool] = []
    for costumer in costumers:
        is_covered = False
        for flavor in costumer:
            if flavor in flavors:
                is_covered = True
                break
        covered.append(is_covered)

    return all(covered)


def solve(N: int, costumers: List[List[Flavor]]) -> Optional[List[int]]:
    _, selected, malted_flavors = flavors_set(costumers)

    n_malted = 0
    while n_malted <= N:
        restore: List[Flavor] = []
        delete: List[Flavor] = []
        for make_malted in itertools.combinations(malted_flavors, n_malted):
            for malted in make_malted:
                unmalted = Flavor(malted.flavor, False)
                if unmalted in selected:
                    selected.discard(unmalted)
                    restore.append(unmalted)
                selected.add(malted)
                delete.append(malted)

        if is_covered(selected, costumers):
            break

        for flavor in restore:
            selected.add(flavor)
        for flavor in delete:
            selected.remove(flavor)

        n_malted += 1

    if n_malted > N:
        return None

    result: List[int] = []
    for f in range(1, N + 1):
        result.append(1 if (Flavor(f, True) in selected) else 0)

    return result


def main():
    C = int(sys.stdin.readline())
    for case in range(1, C + 1):
        N = int(sys.stdin.readline())  # number of flavors, we don't care

        # Costumers
        costumers: List[List[Flavor]] = []
        for _ in range(int(sys.stdin.readline())):
            milkshakes: List[Flavor] = []
            costumers.append(milkshakes)
            costumer_flavours = [int(s) for s in sys.stdin.readline().split()]

            # first number is the number of flavours
            n_milkshakes = costumer_flavours.pop(0)

            # Milkshake flavor
            for _ in range(n_milkshakes):
                flavor, malted = costumer_flavours.pop(0), costumer_flavours.pop(0)
                milkshakes.append(Flavor(flavor, bool(malted)))

        solution = solve(N, costumers)
        if solution is not None:
            result = " ".join(map(str, solution))
        else:
            result = "IMPOSSIBLE"
        print(f"Case #{case}: {result}")
    sys.stdout.close()


if __name__ == "__main__":
    main()