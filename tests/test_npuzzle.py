import pytest

from algorithms.solver import Solver
from constants import *
from problems.npuzzle import NPuzzleProblem, NPuzzleState, RightMove, LeftMove, UpMove, DownMove

initial = (
    1, 4, 2,
    6, 5, 0,
    7, 3, 8
)

p = NPuzzleProblem(initial)

L = LeftMove()
R = RightMove()
U = UpMove()
D = DownMove()

can_move_config = [
    (NPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8)).can_move_up(), True),
    (NPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8)).can_move_up(), False),
    (NPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8)).can_move_left(), True),
    (NPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8)).can_move_left(), False),
    (NPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8)).can_move_right(), True),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)).can_move_right(), False),
    (NPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8)).can_move_down(), True),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)).can_move_down(), False)
]


@pytest.mark.parametrize("actual, expected", can_move_config)
def test_can_move(actual, expected):
    assert actual == expected


state_is_goal_config = [
    (NPuzzleState((4, 7, 5, 6, 3, 8, 2, 1, 0)), False),
    (NPuzzleState(tuple(range(0, 9))), True),
    (NPuzzleState(tuple(reversed(range(0, 16)))), False)
]


@pytest.mark.parametrize("state, expected", state_is_goal_config)
def test_state_is_goal(state, expected):
    assert p.is_goal(state) == expected


enabled_actions_config = [
    (NPuzzleState((0, 6, 5, 7, 4, 8, 3, 1, 2)), (R, D)),
    (NPuzzleState((2, 6, 5, 7, 4, 8, 3, 1, 0)), (L, U)),
    (NPuzzleState((2, 6, 5, 7, 0, 4, 3, 1, 8)), (L, U, R, D)),
]


@pytest.mark.parametrize("state, expected", enabled_actions_config)
def test_enabled_actions(state, expected):
    assert set(p.enabled_actions(state)) == set(expected)


algorithms_config = [(alg, h) for alg in informed_algorithms for h in heuristics[NPUZZLE]] \
                    + [(alg, None) for alg in uninformed_algorithms
                       if alg not in [DEPTH_GRAPH, DEPTH_ACYCLIC, DEPTH_FIRST]]


@pytest.mark.parametrize("algorithm, heuristic", algorithms_config)
def test_solution(algorithm, heuristic):
    size = p.initial_state.size
    solver = Solver("NPuzzle", initial, algorithm, heuristic)
    solution = solver.solve()

    assert solution.final_state == NPuzzleState(tuple(range(0, size)))
