import heapq
import random
from typing import Callable, Optional

from algorithms.search_algorithm import SearchAlgorithm, Node
from factories.state_factory import StateFactory
from problems.problem import Problem


class HillClimbing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float]):
        self.heuristic = heuristic
        super().__init__()

    def search(self, problem: Problem) -> Node | None:
        current: Node = Node(problem.initial_state)

        while True:
            neighbors = current.expand(problem)
            if not neighbors:
                return current
            neighbor = max(neighbors, key=(lambda n: self.heuristic(n)))

            if self.heuristic(neighbor) <= self.heuristic(current):
                return current

            current = neighbor


class HillClimbingSideMovements(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], k: int):
        self.heuristic = heuristic
        self.k = k
        super().__init__()

    def search(self, problem: Problem) -> Optional[Node]:
        current: Node = Node(problem.initial_state)
        current_value = self.heuristic(current)
        current_k = self.k

        while True:
            neighbors = [(n, self.heuristic(n)) for n in current.expand(problem)]
            if not neighbors:
                return current
            (best_neighbor, best_neighbor_value) = max(neighbors, key=(lambda p: p[1]))

            if best_neighbor_value < current_value or best_neighbor_value == current_value and current_k == 0:
                return current

            current = best_neighbor

            if best_neighbor_value == current_value:
                current_k -= 1
                best_value_neighbors = [n for (n, v) in neighbors if v == best_neighbor_value]
                current = random.choice(best_value_neighbors)
            else:
                current_k = self.k

            current_value = self.heuristic(current)


class RandomRestartHillClimbing(SearchAlgorithm):
    def __init__(self, problem_name: str, heuristic: Callable[[Node], float]):
        self.problem_name = problem_name
        self.heuristic = heuristic
        super().__init__()

    def search(self, problem: Problem) -> Optional[Node]:
        initial_state = problem.initial_state
        state_factory = problem.initial_state_factory #StateFactory(self.problem_name, state=initial_state)
        hc = HillClimbing(self.heuristic)

        solution = hc.search(problem)

        while not solution.state.is_goal():
            problem.initial_state = state_factory.random()
            solution = hc.search(problem)

        problem.initial_state = initial_state
        return solution
