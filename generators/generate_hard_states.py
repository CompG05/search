import signal
import os
import sys

from algorithms.instrumented_solver import InstrumentedSolution
from algorithms.solver import Solver
from generators import generate_npuzzle_state
from constants import *

TIME_LIMIT = 60


def handle_timeout(signum, frame):
    raise TimeoutError


def nonstop_states(filename, dimension: int):
    if dimension < 4:
        print("WARNING: This program is meant to generate states for 15-Puzzle or bigger")

    signal.signal(signal.SIGALRM, handle_timeout)

    while True:
        state = generate_npuzzle_state(dimension)
        solver = Solver(NPUZZLE, state, A_STAR, MANHATTAN_DISTANCE)

        signal.alarm(TIME_LIMIT)
        try:
            _ = solver.solve()
            with open(filename, "a") as f:
                f.write(",".join(str(x) for x in state) + "\n")
        except TimeoutError:
            pass


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: %s <output_file> <dimension>" % sys.argv[0])
    nonstop_states(args[0], int(args[1]))


if __name__ == "__main__":
    main()
