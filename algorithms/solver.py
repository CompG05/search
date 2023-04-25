from algorithms.search_algorithm import Node
from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory


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


class Solver:
    def __init__(self, problem: str, initial_state, algorithm: str, heuristic: str):
        self.problem, heuristic_factory = problem_factory.create(problem, initial_state)
        self.heuristic = heuristic and heuristic_factory.create(heuristic)
        self.algorithm = algorithm_factory.create(algorithm, self.heuristic)

    def solve(self) -> Solution:
        node = self.algorithm.search(self.problem)
        return Solution(node, self.algorithm.__class__.__name__)
