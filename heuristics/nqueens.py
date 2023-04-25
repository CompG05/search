from typing import Callable

from algorithms.search_algorithm import Node


class NQueensHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        raise NotImplementedError