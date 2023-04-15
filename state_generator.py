import sys

from generators import generate_npuzzle_state


NPUZZLE = "NPuzzle"


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
            return
        if args[0] == "-l":
            print("Available problems:")
            print("  " + NPUZZLE)
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

    if len(args) < 2:
        print("Missing arguments")
        return

    num_states = int(args[0])
    problem = args[1]
    problem_args = args[2:]

    states = []

    if problem == NPUZZLE:
        if len(problem_args) != 1:
            print("Usage: python state_generator.py [-o <file>] <num_states> NPuzzle <dimension>")
            return
        dimension = int(problem_args[0])
        states = [generate_npuzzle_state(dimension) for _ in range(num_states)]
    else:
        print("Unknown problem: " + problem)
        return

    if file_name is None:
        for state in states:
            print(state)
    else:
        with open(file_name, "w") as file:
            for state in states:
                # Write tuple as csv
                file.write(",".join(str(x) for x in state) + "\n")


if __name__ == "__main__":
    main()
