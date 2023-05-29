import heapq
import random
import sys
from typing import Callable, Optional

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class HillClimbing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float]):
        self.heuristic = heuristic
        super().__init__()

    def search(self, problem: Problem) -> Node:
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

    def search(self, problem: Problem) -> Node:
        current: Node = Node(problem.initial_state)
        current_value = self.heuristic(current)
        current_k = self.k

        while True:
            neighbors = []
            best_neighbor = None
            best_neighbor_value = -sys.float_info.max
            best_neighbors = []

            for n in current.expand(problem):
                neighbors.append(n)
                v = self.heuristic(n)
                if v > best_neighbor_value:
                    best_neighbor_value = v
                    best_neighbor = n
                    best_neighbors = [n]
                elif v == best_neighbor_value:
                    best_neighbors.append(n)

            if not neighbors:
                return current

            if best_neighbor_value < current_value or best_neighbor_value == current_value and current_k == 0:
                return current

            current = best_neighbor

            if best_neighbor_value == current_value:
                current_k -= 1
                current = random.choice(best_neighbors)
            else:
                current_k = self.k

            current_value = self.heuristic(current)


class RandomRestartHillClimbing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], exhaustive: bool = True, max_iterations: int = 50):
        self.heuristic = heuristic
        self.exhaustive = exhaustive
        self.max_iterations = max_iterations
        super().__init__()

    def search(self, problem: Problem) -> Node:
        if self.exhaustive:
            return self.exhaustive_search(problem)
        else:
            return self.non_exhaustive_search(problem)

    def exhaustive_search(self, problem: Problem) -> Node:
        state_factory = problem.state_factory
        hc = HillClimbing(self.heuristic)

        solution = hc.search(problem)

        while not solution.state.is_goal():
            problem.initial_state = state_factory.random()
            solution = hc.search(problem)

        return solution

    def non_exhaustive_search(self, problem: Problem) -> Node:
        initial_state = problem.initial_state
        state_factory = problem.state_factory
        hc = HillClimbing(self.heuristic)

        solutions = [hc.search(problem)]

        while not solutions[-1].state.is_goal() and len(solutions) < self.max_iterations:
            problem.initial_state = state_factory.random()
            solutions.append(hc.search(problem))

        problem.initial_state = initial_state
        return max(solutions, key=(lambda n: self.heuristic(n)))

