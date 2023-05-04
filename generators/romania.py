import random

from constants import romania_map


def generate_romania_state() -> tuple:
    return tuple(random.choices(romania_map.nodes, k=2))
