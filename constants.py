from algorithms.informed.astar import AStar
from algorithms.informed.best_first_search import BestFirstSearch
from algorithms.uninformed.breadth_first_search import BreadthFirstSearch, BreadthFirstGraphSearch, \
    BreadthFirstSearchAcyclic
from algorithms.uninformed.depth_first_search import DepthFirstSearch, DepthFirstGraphSearch, DepthFirstSearchAcyclic
from algorithms.uninformed.iterative_deepening_search import IterativeDeepeningSearch
from algorithms.uninformed.uniform_cost_search import UniformCostSearch

# uninformed algorithms
BREADTH_FIRST = "breadth_first"
BREADTH_GRAPH = "breadth_graph"
BREADTH_ACYCLIC = "breadth_acyclic"

DEPTH_FIRST = "depth_first"
DEPTH_GRAPH = "depth_graph"
DEPTH_ACYCLIC = "depth_acyclic"

ITERATIVE_DEEPENING = "iterative_deepening"

UNIFORM_COST = "uniform_cost"

uninformed_algorithms = {
    BREADTH_FIRST: BreadthFirstSearch,
    BREADTH_GRAPH: BreadthFirstGraphSearch,
    BREADTH_ACYCLIC: BreadthFirstSearchAcyclic,

    DEPTH_FIRST: DepthFirstSearch,
    DEPTH_GRAPH: DepthFirstGraphSearch,
    DEPTH_ACYCLIC: DepthFirstSearchAcyclic,

    ITERATIVE_DEEPENING: IterativeDeepeningSearch,

    UNIFORM_COST: UniformCostSearch
}

# informed algorithms

GREEDY_BEST_FIRST = "greedy_best_frist"
A_STAR = "a_star"

informed_algorithms = {
    GREEDY_BEST_FIRST: BestFirstSearch,
    A_STAR: AStar
}

# problems
NPUZZLE = "npuzzle"
NQUEENS = "nqueens"
ROMANIA = "romania"

# npuzzle heuristics
WRONG_TILES = "wrong_tiles"
MANHATTAN_DISTANCE = "manhattan_distance"

npuzzle_heuristics = [WRONG_TILES, MANHATTAN_DISTANCE]
