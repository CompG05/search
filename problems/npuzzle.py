import math

from problems.problem import State, InvertibleAction, InvertibleProblem


class NPuzzleState(State):
    def __init__(self, data: tuple):
        self.size = len(data)
        self.dimension = int(math.sqrt(self.size))
        super().__init__(data)
        self.blank_index = self.find_blank_square()

    def is_goal(self) -> bool:
        return self.data == tuple(range(0, self.size))

    def find_blank_square(self) -> int:
        return self.data.index(0)

    def can_move_left(self) -> bool:
        return self.blank_index % self.dimension != 0

    @staticmethod
    def get_left(index: int) -> int:
        return index - 1

    @staticmethod
    def get_right(index: int) -> int:
        return index + 1

    def can_move_right(self) -> bool:
        return self.blank_index % self.dimension != self.dimension - 1

    def can_move_up(self) -> bool:
        return self.blank_index >= self.dimension

    def get_up(self, index: int) -> int:
        return index - self.dimension

    def can_move_down(self) -> bool:
        return self.blank_index < self.size - self.dimension

    def get_down(self, index) -> int:
        return index + self.dimension

    def is_valid(self) -> bool:
        return self.is_solvable() and float.is_integer(math.sqrt(self.size))

    def is_solvable(self) -> bool:
        inversions = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.data[i] > self.data[j] != 0:
                    inversions += 1
        return inversions % 2 == 0

    def __repr__(self):
        return str(self.data)


class SwappableAction(InvertibleAction):
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

    def inverse(self) -> 'SwappableAction':
        raise NotImplementedError


class LeftMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        left_index = state.get_left(state.blank_index)
        return self.swap(state, state.blank_index, left_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        return state.can_move_left()

    def inverse(self) -> 'SwappableAction':
        return RightMove()


class RightMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        right_index = state.get_right(state.blank_index)
        return self.swap(state, state.blank_index, right_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        return state.can_move_right()

    def inverse(self) -> 'SwappableAction':
        return LeftMove()


class UpMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        up_index = state.get_up(state.blank_index)
        return self.swap(state, state.blank_index, up_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        return state.can_move_up()

    def inverse(self) -> 'SwappableAction':
        return DownMove()


class DownMove(SwappableAction):
    def execute(self, state: NPuzzleState) -> NPuzzleState:
        down_index = state.get_down(state.blank_index)
        return self.swap(state, state.blank_index, down_index)

    def is_enabled(self, state: NPuzzleState) -> bool:
        return state.can_move_down()

    def inverse(self) -> 'SwappableAction':
        return UpMove()


class NPuzzleProblem(InvertibleProblem):
    def __init__(self, initial: tuple, goal: tuple = None):
        self.actions = [UpMove(),  LeftMove(), DownMove(), RightMove()]
        if isinstance(initial, tuple):
            initial = NPuzzleState(initial)
        super().__init__(initial, goal or NPuzzleState(tuple(range(0, initial.size))))

    def enabled_actions(self, state: NPuzzleState) -> list[SwappableAction]:
        return [action for action in self.actions if action.is_enabled(state)]
