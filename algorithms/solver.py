from typing import Optional

from algorithms.search_algorithm import Node
from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory


class Solution:
    def __init__(self, node: Node | None, algorithm_name: str, heuristic_name: Optional[str], initial_state):
        if not node:
            self.final_state = None
            self.path = []
            self.path_cost = []
            self.action_sequence = []
            self.depth = 0
        else:
            self.final_state = node.state
            self.path = [node.state for node in node.path()]
            self.path_cost = node.path_cost
            self.action_sequence = node.solution()
            self.depth = node.depth
        self.algorithm_name = algorithm_name
        self.heuristic_name = heuristic_name
        self.initial_state = initial_state

    @classmethod
    def not_found(cls, algorithm_name: str, heuristic_name: Optional[str], initial_state):
        return Solution(None, algorithm_name, heuristic_name, initial_state)

    def __str__(self):
        return f"""
algorithm: {self.algorithm_name}
final state: {self.final_state}
path cost: {self.path_cost}
action sequence: {self.action_sequence}"""

    @classmethod
    def csv_header(cls):
        return "algorithm,heuristic,depth,initial_state,final_state,action_sequence,path_cost"

    def to_csv(self):
        return f"{self.algorithm_name},{self.heuristic_name},{self.depth},\"{self.initial_state}\",\"{self.final_state}\",\"{self.action_sequence}\",{self.path_cost}"


class Solver:
    def __init__(self, problem: str, initial_state, algorithm: str, heuristic: str):
        self.problem, heuristic_factory = problem_factory.create(problem, initial_state)
        self.heuristic = heuristic and heuristic_factory.create(heuristic)
        self.algorithm = algorithm_factory.create(algorithm, self.heuristic)

    def solve(self) -> Solution:
        node = self.algorithm.search(self.problem)
        heuristic_name = "" if self.heuristic is None else self.heuristic.__name__
        return Solution(node, self.algorithm.__class__.__name__, heuristic_name, self.problem.initial_state)
