from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class DepthFirstSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = [initial_node]

        while frontier:
            node = frontier.pop()
            if problem.is_goal(node.state):
                return node
            frontier.extend(node.expand(problem))

        return None


class DepthFirstGraphSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = [initial_node]

        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.is_goal(node.state):
                return node
            explored.add(node.state)
            frontier.extend(child for child in node.expand(problem)
                            if child.state not in explored
                            and child not in frontier)

        return None


class DepthFirstSearchAcyclic(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = [initial_node]

        while frontier:
            node = frontier.pop()
            if problem.is_goal(node.state):
                return node
            frontier.extend(child for child in node.expand(problem)
                            if not node.in_path(child.state) and node.state != child.state)

        return None
