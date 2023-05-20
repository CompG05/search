from typing import Callable

from algorithms.search_algorithm import Node
from constants import ACCUM_VALUE


class KnapsackHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == ACCUM_VALUE:
            return self.accumulated_value

    @staticmethod
    def accumulated_value(node: Node) -> float:
        return node.state.sack_value
        # sack_content: set[int] = node.state.data
        # value: list[float] = node.state.value
        # return sum([value[i] for i in sack_content])
