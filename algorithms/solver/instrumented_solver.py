import sys
import time
import tracemalloc as tm
from typing import Optional

from algorithms.solver import Solution, Solver
from algorithms.search_algorithm import Node
from problems.problem import InstrumentedProblem, InvertibleProblem, InstrumentedInvertibleProblem


class InstrumentedSolution(Solution):
    def __init__(self, node: Node | None, algorithm_name: str, heuristic_name: str, initial_state, dtime, memory_peak, problem: InstrumentedProblem):
        super().__init__(node, algorithm_name, heuristic_name, initial_state)
        self.problem = problem
        self.node_size = sys.getsizeof(node)
        self.time = dtime * 1000
        self.memory = memory_peak
        self.nodes = problem.nodes


    def __str__(self):
        return super().__str__() + f"""
time: %.2f ms
branching factor: %.4f
generated nodes: {self.nodes}
max nodes in frontier: {self.problem.max_nodes_in_frontier}
max memory usage: {self.memory} bytes"""\
            % (self.time, self.problem.branching_factor)

    @classmethod
    def csv_header(cls):
        return super().csv_header() + ",time (ms), nodes, memory (Kb)"

    def to_csv(self):
        return super().to_csv() + f",{self.time},{self.nodes},%.3f" % (self.memory / 1000)


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
        tm.start()
        node = self.algorithm.search(self.problem)
        tm.take_snapshot()
        memory_peak = tm.get_traced_memory()[1]
        after = time.time()
        tm.stop()

        return InstrumentedSolution(node, self.algorithm_name, self.heuristic_name, self.problem.initial_state, after - before, memory_peak, self.problem)
