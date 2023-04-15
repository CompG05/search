from typing import Callable

from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.search_algorithm import Node


class AStar(BestFirstSearch):
    def __init__(self, heuristic: Callable[[Node], float]):
        super().__init__(lambda node: node.path_cost + heuristic(node))

    def set_heuristic(self, new_heuristic: Callable[[Node], float]):
        self.heuristic = (lambda node: node.path_cost + new_heuristic(node))
