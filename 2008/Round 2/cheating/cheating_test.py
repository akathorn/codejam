import cheating


def test_build_tree():
    cheating.build_tree([(1, 1), (0, 0), 1, 1, 0], 0)
    cheating.build_tree([(1, 0), (1, 1), (1, 1), (0, 0), 1, 0, 1, 0, 1], 0)


def test_sample():
    assert cheating.solve(1, [(1, 0), (1, 1), (1, 1), (0, 0)], [1, 0, 1, 0, 1]) == 1
    assert cheating.solve(0, [(1, 1), (0, 0)], [1, 1, 0]) == None


def test_sanity():
    assert cheating.solve(1, [(1, 1)], [0, 0]) == None
    assert cheating.solve(1, [(1, 1)], [1, 0]) == 1
    assert cheating.solve(1, [(1, 1)], [0, 1]) == 1
    assert cheating.solve(1, [(1, 1)], [1, 1]) == 0
    assert cheating.solve(0, [(0, 1)], [0, 0]) == 0
    assert cheating.solve(0, [(0, 1)], [1, 0]) == 1
    assert cheating.solve(0, [(0, 1)], [0, 1]) == 1
    assert cheating.solve(0, [(0, 1)], [1, 1]) == None
    assert cheating.solve(1, [(1, 0)], [1, 0]) == None
    assert cheating.solve(1, [(1, 1), (0, 0)], [0, 0, 0]) == None