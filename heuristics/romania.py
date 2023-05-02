from typing import Callable

from algorithms.solver import Node
from constants import *
import math


class RomaniaHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == LINEAR_DISTANCE:
            return self.linear_distance_to_bucharest
        else:
            raise ValueError("Heuristic not found")

    @staticmethod
    def linear_distance_to_bucharest(node: Node) -> float:
        state: str = node.state

        (x_a, y_a) = romania_locations[state]
        (x_b, y_b) = romania_locations['Bucharest']

        return math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
