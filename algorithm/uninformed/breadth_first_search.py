from collections import deque

from problems.problem import Problem
from algorithm.solver import SearchAlgorithm, Node


class BreadthFirstSearch(SearchAlgorithm):
    def search(self,
               problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = deque([initial_node])

        while frontier:
            node = frontier.popleft()
            if problem.is_goal(node.state):
                return node
            frontier.extend(node.expand(problem))

        return None


breadth_first_search = BreadthFirstSearch()
