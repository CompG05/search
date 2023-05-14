import heapq
from typing import Callable

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class HillClimbing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float]):
        self.heuristic = heuristic
        super().__init__()

    def search(self, problem: Problem) -> Node | None:
        current: Node = Node(problem.initial_state)

        while True:
            neighbors = current.expand(problem)
            neighbor = max(neighbors, key=(lambda n: self.heuristic(n)))

            if self.heuristic(neighbor) <= self.heuristic(current):
                return current

            current = neighbor
