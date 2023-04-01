from problems.problem import State, Action


class MCState(State):
    def __init__(self, data: tuple[int, int, int, int]):
        m1, c1, m2, c2 = data
        self.missionaries = m1 + m2
        self.cannibals = c1 + c2
        super().__init__(data)

    def is_goal(self) -> bool:
        return self.data == (0, 0, self.missionaries, self.cannibals)

    def is_valid(self) -> bool:
        m1, c1, m2, c2 = self.data
        return m1 >= c1 and m2 >= c2


class MCAction(Action):
    def __init__(self, m: int, c: int, cost=1):
        """m: number of missionaries, c: number of cannibals"""
        self.m = m
        self.c = c
        super().__init__(cost)

    def execute(self, state: State) -> State:
        m1, c1, m2, c2 = state.data
        return MCState((m1 - self.m, c1 - self.c, m2 + self.m, c2 + self.c))

    def is_enabled(self, state: State) -> bool:
        m1, c1, m2, c2 = state.data
        enough_to_move = m1 >= self.m and c1 >= self.c
        # there will never be more cannibals than missionaries on either side
        can_move = (m1 - self.m >= c1 - self.c or m1 - self.m == 0) and (m2 + self.m >= c2 + self.c or m2 + self.m == 0)
        return enough_to_move and can_move
