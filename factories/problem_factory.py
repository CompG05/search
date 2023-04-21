from heuristics.npuzzle import NPuzzleHeuristic
from problems.npuzzle import NPuzzleProblem


class ProblemFactory:
    def create(self, problem: str, initial_state, *args):
        if problem.lower() == "npuzzle":  # input: args = [size, depth]
            return self.create_npuzzle(initial_state)
        else:
            raise ValueError("Problem not found")

    @staticmethod
    def create_npuzzle(initial_state):
        return NPuzzleProblem(initial_state), NPuzzleHeuristic()


problem_factory = ProblemFactory()
