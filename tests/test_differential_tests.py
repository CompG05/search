from typing import Callable

import pytest

from algorithms.aima_algorithms.best_first_search import best_first_graph_search
from algorithms.informed.best_first_search import BestFirstSearch
from problems.npuzzle import NPuzzleProblem, NPuzzleState
from utils import generate_npuzzle_states

initial = (
    1, 4, 2,
    6, 5, 0,
    7, 3, 8
)

# 0, 1, 2
# 3, 4, 5
# 6, 7, 8

p = NPuzzleProblem(initial)

# bfs = BestFirstSearch(h_wrong_positions)
bfs = BestFirstSearch(lambda node: node.depth)
bfs_t = best_first_graph_search

algorithms_config = [
    (bfs, bfs_t, s) for s in generate_npuzzle_states(9, 1000)
]


@pytest.mark.parametrize("ours, theor, state", algorithms_config)
def test_theoretical_vs_ours(ours: BestFirstSearch, theor: Callable, state):
    p.initial_state = state
    our_solution_node = ours.search(p)
    other_solution_node = theor(p, lambda node: node.depth)

    our_solution = our_solution_node.solution()
    other_solution = other_solution_node.solution()
    assert our_solution == other_solution or len(our_solution) == len(other_solution)
