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


class Solution:
    def __init__(self, node: Node | None, algorithm_name: str):
        if not node:
            self.final_state = None
            self.path = []
            self.path_cost = []
            self.action_sequence = []
        else:
            self.final_state = node.state
            self.path = [node.state for node in node.path()]
            self.path_cost = node.path_cost
            self.action_sequence = node.solution()
        self.algorithm_name = algorithm_name

    def __str__(self):
        return f"""
algorithm: {self.algorithm_name}
final state: {self.final_state}
path cost: {self.path_cost}
action sequence: {self.action_sequence}"""


class SearchAlgorithm:
    def search(self, problem: Problem) -> Node | None:
        raise NotImplementedError


class Solver:
    def __init__(self, problem: Problem, algorithm: SearchAlgorithm):
        self.problem = problem
        self.algorithm = algorithm

    def set_algorithm(self, algorithm: SearchAlgorithm):
        self.algorithm = algorithm

    def solve(self) -> Solution:
        node = self.algorithm.search(self.problem)
        return Solution(node, self.algorithm.__class__.__name__)
