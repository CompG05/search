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
        return [Node(action.execute(self.state),
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


class Solution:
    def __init__(self, node: Node):
        self.final_state = node.state
        self.path = [node.state for node in node.path()]
        self.path_cost = node.path_cost
        self.action_sequence = node.solution()


class SearchAlgorithm:
    def search(self, problem: Problem) -> Solution:
        raise NotImplementedError


class Solver:
    def __init__(self, problem: Problem, algorithm: SearchAlgorithm = None):
        self.problem = problem
        self.algorithm = algorithm

    def set_algorithm(self, algorithm: SearchAlgorithm):
        self.algorithm = algorithm

    def solve(self) -> Solution:
        return self.algorithm.search(self.problem)
