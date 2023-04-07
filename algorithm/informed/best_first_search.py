import heapq
from typing import Callable

from algorithm.solver import SearchAlgorithm, Node
from problems.problem import Problem


class BestFirstSearch(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float]):
        super().__init__()
        self.heuristic = heuristic

    def set_heuristic(self, heuristic: Callable[[Node], float]):
        self.heuristic = heuristic

    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = [(self.heuristic(initial_node), initial_node)]
        heapq.heapify(frontier)

        while frontier:
            _, node = heapq.heappop(frontier)
            if problem.is_goal(node.state):
                return node
            for child in node.expand(problem):
                heapq.heappush(frontier, (self.heuristic(child), child))

        return None
