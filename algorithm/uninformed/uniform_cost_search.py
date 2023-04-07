from typing import Callable

from algorithm.informed.best_first_search import BestFirstSearch
from algorithm.solver import Node


class UniformCostSearch(BestFirstSearch):
    def __init__(self):
        super().__init__(lambda node: node.path_cost)

    def set_heuristic(self, heuristic: Callable[[Node], float]):
        raise NotImplementedError


uniform_cost_search = UniformCostSearch()
