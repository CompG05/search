from typing import Callable

from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.search_algorithm import Node
from algorithms.uninformed.bidirectional_search import bidirectional_search
from algorithms.uninformed.breadth_first_search import breadth_first_search


class AlgorithmFactory:
    def create(self, algorithm: str, heuristic: Callable[[Node], float]):
        if algorithm.lower() == "breadthfirst":
            return breadth_first_search
        if algorithm.lower() == "bestfirst":
            return BestFirstSearch(heuristic)
        if algorithm.lower() == "bidirectional":
            return bidirectional_search
        else:
            raise ValueError(f"Algorithm '{algorithm}' not found")


algorithm_factory = AlgorithmFactory()
