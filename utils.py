import random

from problems.npuzzle import NPuzzleState


def generate_npuzzle_states(size: int, amount: int) -> list[NPuzzleState]:
    return [random_npuzzle_state(size) for _ in range(amount)]


def random_npuzzle_state(n: int) -> NPuzzleState:
    state = NPuzzleState(tuple(random.sample(range(0, n), n)))
    while not state.is_valid():
        state = NPuzzleState(tuple(random.sample(range(0, n), n)))

    return state
