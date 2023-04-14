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


class InvertibleAction(Action):
    def inverse(self) -> 'InvertibleAction':
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


class InvertibleProblem(Problem):
    def __init__(self, initial, goal=None):
        self.goal = goal
        super().__init__(initial)

    def is_goal(self, state) -> bool:
        return state == self.goal

    def inverse(self) -> 'InvertibleProblem':
        return self.__class__(self.goal, self.initial_state)


class InstrumentedProblem(Problem):
    def __init__(self, problem):
        self.problem = problem
        self.nodes = 1
        self.visited = 0
        self.max_nodes_in_frontier = 0
        super().__init__(problem.initial_state)

    @property
    def nodes_in_frontier(self):
        return self.nodes - self.visited

    @property
    def branching_factor(self):
        return (self.nodes - 1) / self.visited

    def reset(self):
        self.nodes = 1
        self.visited = 0
        self.max_nodes_in_frontier = 0

    def inverse(self) -> 'InstrumentedProblem':
        return InstrumentedProblem(self.problem.inverse())

    def is_goal(self, state):
        self.visited += 1
        return self.problem.is_goal(state)

    def result(self, state, action):
        self.nodes += 1
        self.max_nodes_in_frontier = max((self.max_nodes_in_frontier, self.nodes_in_frontier))
        return self.problem.result(state, action)

    def enabled_actions(self, state) -> list[Action]:
        actions = self.problem.enabled_actions(state)
        return actions
