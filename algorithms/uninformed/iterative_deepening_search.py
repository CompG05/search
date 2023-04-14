from algorithms.search_algorithm import SearchAlgorithm, Node
from algorithms.uninformed.depth_limited_search import DepthLimitedSearch
from problems.problem import Problem


class IterativeDeepeningSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        result = None
        depth = 0

        while result is None:
            result = DepthLimitedSearch(depth).search(problem)
            depth += 1

        return result


iterative_deepening_search = IterativeDeepeningSearch()
