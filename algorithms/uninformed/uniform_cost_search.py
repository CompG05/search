from typing import Callable

from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.solver import Node


class UniformCostSearch(BestFirstSearch):
    def __init__(self):
        super().__init__(lambda node: node.path_cost)

    def set_heuristic(self, heuristic: Callable[[Node], float]):
        raise NotImplementedError


uniform_cost_search = UniformCostSearch()
