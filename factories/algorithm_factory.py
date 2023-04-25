from typing import Callable

from algorithms.search_algorithm import Node
from constants import *


class AlgorithmFactory:
    @staticmethod
    def create(algorithm: str, heuristic: Callable[[Node], float]):
        if algorithm in uninformed_algorithms:
            if heuristic is not None:
                raise ValueError(f"Passed a heuristic for the uninformed algorithm {algorithm}")

            return uninformed_algorithms[algorithm]()

        elif algorithm in informed_algorithms:
            if heuristic is None:
                raise ValueError(f"{algorithm} algorithm requires a heuristic, passed None")

            return informed_algorithms[algorithm](heuristic)

        else:
            raise ValueError(f"Algorithm '{algorithm}' not found")


algorithm_factory = AlgorithmFactory()
