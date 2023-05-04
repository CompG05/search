import pytest

from algorithms.solver import Solver
from problems.graph_problem import GraphProblem, Edge, Vertex
from constants import *

p = GraphProblem(romania_map, 'Arad', 'Bucharest')


def test_enabled_actions():
    Sibiu = Vertex('Sibiu', 'Bucharest')
    expected = [Edge(romania_map, 'Sibiu', dest)
                for dest in ['Arad', 'Oradea', 'Fagaras', 'Rimnicu']]
    actual = p.enabled_actions(Sibiu)

    assert len(actual) == len(expected) \
           and all([a in expected for a in actual])


def test_bidirectional_solution():
    Arad = Vertex('Arad', 'Bucharest')
    Sibiu = Vertex('Sibiu', 'Bucharest')
    Fagaras = Vertex('Fagaras', 'Bucharest')
    Bucharest = Vertex('Bucharest', 'Bucharest')
    expected = [Arad, Sibiu, Fagaras, Bucharest]
    solver = Solver(ROMANIA, ("Arad", "Bucharest"), BIDIRECTIONAL, None)
    solution = solver.solve()
    actual = solution.path

    assert actual == expected


uninformed_search_config = [(alg, None) for alg in uninformed_algorithms if alg != DEPTH_FIRST]
informed_search_config = [(alg, h) for alg in informed_algorithms for h in heuristics[ROMANIA]]


@pytest.mark.parametrize("algorithm, heuristic", informed_search_config + uninformed_search_config)
def test_informed_search(algorithm, heuristic):
    solver = Solver(ROMANIA, ('Arad', 'Bucharest'), algorithm, heuristic)
    solution = solver.solve()

    assert solution.final_state == Vertex("Bucharest", "Bucharest")
