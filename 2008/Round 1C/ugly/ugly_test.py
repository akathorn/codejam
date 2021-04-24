import ugly


# def test_rec_solutions():
#     s = ugly.rec_solutions("123")
#     assert ugly.rec_solutions("123") == [6, 0, 24, -22, 123]


def test_evaluate():
    assert ugly.evaluate("1") == 1
    assert ugly.evaluate("12") == 12
    assert ugly.evaluate("1+2") == 3
    assert ugly.evaluate("1-2") == -1
    assert ugly.evaluate("1-02") == -1
    assert ugly.evaluate("01-2") == -1
    assert ugly.evaluate("-12") == -12
    assert ugly.evaluate("0-0") == 0


def test_solve():
    assert ugly.solve("123")
    assert ugly.solve("12")


def test_sample():
    assert ugly.solve("1") == 0
    assert ugly.solve("9") == 1
    assert ugly.solve("011") == 6
    assert ugly.solve("12345") == 64


def test_other():
    ugly.solve("001")
    ugly.solve("010")
    ugly.solve("1000")
    ugly.solve("000")


def test_biggish():
    ugly.solve("1234567890123")


def test_big():
    ugly.solve("123456789012312345678901231234567890123")


# def test_evaluate():
#     assert ugly.evaluate(ugly.Exp("3", "+", "4")) == 7
#     assert ugly.evaluate(ugly.Exp("3", "-", "4")) == -1