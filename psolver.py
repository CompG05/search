import sys
import argparse
import signal

from algorithms.instrumented_solver import InstrumentedSolver, InstrumentedSolution
from algorithms.solver import Solution
from constants import *

TIME_LIMIT = 90


def handle_timeout(signum, frame):
    raise TimeoutError


def print_progress(iteration, total):
    length = 60
    filled_len = length * iteration // total
    bar = "[" + "#" * filled_len + "-" * (length - filled_len) + "]"
    print(f"\r{bar} {iteration}/{total}", end="\r")


def read_simple_tuple(s: str, problem) -> tuple:
    if problem == ROMANIA:
        return tuple(x.strip() for x in s.split(","))
    else:
        return tuple(int(x) for x in s.split(","))


def read_states(input_file, problem):
    """Convert a csv file into a list of tuples."""
    states = []
    with open(input_file, "r") as f:
        for line in f:
            states.append(read_simple_tuple(line, problem))
    return states


def benchmark(problem, algorithm, initial_states):
    """Return a list of solutions"""
    signal.signal(signal.SIGALRM, handle_timeout)

    result = []
    n_heuristics = (len(heuristics[problem]) * (algorithm in informed_algorithms)) or 1
    n_states = len(initial_states)

    tests = n_heuristics * n_states
    iteration = 0

    print_progress(iteration, tests)

    h = heuristics[problem] if algorithm in informed_algorithms else [None]

    for heuristic in h:
        for initial_state in initial_states:
            solver = InstrumentedSolver(problem, initial_state, algorithm, heuristic)
            signal.alarm(TIME_LIMIT)
            try:
                solution = solver.solve()
            except TimeoutError:
                solution = Solution.not_found(algorithm, heuristic, initial_state)
            iteration += 1
            print_progress(iteration, tests)
            result.append(solution)

    print()

    return result


def write_report(result, output_file):
    """Write the list of solutions to the output file (or stdout)"""
    buffer = open(output_file, "w") if output_file else sys.stdout
    buffer.write(InstrumentedSolution.csv_header() + "\n")
    for solution in result:
        buffer.write(solution.to_csv() + "\n")

    if buffer is not sys.stdout:
        buffer.close()


def main():
    """Takes an input file with initial states and generates a report
    comparing the different algorithms and heuristics.
    """
    parser = argparse.ArgumentParser(
        prog="psolver.py",
        description="Solve a problem using different algorithms and heuristics.")

    parser.add_argument("-i", "--input",
                        action="store",
                        default="input.txt",
                        help="input file with initial states (default: input.txt)",
                        dest="input_file")

    parser.add_argument("-o", "--output",
                        action="store",
                        help="output file with results",
                        dest="output_file")

    parser.add_argument("problem",
                        action="store",
                        choices=problems,
                        metavar="problem",
                        help="problem to solve")

    parser.add_argument("algorithm",
                        choices=list(uninformed_algorithms.keys()) + list(informed_algorithms.keys()),
                        metavar="algorithm",
                        help="algorithm to use")

    args = parser.parse_args(sys.argv[1:])

    initial_states = read_states(args.input_file, args.problem)
    result = benchmark(args.problem, args.algorithm, initial_states)
    write_report(result, args.output_file)


if __name__ == "__main__":
    main()
