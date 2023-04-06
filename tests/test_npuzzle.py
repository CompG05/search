import pytest
from problems.npuzzle import NPuzzleProblem, NPuzzleState, RightMove, LeftMove, UpMove, DownMove
from algorithm.solver import Solver
from algorithm.uninformed.breadth_first_search import breadth_first_search
from algorithm.uninformed.depth_first_search import depth_first_graph_search


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


algorithms = [breadth_first_search]


@pytest.mark.parametrize("algorithm", algorithms)
def test_solution(algorithm):
    size = p.initial_state.size
    solver = Solver(p, algorithm)
    solution = solver.solve()

    print("algorithm: ", algorithm.__class__.__name__)
    print("final state: ", solution.final_state)
    print("path: ", solution.path)
    print("action sequence: ", solution.action_sequence)
    print("path cost: ", solution.path_cost)
    assert solution.final_state == NPuzzleState(tuple(range(0, size)))
    assert False
