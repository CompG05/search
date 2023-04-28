import pytest

from algorithms.solver import Solver
from constants import informed_algorithms, npuzzle_heuristics, uninformed_algorithms, DEPTH_GRAPH, DEPTH_ACYCLIC, \
    DEPTH_FIRST
from problems.nqueens import NQueensState

initial = NQueensState((3, 0, 2, 0, 5, 7, 1, 3))

conflicted_config = [
    (4, 0, 7, 3, True),
    (7, 1, 1, 7, True),
    (1, 3, 1, 8, True),
    (1, 4, 5, 4, True),
    (0, 0, 2, 1, False),
]


@pytest.mark.parametrize("row1, col1, row2, col2, expected", conflicted_config)
def test_conflicted(row1, col1, row2, col2, expected):
    assert NQueensState.conflicted(row1, col1, row2, col2) == expected


n_conflicts_config = [
    (NQueensState((4, 2, 0, 6, 1, 7, 5, 3)), 0),
    (NQueensState((4, 2, 1, 6, 1, 7, 5, 3)), 3),
    (NQueensState((4, 2, 1, 2, 1, 7, 5, 3)), 7),
    (NQueensState((4, 2, 1, 2, 1, 7, 5, 2)), 9),
    (NQueensState((4, 2, 0, 6, 1, 7, 5, 1)), 1)
]


@pytest.mark.parametrize("state, expected", n_conflicts_config)
def test_n_conflicts(state, expected):
    assert state.n_conflicts() == expected


move_queen_config = [
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), 5, 1, NQueensState((0, 1, 2, 3, 4, 6, 6, 7))),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), 0, 1, NQueensState((1, 1, 2, 3, 4, 5, 6, 7))),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), 7, 1, NQueensState((0, 1, 2, 3, 4, 5, 6, 0))),
]


@pytest.mark.parametrize("state, column, delta, expected", move_queen_config)
def test_move_queen(state, column, delta, expected):
    assert state.move_queen(column, delta) == expected


is_goal_config = [
    (NQueensState((6, 4, 2, 0, 5, 7, 1, 3)), True),
    (NQueensState((4, 2, 0, 6, 1, 7, 5, 1)), False)
]


@pytest.mark.parametrize("state, expected", is_goal_config)
def test_is_goal(state, expected):
    assert state.is_goal() == expected


is_valid_config = [
    (NQueensState((0, 1, 2, 3, 4, 5, 6, -1)), False),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 8)), False),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), True),
    (NQueensState((0, 0, 0, 0, 0, 0, 0, 0)), True)
]


@pytest.mark.parametrize("state, expected", is_valid_config)
def test_is_valid(state, expected):
    assert state.is_valid() == expected


algorithms_config = [(alg, h) for alg in informed_algorithms for h in npuzzle_heuristics] \
                    + [(alg, None) for alg in uninformed_algorithms
                       if alg not in [DEPTH_GRAPH, DEPTH_ACYCLIC, DEPTH_FIRST]]


@pytest.mark.parametrize("algorithm, heuristic", algorithms_config)
def test_solution(algorithm, heuristic):
    solver = Solver("NQueens", initial, algorithm, heuristic)
    solution = solver.solve()

    assert solution.final_state.n_conflicts() == 0
