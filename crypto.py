import sys
from typing import Any, Callable, List, TypeVar, Union, Generator


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

P: List[int] = []
q: int = 2
D = {}


def gen_primes():
    """Generate an infinite sequence of prime numbers."""
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    global P, q, D
    yield from P

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            P.append(q)
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def process_cipher_left(cipher: List[int], p: int) -> List[int]:
    if not cipher:
        return []
    q = int(cipher[-1] / p)
    return process_cipher_left(cipher[:-1], q) + [q]


def process_cipher_right(cipher: List[int], p: int) -> List[int]:
    if not cipher:
        return []
    q = int(cipher[0] / p)
    return [q] + process_cipher_right(cipher[1:], q)


def solve(N: int, cipher: List[int]) -> str:
    found = False
    for p in gen_primes():
        for i, n in enumerate(cipher):
            if n % p == 0:
                q = int(n / p)
                if i == 0:
                    if cipher[1] % p != 0:
                        p, q = q, p
                elif i == len(cipher) - 1:
                    if cipher[-2] % q != 0:
                        p, q = q, p
                elif cipher[i - 1] % q != 0 or cipher[i + 1] % p != 0:
                    p, q = q, p
                if i > 0:
                    assert cipher[i - 1] % q == 0
                if i < len(cipher) - 1:
                    assert cipher[i + 1] % p == 0
                left = process_cipher_left(cipher[:i], q)
                right = process_cipher_right(cipher[i + 1 :], p)
                if any(prime % 2 == 0 for prime in left + right):
                    p, q = q, p
                    left = process_cipher_left(cipher[:i], q)
                    right = process_cipher_right(cipher[i + 1 :], p)

                found = True
                break
        if found:
            break

    primes = left + [q, p] + right  # type: ignore
    to_char = {p: chr(n) for p, n in zip(sorted(set(primes)), range(65, 65 + 26))}
    # if len(set(primes)) != 26:
    #     raise Exception

    return "".join([to_char[p] for p in primes])


def solve_case(case: int):
    # Init primes
    for p in gen_primes():
        if p == 101:
            break

    # Read data
    N, _ = readmany(int)
    cipher = readmany(int)

    # Solve
    try:
        result = solve(N, cipher)
    except Impossible:
        result = None

    # Write solution
    Output(writesolution(case, result))


############################ Template code ###############################

T = TypeVar("T")


class EndInteractive(Exception):
    pass


class Impossible(Exception):
    pass


def Input() -> str:
    return sys.stdin.readline().strip()


def Output(s: str):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def Finalize():
    sys.stdout.close()
    sys.stderr.close()


def read(typ: Callable[[str], T] = str) -> T:
    return typ(Input())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in Input().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(
    case: int, result: Union[Any, List[Any], None], print_length=False
) -> str:
    """Prints the solution for one case.

    The result will be printed according to the type:
    - None:
        Case #{case}: IMPOSSIBLE
    - Single value:
        Case #{case}: {str(result)}
    - List:
        Case #{case}: {str(result[0]), str(result[1]), str(result[2]), ...}
    - List of lists:
        Case #{case}: {#rows if print_length == True}
        {str(result[0][0]), str(result[0][1]), ...}
        {str(result[1][0]), str(result[1][1]), ...}
        {str(result[2][0]), str(result[2][1]), ...}
        ...
    """
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = str(len(result)) if print_length else ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    return f"Case #{case}: {out_string}"


def main():
    try:
        T = read(int)
        for case in range(1, T + 1):
            solve_case(case)
    except EndInteractive:
        pass
    Finalize()


if __name__ == "__main__":
    main()