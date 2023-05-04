import os
import sys

from algorithms.solver import Solver
from generators import *
from constants import *

generators = {
    NPUZZLE: generate_npuzzle_state,
    NQUEENS: generate_nqueens_state,
    ROMANIA: generate_romania_state,
}

cache = {}


def depth(s, problem):
    """Return the depth of the shortest solution"""
    if s in cache:
        return cache[s]

    heuristic = WRONG_ROW_COL if problem == NPUZZLE else N_CONFLICTS
    if problem == NPUZZLE:
        heuristic = WRONG_ROW_COL
    elif problem == NQUEENS:
        heuristic = N_CONFLICTS
    elif problem == ROMANIA:
        heuristic = LINEAR_DISTANCE
    else:
        raise ValueError("Invalid problem")

    solver = Solver(problem, s, A_STAR, heuristic)
    solution = solver.solve()
    cache[s] = solution.depth
    return solution.depth


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Use -h for help")
        return

    if len(args) == 1:
        if args[0] == "-h":
            print("Usage: python state_generator.py [-o <file>] <num_states> <problem> [problem_args]")
            print("Operations:")
            print("  -h  Show this help message")
            print("  -l  List available problems")
            print("  -o  Output to file")
            print("  -d  Delete file")
            return
        if args[0] == "-l":
            print("Available problems:")
            print(f"{NPUZZLE}, {NQUEENS}, {ROMANIA}")
            return

    file_name = None

    if "-o" in args:
        index = args.index("-o")
        if index == len(args) - 1:
            print("Missing file name")
            return
        file_name = args[index + 1]
        args.pop(index)
        args.pop(index)

    if "-d" in args:
        index = args.index("-d")
        if index == len(args) - 1:
            print("Missing file name")
            return
        file_name = args[index + 1]
        file_path = f"./{file_name}"
        try:
            os.remove(file_path)
            print("File deleted successfully")
        except:
            print("File not found")
        return

    if len(args) < 2:
        print("Missing arguments")
        return

    num_states = int(args[0])
    problem = args[1]
    problem_args = args[2:]

    if problem == ROMANIA:
        num_states = min(num_states, len(romania_map.nodes()) ** 2)

    if problem == NPUZZLE or problem == NQUEENS:
        if len(problem_args) != 1:
            print(f"Usage: python state_generator.py [-o <file>] <num_states> {problem} <dimension>")
            return
        dimension = int(problem_args[0])

        # half of states are random
        states = [generators[problem](dimension) for _ in range(int(num_states / 2))]

        # the rest are the most difficult of a sample -evaluated by A* (Wrong_row_col for npuzzle)/(N_conflicts for
        # nqueens)-
        remaining = num_states - int(num_states / 2)  # In case num_states is odd
        hard_states = [generators[problem](dimension) for _ in range(remaining * 3)]

    elif problem == ROMANIA:
        states = []
        hard_states_raw = [(src, dst) for src in romania_map.nodes() for dst in romania_map.nodes()]
        hard_states = []
        for (src, dst) in hard_states_raw:
            if (dst, src) not in hard_states:
                hard_states.append((src, dst))
        remaining = num_states

    else:
        print("Unknown problem: " + problem)
        return

    hard_states.sort(key=lambda s: depth(s, problem), reverse=True)
    hard_states = hard_states[:remaining]

    if file_name is None:
        for state in states + hard_states:
            print(state)
    else:
        with open(file_name, "w") as file:
            for state in states + hard_states:
                # Write tuple as csv
                file.write(",".join(str(x) for x in state) + "\n")


if __name__ == "__main__":
    main()
