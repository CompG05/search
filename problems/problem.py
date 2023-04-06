class State:
    def __init__(self, data):
        self.data = data

    def is_goal(self) -> bool:
        raise NotImplementedError

    def is_valid(self) -> bool:
        raise NotImplementedError

    def __eq__(self, other: 'State'):
        return self.data == other.data and isinstance(other, type(self))

    def __hash__(self):
        return hash(self.data)


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
        return state.is_goal()

    def result(self, state, action: Action) -> object:
        return action.execute(state)

    def enabled_actions(self, state) -> list[Action]:
        raise NotImplementedError
