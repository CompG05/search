import sys
import argparse
import signal

from algorithms.instrumented_solver import InstrumentedSolver, InstrumentedSolution
from algorithms.solver import Solution
from constants import *

TIME_LIMIT = 50


def handle_timeout(signum, frame):
    raise TimeoutError


def read_simple_tuple(s: str, problem) -> tuple:
    if problem == ROMANIA:
        return tuple(x.strip() for x in s.split(","))
    else:
        return tuple(int(x) for x in s.split(","))


def read_states(input_file, problem):
    """Convert a csv file into a list of tuples."""
    states = []
    print("Parsing input...")
    with open(input_file, "r") as f:
        for line in f:
            states.append(read_simple_tuple(line, problem))
    return states


def benchmark(problem, initial_states):
    """Return a list of solutions"""
    print("Testing algorithms...")

    # signal.signal(signal.SIGALRM, handle_timeout)

    result = []
    tests = ((len(uninformed_algorithms.keys())) + len(informed_algorithms.keys()) * len(heuristics[problem])) * len(
        initial_states)
    iteration = 0

    print(f"0/{tests}")

    for algorithm in uninformed_algorithms:
        for initial_state in initial_states:
            solver = InstrumentedSolver(problem, initial_state, algorithm, None)
            # signal.alarm(TIME_LIMIT)
            try:
                solution = solver.solve()
            except TimeoutError:
                solution = Solution.not_found(algorithm, None, initial_state)
            iteration += 1
            print(f"{iteration}/{tests}")
            result.append(solution)

    for algorithm in informed_algorithms:
        for initial_state in initial_states:
            for heuristic in heuristics[problem]:
                solver = InstrumentedSolver(problem, initial_state, algorithm, heuristic)
                # signal.alarm(TIME_LIMIT)
                try:
                    solution = solver.solve()
                except TimeoutError:
                    solution = Solution.not_found(algorithm, heuristic, initial_state)
                iteration += 1
                print(f"{iteration}/{tests}")
                result.append(solution)

    return result


def write_report(result, output_file):
    """Write the list of solutions to the output file (or stdout)"""
    print("Writing report...")
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

    args = parser.parse_args(sys.argv[1:])

    initial_states = read_states(args.input_file, args.problem)
    result = benchmark(args.problem, initial_states)
    write_report(result, args.output_file)
    print("Finished!")


if __name__ == "__main__":
    main()
