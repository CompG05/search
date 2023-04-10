from typing import Callable

import pytest
from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.aima_algorithms.best_first_search import best_first_graph_search
from problems.npuzzle import h_wrong_positions, NPuzzleProblem, NPuzzleState
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

bfs = BestFirstSearch(h_wrong_positions)
bfs_t = best_first_graph_search

algorithms_config = [
    # (bfs, bfs_t, s) for s in generate_npuzzle_states(9, 8)
    (bfs, bfs_t, NPuzzleState((3, 0, 2, 5, 4, 8, 7, 6, 1)))
]


@pytest.mark.parametrize("ours, theor, state", algorithms_config)
def test_theoretical_vs_ours(ours: BestFirstSearch, theor: Callable, state):
    p.initial_state = state
    assert ours.search(p).solution() == theor(p, h_wrong_positions).solution()
