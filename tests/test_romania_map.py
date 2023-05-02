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
