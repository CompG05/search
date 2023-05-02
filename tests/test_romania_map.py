import pytest

from algorithms.solver import Solver
from problems.graph_problem import GraphProblem, Edge
from constants import *

p = GraphProblem(romania_map, 'Arad', 'Bucharest')


def test_enabled_actions():
    expected = [Edge(romania_map, 'Sibiu', dest)
                for dest in ['Arad', 'Oradea', 'Fagaras', 'Rimnicu']]
    actual = p.enabled_actions('Sibiu')

    print(actual)
    assert len(actual) == len(expected) \
        and all([a in expected for a in actual])


def test_bidirectional_solution():
    expected = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
    solver = Solver(ROMANIA, 'Arad', BIDIRECTIONAL, None)
    solution = solver.solve()
    actual = solution.path

    assert actual == expected


uninformed_search_config = [(alg, None) for alg in uninformed_algorithms if alg != DEPTH_FIRST]
informed_search_config = [(alg, h) for alg in informed_algorithms for h in heuristics[ROMANIA]]


@pytest.mark.parametrize("algorithm, heuristic", informed_search_config + uninformed_search_config)
def test_informed_search(algorithm, heuristic):
    solver = Solver(ROMANIA, 'Arad', algorithm, heuristic)
    solution = solver.solve()

    assert solution.final_state == "Bucharest"
