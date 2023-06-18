import math

from problems.problem import Problem, State, Action


class NQueensState(State):
    def __init__(self, data: tuple):
        self.dimension = len(data)
        super().__init__(data)

    def is_goal(self):
        return self.n_conflicts() == 0

    @staticmethod
    def conflicted(row1, col1, row2, col2):
        return (row1 == row2 or
                col1 == col2 or
                abs(row1 - row2) == abs(col1 - col2))

    def n_conflicts(self):
        occupied_cells = list(enumerate(self.data))
        conflicts = 0

        for (c1, r1) in occupied_cells:
            for (c2, r2) in occupied_cells[c1 + 1:]:
                conflicts += self.conflicted(r1, c1, r2, c2)

        return conflicts

    def move_queen(self, column: int, delta: int) -> 'NQueensState':
        """Returns a new state with the column-nth queen moved by delta"""
        board = list(self.data)
        board[column] = (board[column] + delta) % self.dimension
        return NQueensState(tuple(board))

    def is_valid(self):
        return all([self.data[i] in range(self.dimension) for i in range(self.dimension)])

    def __repr__(self):
        return str(self.data)


class NQueensAction(Action):
    def __init__(self, column: int, new_row: int):
        super().__init__()
        self.column = column
        self.new_row = new_row

    def execute(self, state: NQueensState) -> NQueensState:
        return state.move_queen(self.column, self.new_row)

    def is_enabled(self, state: NQueensState) -> bool:
        return True

    def __hash__(self):
        return hash((self.column, self.new_row))

    def __eq__(self, other):
        return isinstance(other, NQueensAction) and self.column == other.column and self.new_row == other.new_row

    def __repr__(self):
        return f"col[{self.column}]->row[{self.new_row}]"


class NQueensProblem(Problem):
    def __init__(self, initial: tuple | NQueensState):
        if isinstance(initial, tuple):
            initial = NQueensState(initial)
        super().__init__(initial)

    def enabled_actions(self, state: NQueensState) -> list[Action]:
        return [NQueensAction(column, new_row) for column in range(state.dimension)
                for new_row in range(state.dimension) if new_row != state.data[column]]
