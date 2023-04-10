import sys
import time

from algorithms.solver import Solution, Node, Solver, SearchAlgorithm
from problems.problem import Problem, InstrumentedProblem


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


class InformedSolver(Solver):
    def __init__(self, problem: Problem, algorithm: SearchAlgorithm):
        super().__init__(problem, algorithm)
        self.problem = InstrumentedProblem(problem)

    def solve(self) -> InstrumentedSolution:
        self.problem.reset()
        before = time.time()
        node = self.algorithm.search(self.problem)
        after = time.time()

        return InstrumentedSolution(node, self.algorithm.__class__.__name__, after - before, self.problem)
