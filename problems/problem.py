class Action:
    def __init__(self, cost=1):
        self.cost = cost

    def execute(self, state) -> object:
        raise NotImplementedError

    def is_enabled(self, state) -> bool:
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError


class Problem:
    """Abstract class for a formal representation of a search problem"""
    def __init__(self, initial):
        self.initial_state = initial

    def is_goal(self, state) -> bool:
        raise NotImplementedError

    def enabled_actions(self, state) -> list[Action]:
        raise NotImplementedError
