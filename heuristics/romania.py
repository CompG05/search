from typing import Callable

from algorithms.solver import Node
from constants import *
import math

from problems.graph_problem import Vertex


class RomaniaHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == LINEAR_DISTANCE:
            return self.linear_distance
        else:
            raise ValueError("Heuristic not found")

    @staticmethod
    def linear_distance(node: Node) -> float:
        state: Vertex = node.state

        (x_a, y_a) = romania_locations[state.current]
        (x_b, y_b) = romania_locations[state.goal]

        return math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
