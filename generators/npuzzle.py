import random
from typing import Sequence


def is_solvable(board: Sequence) -> bool:
    """Checks if the given board is solvable."""
    size = len(board)
    inversions = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            if board[i] > board[j] != 0:
                inversions += 1
    return inversions % 2 == 0


def generate_npuzzle_state(dimension: int) -> tuple:
    """Generates a random NPuzzle state."""
    size = dimension * dimension
    board = list(range(0, size))
    random.shuffle(board)
    while not is_solvable(board):
        random.shuffle(board)
    return tuple(board)
