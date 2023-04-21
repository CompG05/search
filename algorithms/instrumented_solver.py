import sys
import time

from algorithms.solver import Solution, Solver
from algorithms.search_algorithm import Node
from problems.problem import InstrumentedProblem, InvertibleProblem, InstrumentedInvertibleProblem


class InstrumentedSolution(Solution):
    def __init__(self, node: Node | None, algorithm_name: str, dtime, problem: InstrumentedProblem):
        super().__init__(node, algorithm_name)
        self.problem = problem
        self.node_size = sys.getsizeof(node)
        self.time = dtime

    def __str__(self):
        return super().__str__() + f"""
time: %.2f ms
branching factor: %.4f
generated nodes: {self.problem.nodes}
max nodes in frontier: {self.problem.max_nodes_in_frontier}
max memory usage: {self.problem.max_nodes_in_frontier * self.node_size} bytes"""\
            % (self.time * 1000, self.problem.branching_factor)


class InstrumentedSolver(Solver):
    def __init__(self, problem: str, initial_state, algorithm: str, heuristic: str, *args):
        super().__init__(problem, initial_state, algorithm, heuristic, *args)
        if isinstance(self.problem, InvertibleProblem):
            self.problem = InstrumentedInvertibleProblem(self.problem)
        else:
            self.problem = InstrumentedProblem(self.problem)

    def solve(self) -> InstrumentedSolution:
        self.problem.reset()
        before = time.time()
        node = self.algorithm.search(self.problem)
        after = time.time()

        return InstrumentedSolution(node, self.algorithm.__class__.__name__, after - before, self.problem)
