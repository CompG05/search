from algorithms.aima_algorithms.best_first_search import best_first_graph_search


def uniform_cost_search(problem):
    """[Figure 3.14]"""
    return best_first_graph_search(problem, lambda node: node.path_cost)