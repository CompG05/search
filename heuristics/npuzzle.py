from typing import Callable

from algorithms.search_algorithm import Node
from constants import WRONG_TILES, MANHATTAN_DISTANCE


class NPuzzleHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == WRONG_TILES:
            return self.wrong_tiles
        if heuristic.lower() == MANHATTAN_DISTANCE:
            return self.manhattan_distance
        else:
            raise ValueError("Heuristic not found")

    @staticmethod
    def wrong_tiles(node: Node) -> float:
        state = node.state
        return sum(1 for i, j in zip(state.data, range(0, state.size)) if i != j)

    @staticmethod
    def manhattan_distance(node: Node) -> float:
        state = node.state
        board = list(state.data)
        dim = state.dimension
        manhattan_distance = 0
        for i in range(0, len(board)):  # i indicates the position where piece i should be in the goal state
            i_goal_row = i / dim
            i_goal_col = i % dim

            i_current_pos = board.index(i)
            i_current_row = i_current_pos / dim
            i_current_col = i_current_pos / dim

            manhattan_distance += abs(i_goal_row - i_current_row) + abs(i_goal_col - i_current_col)
        return manhattan_distance
