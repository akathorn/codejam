import sys
import itertools

# O(M*N)
def is_covered(flavors, costumers):
    covered = []
    for costumer in costumers:
        is_covered = False
        for flavor in costumer:
            if flavor in flavors:
                is_covered = True
                break
        covered.append(is_covered)

    return all(covered)


# Returns malted flavors that are wanted by at least an uncovered costumer
# O(M*N)
def missing_malted(flavors, costumers):
    missing_malted = set()
    for costumer in costumers:
        wants_malted = []
        is_covered = False
        for flavor in costumer:
            if flavor in flavors:
                is_covered = True
                break
            elif flavor[1]:
                wants_malted.append(flavor)
        if not is_covered:
            missing_malted.update(wants_malted)

    return missing_malted


def solve(N, costumers, unmalted_flavors, malted_flavors):
    selected = unmalted_flavors

    n_malted = -1
    solved = False

    # O(N) * O(N^3 * M) = O(N^4 * M) ~= O(N^5)
    while not solved and n_malted <= len(malted_flavors):
        n_malted += 1

        ## Choose which icecreams to malt
        # Malted icecreams that are not selected and that some costumer wants
        options = missing_malted(selected, costumers)
        # O(N*N) * O(N*M) = O(N^3 * M)
        for make_malted in itertools.combinations(options, n_malted):
            restore = []
            delete = []
            # Malt the icecreams
            # O(N)
            for malted in make_malted:
                unmalted = (malted[0], False)
                if unmalted in selected:
                    selected.remove(unmalted)
                    restore.append(unmalted)
                selected.add(malted)
                delete.append(malted)

            # O(N*M)
            if is_covered(selected, costumers):
                solved = True
                break

            # Restore to previous state
            for flavor in restore:
                selected.add(flavor)
            for flavor in delete:
                selected.remove(flavor)

    if n_malted > N:
        return None

    # O(N)
    result = []
    for f in range(1, N + 1):
        result.append(1 if ((f, True) in selected) else 0)

    return result


def main():
    C = int(sys.stdin.readline())
    for case in range(1, C + 1):
        N = int(sys.stdin.readline())  # number of flavors, we don't care

        unmalted_set = set()
        malted_set = set()

        # Costumers
        costumers = []
        for _ in range(int(sys.stdin.readline())):
            milkshakes = set()
            costumers.append(milkshakes)
            costumer_flavours = [int(s) for s in sys.stdin.readline().split()]

            # first number is the number of flavours
            n_milkshakes = costumer_flavours[0]

            # Milkshake flavor
            for i in range(1, n_milkshakes * 2, 2):
                flavor_n, malted = costumer_flavours[i], costumer_flavours[i + 1]
                flavor = (flavor_n, bool(malted))
                milkshakes.add(flavor)

                if malted:
                    malted_set.add(flavor)
                else:
                    unmalted_set.add(flavor)

        solution = solve(N, costumers, unmalted_set, malted_set)
        if solution is not None:
            result = " ".join(map(str, solution))
        else:
            result = "IMPOSSIBLE"
        print(f"Case #{case}: {result}")
    sys.stdout.close()


if __name__ == "__main__":
    main()