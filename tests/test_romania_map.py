from algorithm.solver import Solver
from algorithm.uninformed.breadth_first_search import BreadthFirstSearch
from problems.graph_problem import GraphProblem, Transition, GraphNode
from structures.graph import UndirectedGraph

romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

p = GraphProblem(romania_map, 'Arad', 'Bucharest')


def test_enabled_actions():
    expected = [Transition(romania_map, 'Sibiu', dest)
                for dest in ['Arad', 'Oradea', 'Fagaras', 'Rimnicu']]
    actual = p.enabled_actions('Sibiu')

    assert len(actual) == len(expected) \
        and all([a in expected for a in actual])