import pytest

from algorithms.local.hill_climbing import HillClimbingSideMovements, HillClimbing, RandomRestartHillClimbing
from constants import NQUEENS, INVERSE_N_CONFLICTS
from generators import generate_nqueens_state
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensState, NQueensProblem

p = NQueensProblem(generate_nqueens_state(8))
h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)

rating_config = [
    (HillClimbing(h), 0.14),
    (HillClimbingSideMovements(h, 100), 0.94),
]


@pytest.mark.parametrize("algorithm, solution_rate", rating_config)
def test_sideways_hill_climbing_nqueens(algorithm, solution_rate):
    i = 1000

    states = [NQueensState(generate_nqueens_state(8)) for _ in range(i)]

    solved = 0
    for state in states:
        p.initial_state = state
        result = algorithm.search(p)
        solved += result.state.is_goal()

    actual_solution_rate = solved / i
    print("Solved:", solved)

    assert solution_rate - 0.05 <= actual_solution_rate <= solution_rate + 0.05


def test_random_restart_nqueens():
    algorithm = RandomRestartHillClimbing(NQUEENS, h)
    solution = algorithm.search(p)
    assert solution.state.is_goal()
