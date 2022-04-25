import alien


def test_example():
    assert alien.solve("(ab)d(dc)", ["add", "adc", "bdd", "bdc"]) == 4