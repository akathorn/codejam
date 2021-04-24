from enum import Enum
import sys
from typing import Dict, List, NamedTuple, Tuple


Trip = NamedTuple("Trip", [("origin", str), ("departure", int), ("arrival", int)])


class State(Enum):
    TRAVELLING_A = 1
    TRAVELLING_B = 2
    TURNAROUND = 3
    WAITING = 4


class Train:
    def __init__(self):
        self.state: State = State.WAITING
        self.location = ""
        self.end_time: int = 0


def solve(turnaround: int, trips: List[Trip]) -> Tuple[int, int]:
    trains: List[Train] = []
    ready_A: List[Train] = []
    ready_B: List[Train] = []
    started_in_A = 0
    started_in_B = 0

    departures: Dict[int, List[Trip]] = {t: [] for t in range(24 * 60)}
    for trip in trips:
        departures[trip.departure].append(trip)

    for t in range(24 * 60):
        for train in trains:
            # Update the trains
            if train.end_time == t:
                if train.state == State.TRAVELLING_A:
                    if turnaround > 0:
                        train.state = State.TURNAROUND
                        train.end_time = t + turnaround
                        train.location = "A"
                    else:
                        train.state = State.WAITING
                        ready_A.append(train)
                elif train.state == State.TRAVELLING_B:
                    if turnaround > 0:
                        train.state = State.TURNAROUND
                        train.end_time = t + turnaround
                        train.location = "B"
                    else:
                        train.state = State.WAITING
                        ready_B.append(train)
                elif train.state == State.TURNAROUND:
                    train.state = State.WAITING
                    if train.location == "A":
                        ready_A.append(train)
                    else:
                        ready_B.append(train)
        for trip in departures[t]:
            if trip.origin == "A":
                if ready_A:
                    train = ready_A.pop()
                else:
                    train = Train()
                    trains.append(train)
                    started_in_A += 1
                train.state = State.TRAVELLING_B
            else:
                if ready_B:
                    train = ready_B.pop()
                else:
                    train = Train()
                    trains.append(train)
                    started_in_B += 1
                train.state = State.TRAVELLING_A
            train.end_time = trip.arrival

    return started_in_A, started_in_B


def parse_time(s: str) -> int:
    hh, mm = s.split(":")
    return int(hh) * 60 + int(mm)


def main():
    N = int(sys.stdin.readline())
    for case in range(1, N + 1):
        T = int(sys.stdin.readline())
        na, nb = sys.stdin.readline().split()

        trips: List[Trip] = []
        for _ in range(int(na)):
            departure, arrival = sys.stdin.readline().split()
            trips.append(Trip("A", parse_time(departure), parse_time(arrival)))

        for _ in range(int(nb)):
            departure, arrival = sys.stdin.readline().split()
            trips.append(Trip("B", parse_time(departure), parse_time(arrival)))

        a, b = solve(T, trips)
        print(f"Case #{case}: {a} {b}")
    sys.stdout.close()


if __name__ == "__main__":
    main()