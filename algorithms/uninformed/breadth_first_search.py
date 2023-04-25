from collections import deque

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class BreadthFirstSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = deque([initial_node])

        while frontier:
            node = frontier.popleft()
            if problem.is_goal(node.state):
                return node
            frontier.extend(node.expand(problem))

        return None


class BreadthFirstGraphSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = deque([initial_node])

        explored = set()
        while frontier:
            node = frontier.popleft()
            if problem.is_goal(node.state):
                return node
            explored.add(node.state)
            frontier.extend(child for child in node.expand(problem)
                            if child.state not in explored
                            and child not in frontier)

        return None


class BreadthFirstSearchAcyclic(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = deque([initial_node])

        while frontier:
            node = frontier.popleft()
            if problem.is_goal(node.state):
                return node
            frontier.extend(child for child in node.expand(problem)
                            if not node.in_path(child.state))

        return None
