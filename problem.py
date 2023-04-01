class State:
    """Abstract class for a state representation"""
    def __init__(self, data):
        self.data = data

    @classmethod
    def initial_state(cls) -> 'State':
        raise NotImplementedError

    def is_goal(self) -> bool:
        raise NotImplementedError

    def is_valid(self) -> bool:
        raise NotImplementedError


class Action:
    def __init__(self, cost=1):
        self.cost = cost

    def execute(self, state: State) -> State:
        raise NotImplementedError

    def is_enabled(self, state: State) -> bool:
        raise NotImplementedError


class Problem:
    """Abstract class for a formal representation of a search problem"""
    def __init__(self, initial: State, actions: list[Action]):
        self.initial_state = initial
        self.actions = actions

    def enabled_actions(self, state: State) -> list[Action]:
        return [action for action in self.actions if action.is_enabled(state)]
