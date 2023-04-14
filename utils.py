import random

from problems.npuzzle import NPuzzleState, NPuzzleProblem


def generate_npuzzle_states(size: int, amount: int) -> list[NPuzzleState]:
    return [random_npuzzle_state(size) for _ in range(amount)]


def random_npuzzle_state(n: int, d: int = 9) -> NPuzzleState:
    state = NPuzzleState(tuple(range(0, n)))
    p = NPuzzleProblem(state)
    for _ in range(0, d):
        actions = p.enabled_actions(state)
        action = random.choice(actions)
        state = action.execute(state)

    return state
