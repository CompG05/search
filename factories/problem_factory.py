from heuristics.npuzzle import NPuzzleHeuristic
from heuristics.nqueens import NQueensHeuristic
from heuristics.romania import RomaniaHeuristic
from problems.npuzzle import NPuzzleProblem
from problems.nqueens import NQueensProblem
from constants import *


class ProblemFactory:
    def create(self, problem: str, initial_state):
        if problem.lower() == NPUZZLE:
            return NPuzzleProblem(initial_state), NPuzzleHeuristic()
        elif problem.lower() == NQUEENS:
            return NQueensProblem(initial_state), NQueensHeuristic()
        elif problem.lower() == ROMANIA:
            return GraphProblem(romania_map, initial_state[0], initial_state[1]), RomaniaHeuristic()
        else:
            raise ValueError("Problem not found")


problem_factory = ProblemFactory()
