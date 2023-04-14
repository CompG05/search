from typing import Callable

from algorithms.search_algorithm import Node


class NPuzzleHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == "wrong_tiles":
            return self.wrong_tiles
        else:
            raise ValueError("Heuristic not found")

    @staticmethod
    def wrong_tiles(node: Node) -> float:
        state = node.state
        return sum(1 for i, j in zip(state.data, range(0, state.size)) if i != j)
