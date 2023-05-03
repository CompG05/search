import random


def generate_nqueens_state(dimension: int) -> tuple:
    state = [random.randrange(dimension) for _ in range(dimension)]
    return tuple(state)