from problems.problem import Problem, Action


class Node:
    def __init__(self,
                 state,
                 parent: 'Node' = None,
                 action: Action = None,
                 path_cost: float = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem: Problem) -> list['Node']:
        return [Node(problem.result(self.state, action),
                     parent=self,
                     action=action,
                     path_cost=self.path_cost + action.cost)
                for action in problem.enabled_actions(self.state)]

    def in_path(self, state) -> bool:
        node = self.parent
        while node:
            if node.state == state:
                return True
            node = node.parent
        return False

    def path(self) -> list['Node']:
        node = self
        reversed_path = []
        while node:
            reversed_path.append(node)
            node = node.parent
        return list(reversed(reversed_path))

    def solution(self) -> list[Action]:
        return [node.action for node in self.path()[1:]]

    def __lt__(self, other):
        return self.path_cost < other.path_cost


class SearchAlgorithm:
    def search(self, problem: Problem) -> Node | None:
        raise NotImplementedError
