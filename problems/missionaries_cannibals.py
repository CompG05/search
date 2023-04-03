from problems.problem import Action, Problem


class MCAction(Action):
    def __init__(self, m: int, c: int, cost=1):
        """m: number of missionaries, c: number of cannibals"""
        self.m = m
        self.c = c
        super().__init__(cost)

    def execute(self, state) -> object:
        m1, c1, m2, c2 = state
        return m1 - self.m, c1 - self.c, m2 + self.m, c2 + self.c

    def is_enabled(self, state) -> bool:
        m1, c1, m2, c2 = state
        enough_to_move = m1 >= self.m and c1 >= self.c
        # there will never be more cannibals than missionaries on either side
        can_move = (m1 - self.m >= c1 - self.c or m1 - self.m == 0) \
            and (m2 + self.m >= c2 + self.c or m2 + self.m == 0)
        return enough_to_move and can_move

    def __hash__(self):
        return hash((self.m, self.c))

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c

    def __repr__(self):
        return f'<{self.m}M,{self.c}C>'


class MCProblem(Problem):
    def __init__(self, initial):
        m1, c1, m2, c2 = initial
        self.missionaries = m1 + m2
        self.cannibals = c1 + c2
        self.actions = []

        for m in range(3):
            for c in range(3):
                if m + c in [1, 2]: # Boat carries 1 or 2 people
                    self.actions.append(MCAction(m, c))

        super().__init__(initial)

    def is_goal(self, state) -> bool:
        return state == (0, 0, self.missionaries, self.cannibals)

    def enabled_actions(self, state) -> list[Action]:
        return [action for action in self.actions if action.is_enabled(state)]
