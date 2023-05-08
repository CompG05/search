from algorithms.aima_algorithms.best_first_search import best_first_graph_search


def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))
