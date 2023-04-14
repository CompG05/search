import heapq
from typing import Callable

from algorithms.search_algorithm import SearchAlgorithm, Node
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
        reached = {problem.initial_state: initial_node}

        while frontier:
            _, node = heapq.heappop(frontier)
            if problem.is_goal(node.state):
                return node
            for child in node.expand(problem):
                if child.state not in reached or child.path_cost < reached[child.state].path_cost:
                    reached[child.state] = child
                    heapq.heappush(frontier, (self.heuristic(child), child))

        return None
