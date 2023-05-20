from constants import *
from generators import generate_nqueens_state
from problems.nqueens import NQueensState
from problems.problem import State


class StateFactory:
    """Factory that generates states for a given problem. Can receive an example state to extract its parameters."""
    def __init__(self, problem_name: str, state: State = None):
        self.problem_name = problem_name
        self.state = state


    def random(self, *args):
        if self.problem_name == NQUEENS:
            state: NQueensState = self.state
            if state is not None:
                dimension = state.dimension
            else:
                dimension = args[0]
            return NQueensState(generate_nqueens_state(dimension))
