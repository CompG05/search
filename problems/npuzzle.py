import math
from problems.problem import State, Action, Problem


class NPuzzleState(State):
    def __init__(self, data: tuple[int, ...]):
        self.size = len(data)
        self.dimension = int(math.sqrt(self.size))
        super().__init__(data)

    def is_goal(self) -> bool:
        return self.data == tuple(range(0, self.size))

    def find_blank_square(self) -> int:
        print(self.data)
        return self.data.index(0)

    def can_move_left(self, index: int) -> bool:
        return index % self.dimension != 0

    def __repr__(self):
        return str(self.data)

    @staticmethod
    def get_left(index: int) -> int:
        return index - 1

    @staticmethod
    def get_right(index: int) -> int:
        return index + 1

    def can_move_right(self, index: int) -> bool:
        return index % self.dimension != self.dimension - 1

    def can_move_up(self, index: int) -> bool:
        return index >= self.dimension

    def get_up(self, index: int) -> int:
        return index - self.dimension

    def can_move_down(self, index: int) -> bool:
        return index < self.size - self.dimension

    def get_down(self, index: int) -> int:
        return index + self.dimension

    def is_valid(self) -> bool:
        return NotImplementedError


class SwappableAction(Action):
    @staticmethod
    def swap(state: NPuzzleState, i: int, j: int) -> NPuzzleState:
        board = list(state.data)
        board[i], board[j] = board[j], board[i]
        return NPuzzleState(tuple(board))

    def __hash__(self):
        return hash(self.__class__.__name__)

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __repr__(self):
        return self.__class__.__name__[0]


class LeftMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        blank_index = state.find_blank_square()
        left_index = state.get_left(blank_index)
        return self.swap(state, blank_index, left_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        blank_index = state.find_blank_square()
        return state.can_move_left(blank_index)


class RightMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        blank_index = state.find_blank_square()
        right_index = state.get_right(blank_index)
        return self.swap(state, blank_index, right_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        blank_index = state.find_blank_square()
        return state.can_move_right(blank_index)


class UpMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        blank_index = state.find_blank_square()
        up_index = state.get_up(blank_index)
        return self.swap(state, blank_index, up_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        blank_index = state.find_blank_square()
        return state.can_move_up(blank_index)


class DownMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        blank_index = state.find_blank_square()
        down_index = state.get_down(blank_index)
        return self.swap(state, blank_index, down_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        blank_index = state.find_blank_square()
        return state.can_move_down(blank_index)


class NPuzzleProblem(Problem):
    def __init__(self, initial: NPuzzleState | tuple[int, ...]):
        self.actions = [UpMove(),  RightMove(), DownMove(), LeftMove()]
        if isinstance(initial, tuple):
            initial = NPuzzleState(initial)
        super().__init__(initial)

    def enabled_actions(self, state: NPuzzleState) -> list[SwappableAction]:
        return [action for action in self.actions if action.is_enabled(state)]
