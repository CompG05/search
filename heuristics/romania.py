from typing import Callable

from algorithms.solver import Node
from constants import *


class RomaniaHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        raise NotImplementedError
