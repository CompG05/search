from typing import Callable

from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.search_algorithm import Node
from algorithms.uninformed.breadth_first_search import breadth_first_search


class AlgorithmFactory:
    def create(self, algorithm: str, heuristic: Callable[[Node], float]):
        if algorithm.lower() == "breadthfirstsearch":
            return breadth_first_search
        if algorithm.lower() == "bestfirstsearch":
            return BestFirstSearch(heuristic)


algorithm_factory = AlgorithmFactory()
