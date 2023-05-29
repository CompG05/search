import pytest

from algorithms.local.hill_climbing import HillClimbingSideMovements, HillClimbing, RandomRestartHillClimbing
from constants import *
from generators import generate_nqueens_state
from heuristics.knapsack import KnapsackHeuristic
from heuristics.nqueens import NQueensHeuristic
from problems.knapsack import KnapsackProblem, KnapsackState
from problems.nqueens import NQueensState, NQueensProblem

p = NQueensProblem(generate_nqueens_state(8))
h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
h2 = KnapsackHeuristic().create(ACCUM_VALUE)


hc_algorithms = [HillClimbing(h), HillClimbingSideMovements(h, 100), RandomRestartHillClimbing(h, exhaustive=True)]


def test_hill_climbing_nqueens():
    i = 100

    state_factory = p.state_factory
    states = [state_factory.random() for _ in range(i)]

    for hc in hc_algorithms:
        solved = 0
        for state in states:
            p.initial_state = state
            result = hc.search(p)
            solved += result.state.is_goal()

        actual_solution_rate = solved / i
        print(f"\n{hc.__class__.__name__} solution rate: {actual_solution_rate}")


def test_random_restart_exhaustive_nqueens():
    algorithm = RandomRestartHillClimbing(h)
    solution = algorithm.search(p)
    assert solution.state.is_goal()

def test_random_restart_non_exhaustive_knapsack():
    weights = [5, 10, 30, 15, 40, 25, 65]
    values = [1, 2, 7, 3, 9, 6, 10]
    cap = 75
    algorithm = RandomRestartHillClimbing(h2, False, 10)
    problem = KnapsackProblem(set(), weights, values, cap)
    print("\n", algorithm.search(problem).state)

