from typing import Callable

import pytest

from algorithms.aima_algorithms.astar import astar_search
from algorithms.aima_algorithms.breadth_first_tree_search import breadth_first_tree_search
from algorithms.aima_algorithms.best_first_search import best_first_graph_search, uniform_cost_search
from algorithms.aima_algorithms.iterative_deepening import iterative_deepening_search
from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.search_algorithm import SearchAlgorithm
from generators import generate_npuzzle_state
from heuristics.npuzzle import NPuzzleHeuristic
from problems.npuzzle import NPuzzleProblem, NPuzzleState
from constants import *

initial = (
    1, 4, 2,
    6, 5, 0,
    7, 3, 8
)

# 0, 1, 2
# 3, 4, 5
# 6, 7, 8

p = NPuzzleProblem(initial)

h_generator = NPuzzleHeuristic()
manhattan_heuristic = h_generator.create(MANHATTAN_DISTANCE)

best = BestFirstSearch(manhattan_heuristic)  # our best first search
best_t = best_first_graph_search  # aima's best first search


def test_theoretical_best_first_vs_ours():
    """Comparison test between our implementation of best first search and aima's.
    Check that in most cases, our implementation is better or equal.
    Leave some error margin (5%)."""

    states = [NPuzzleState(generate_npuzzle_state(3)) for _ in range(1000)]
    count_worst = 0
    count_better = 0
    for state in states:
        p.initial_state = state
        our_solution_depth = best.search(p).depth
        other_solution_depth = best_t(p, manhattan_heuristic).depth

        count_worst += our_solution_depth > other_solution_depth
        count_better += our_solution_depth < other_solution_depth

    print()
    print(f"{count_better / 1000 * 100}% our algorithm is better")
    print(f"{(1000 - count_worst - count_better) / 1000 * 100}% our algorithm is equal")
    print(f"{count_worst / 1000 * 100}% aima's algorithm is better")

    assert count_worst < 50


breadth = BreadthFirstSearch()          # our breadth first search
breadth_t = breadth_first_tree_search   # aima's breadth first search

it_deepening = IterativeDeepeningSearch()     # our iterative deepening
it_deepening_t = iterative_deepening_search   # aima's iterative deepening

u_cost = UniformCostSearch()     # our uniform cost
u_cost_t = uniform_cost_search   # aima's uniform cost


astar = AStar(manhattan_heuristic)   # our astar
astar_t = astar_search               # aima's astar


easy_states = [
    (4, 3, 1, 0, 7, 2, 6, 8, 5),
    (1, 5, 4, 3, 7, 2, 0, 6, 8),
    (1, 4, 2, 7, 0, 8, 3, 5, 6),
    (1, 2, 5, 4, 0, 8, 3, 6, 7),
    (1, 5, 0, 4, 2, 8, 3, 6, 7)
]

optimal_config = []
for state in easy_states:
    s = NPuzzleState(state)
    optimal_config.append((breadth, breadth_t, None, s))
    optimal_config.append((astar, astar_t, manhattan_heuristic, s))
    optimal_config.append((it_deepening, it_deepening_t, None, s))
    optimal_config.append((u_cost, u_cost_t, None, s))


@pytest.mark.parametrize("ours, theor, heuristic, state", optimal_config)
def test_differential_optimal_algorithms(ours, theor, heuristic, state):
    """Test that the passed algorithms and heuristic (posibly None) encounter
    a solution at the same depth for a given initial state"""
    p.initial_state = state
    our_solution_depth = ours.search(p).depth
    if heuristic is None:
        other_solution_depth = theor(p).depth
    else:
        other_solution_depth = theor(p, heuristic).depth

    assert our_solution_depth == other_solution_depth
