import sys
import tracemalloc as tm

from algorithms.instrumented_solver import InstrumentedSolver
from algorithms.uninformed.breadth_first_search import BreadthFirstSearch
from problems.npuzzle import NPuzzleProblem, NPuzzleState
from problems.problem import InstrumentedProblem
from constants import *


# def test_memory_profiling():
#     """For an initial state with a known search tree
#     check that the peak memory usage is about the expected.
#     """
#     state = (
#         3, 1, 2,
#         4, 0, 5,
#         6, 7, 8,
#     )
#
#     bfs = BreadthFirstSearch()
#     problem = NPuzzleProblem(state)
#
#     tm.start()
#
#     solution_node = bfs.search(problem)
#
#     tm.take_snapshot()
#
#     peak_memory_in_bytes = tm.get_traced_memory()[1]
#     max_nodes_in_frontier_estimate = peak_memory_in_bytes / sys.getsizeof(NPuzzleState)
#
#     tm.stop()
#
#     # Using breadth-first search, the solution is found at depth 2
#     # Best case: the solution is found before the next level is expanded (frontier nodes: 12)
#     # Worst case: it's found after the next level was completly expanded (frontier nodes: 31)
#     assert 12 <= max_nodes_in_frontier_estimate <= 31


def test_nodes_count():
    state = (
        3, 1, 2,
        4, 0, 5,
        6, 7, 8,
    )

    solver = InstrumentedSolver(NPUZZLE, state, BREADTH_FIRST, None)
    solution_node = solver.solve()

    cant_nodes = solution_node.nodes

    assert 17 <= cant_nodes <= 47
