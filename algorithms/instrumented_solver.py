import sys
import time
from typing import Optional

from algorithms.solver import Solution, Solver
from algorithms.search_algorithm import Node
from problems.problem import InstrumentedProblem, InvertibleProblem, InstrumentedInvertibleProblem


class InstrumentedSolution(Solution):
    def __init__(self, node: Node | None, algorithm_name: str, heuristic_name: str, initial_state, dtime, problem: InstrumentedProblem):
        super().__init__(node, algorithm_name, heuristic_name, initial_state)
        self.problem = problem
        self.node_size = sys.getsizeof(node)
        self.time = dtime * 1000
        self.memory = self.problem.max_nodes_in_frontier * self.node_size


    def __str__(self):
        return super().__str__() + f"""
time: %.2f ms
branching factor: %.4f
generated nodes: {self.problem.nodes}
max nodes in frontier: {self.problem.max_nodes_in_frontier}
max memory usage: {self.memory} bytes"""\
            % (self.time, self.problem.branching_factor)

    @classmethod
    def csv_header(cls):
        return super().csv_header() + ",time (ms),nodes,memory (bytes)"

    def to_csv(self):
        return super().to_csv() + f",{self.time},{self.problem.nodes},{self.memory}"


class InstrumentedSolver(Solver):
    def __init__(self, problem: str, initial_state, algorithm: str, heuristic: Optional[str]):
        super().__init__(problem, initial_state, algorithm, heuristic)
        if isinstance(self.problem, InvertibleProblem):
            self.problem = InstrumentedInvertibleProblem(self.problem)
        else:
            self.problem = InstrumentedProblem(self.problem)

    def solve(self) -> InstrumentedSolution:
        self.problem.reset()
        before = time.time()
        node = self.algorithm.search(self.problem)
        after = time.time()

        return InstrumentedSolution(node, self.algorithm_name, self.heuristic_name, self.problem.initial_state, after - before, self.problem)
