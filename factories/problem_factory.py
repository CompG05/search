from heuristics.npuzzle import NPuzzleHeuristic
from problems.npuzzle import NPuzzleProblem
from utils import random_npuzzle_state


class ProblemFactory:
    def create(self, problem: str, *args):
        if problem.lower() == "npuzzle":  # input: args = [size, depth]
            return self.create_npuzzle(*args)
        else:
            raise ValueError("Problem not found")

    @staticmethod
    def create_npuzzle(size, depth):
        initial_state = random_npuzzle_state(size, depth)

        return NPuzzleProblem(initial_state), NPuzzleHeuristic()


problem_factory = ProblemFactory()
