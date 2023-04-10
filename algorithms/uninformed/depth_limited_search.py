from algorithms.solver import SearchAlgorithm, Node


class DepthLimitedSearch(SearchAlgorithm):
    def __init__(self, limit: int):
        self.limit = limit

    def search(self, problem) -> Node | None:
        initial_node = Node(problem.initial_state)
        frontier = [initial_node]

        while frontier:
            node = frontier.pop()
            if problem.is_goal(node.state):
                return node
            if node.depth < self.limit:
                frontier.extend(node.expand(problem))

        return None
