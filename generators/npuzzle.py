import random
import math
from typing import Sequence


def num_inversions(board: Sequence) -> int:
    size = len(board)
    inversions = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            if board[i] > board[j] != 0:
                inversions += 1
    return inversions


def is_solvable(board: Sequence) -> bool:
    """Checks if the given board is solvable."""
    dim = math.sqrt(len(board))
    if not float.is_integer(dim):
        return False

    dim = int(dim)
    n_inv = num_inversions(board)
    if dim % 2 != 0:
        return n_inv % 2 == 0
    else:
        blank_position = board.index(0)
        blank_row = blank_position / dim
        return blank_row % 2 != n_inv % 2


def generate_npuzzle_state(dimension: int) -> tuple:
    """Generates a random NPuzzle state."""
    size = dimension * dimension
    board = list(range(0, size))
    random.shuffle(board)
    while not is_solvable(board):
        random.shuffle(board)
    return tuple(board)
