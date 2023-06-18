from algorithms.informed.astar import AStar
from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.uninformed.breadth_first_search import BreadthFirstSearch, BreadthFirstGraphSearch, \
    BreadthFirstSearchAcyclic
from algorithms.uninformed.depth_first_search import DepthFirstSearch, DepthFirstGraphSearch, DepthFirstSearchAcyclic
from algorithms.uninformed.iterative_deepening_search import IterativeDeepeningSearch
from algorithms.uninformed.uniform_cost_search import UniformCostSearch
from algorithms.uninformed.bidirectional_search import BidirectionalSearch

from problems.graph_problem import GraphProblem
from structures.graph import UndirectedGraph

# uninformed algorithms
BREADTH_FIRST = "breadth_first"
BREADTH_GRAPH = "breadth_graph"
BREADTH_ACYCLIC = "breadth_acyclic"

DEPTH_FIRST = "depth_first"
DEPTH_GRAPH = "depth_graph"
DEPTH_ACYCLIC = "depth_acyclic"

ITERATIVE_DEEPENING = "iterative_deepening"

UNIFORM_COST = "uniform_cost"

BIDIRECTIONAL = "bidirectional"

uninformed_algorithms = {
    BREADTH_FIRST: BreadthFirstSearch,
    # BREADTH_GRAPH: BreadthFirstGraphSearch,
    # BREADTH_ACYCLIC: BreadthFirstSearchAcyclic,

    # DEPTH_FIRST: DepthFirstSearch,
    # DEPTH_GRAPH: DepthFirstGraphSearch,
    DEPTH_ACYCLIC: DepthFirstSearchAcyclic,

    ITERATIVE_DEEPENING: IterativeDeepeningSearch,

    UNIFORM_COST: UniformCostSearch,

    BIDIRECTIONAL: BidirectionalSearch
}

# informed algorithms

GREEDY_BEST_FIRST = "greedy_best_first"
A_STAR = "a_star"

informed_algorithms = {
    GREEDY_BEST_FIRST: BestFirstSearch,
    A_STAR: AStar
}

# problems
NPUZZLE = "npuzzle"
NQUEENS = "nqueens"
ROMANIA = "romania"

problems = [NPUZZLE, NQUEENS, ROMANIA]
invertible_problems = [NPUZZLE, ROMANIA]

# npuzzle heuristics
WRONG_TILES = "wrong_tiles"
MANHATTAN_DISTANCE = "manhattan_distance"
GASCHNIG_DISTANCE = "gaschnig_distance"
WRONG_ROW_COL = "wrong_row_col"

# nqueens heuristic
N_CONFLICTS = "n_conflicts"

# romania heuristic
LINEAR_DISTANCE = "linear_distance"

heuristics = {
    NPUZZLE: [WRONG_TILES, MANHATTAN_DISTANCE, GASCHNIG_DISTANCE, WRONG_ROW_COL],
    NQUEENS: [N_CONFLICTS],
    ROMANIA: [LINEAR_DISTANCE],
}

# Romania problem

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

romania_locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))


def PathToBucharest(initial):
    return GraphProblem(romania_map, initial, 'Bucharest')
