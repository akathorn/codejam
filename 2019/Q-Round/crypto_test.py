import crypto
import random
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
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
""")
out_str = ("""
Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
""")
# fmt: on


def test_in_out(mocker: MockerFixture):
    mock_read = mocker.patch("crypto.Input")
    mock_write = mocker.patch("crypto.Output")
    _ = mocker.patch("crypto.Finalize")
    mock_read.side_effect = in_str.splitlines()[1:]

    crypto.main()

    out_lines = out_str.splitlines()[1:]
    for call, out in zip(mock_write.mock_calls, out_lines):
        assert call[1][0].strip() == out
    assert len(mock_write.mock_calls) == len(out_lines)


def test_simple():
    gen = crypto.gen_primes()
    primes = []
    while len(primes) < 26:
        p = next(gen)
        if p % 2 != 0:
            primes.append(p)
    to_prime = {chr(n): p for n, p in zip(range(65, 65 + 26), primes)}
    text = [to_prime[c] for c in "CJQUIZKNOWBEVYOFDPFLUXALGORITHMS"]
    cipher = [p * q for p, q in zip(text, text[1:])]

    assert crypto.solve(103, cipher) == "CJQUIZKNOWBEVYOFDPFLUXALGORITHMS"


def test_random():
    random.seed(1111111111111111111111111111111111111)
    for _ in range(1000):
        gen = crypto.gen_primes()
        primes = []
        while len(primes) < 26:
            p = next(gen)
            if p < 101:
                continue
            if random.random() > 0.99:
                primes.append(p)

        if any(p % 2 == 0 for p in primes):
            assert not any(p % 2 == 0 for p in primes)

        to_prime = {chr(n): p for n, p in zip(range(65, 65 + 26), primes)}
        text_raw = [chr(n) for n in range(65, 65 + 26)]
        for _ in range(100 - 26):
            text_raw.append(chr(random.randint(65, 65 + 25)))
        random.shuffle(text_raw)
        text_raw = "".join(text_raw)
        assert len(set(text_raw)) == 26

        text = [to_prime[c] for c in text_raw]
        cipher = [p * q for p, q in zip(text, text[1:])]
        assert len(cipher) == 99

        try:
            assert crypto.solve(10000, cipher) == text_raw
        except ZeroDivisionError:
            crypto.solve(10000, cipher)
        except KeyError:
            crypto.solve(10000, cipher)