from typing import Callable

from algorithms.search_algorithm import Node
from problems.nqueens import NQueensState
from constants import *


class NQueensHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == N_CONFLICTS:
            return self.n_conflicts
        if heuristic.lower() == INVERSE_N_CONFLICTS:
            return lambda n: -self.n_conflicts(n)
        else:
            raise ValueError("Heuristic not found")

    @staticmethod
    def n_conflicts(node: Node):
        state: NQueensState = node.state
        return state.n_conflicts()
