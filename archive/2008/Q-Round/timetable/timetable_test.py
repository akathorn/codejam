from timetable import solve, Trip, parse_time


def test_basic():
    trips = [
        Trip("A", parse_time("09:00"), parse_time("12:00")),
        Trip("A", parse_time("10:00"), parse_time("13:00")),
        Trip("A", parse_time("11:00"), parse_time("12:30")),
        Trip("B", parse_time("12:02"), parse_time("15:00")),
        Trip("B", parse_time("09:00"), parse_time("10:30")),
    ]

    assert solve(5, trips) == (2, 2)


def test_basic2():
    trips = [
        Trip("A", parse_time("09:00"), parse_time("09:01")),
        Trip("A", parse_time("12:00"), parse_time("12:02")),
    ]

    assert solve(2, trips) == (2, 0)


def test_zero():
    trips = [
        Trip("A", parse_time("09:00"), parse_time("09:01")),
        Trip("B", parse_time("09:01"), parse_time("12:00")),
    ]

    assert solve(0, trips) == (1, 0)