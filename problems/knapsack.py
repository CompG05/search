import random

from problems.problem import Problem, Action, State, StateFactory


class KnapsackState(State):
    def __init__(self, data: set[int], weights: list[float], values: list[float], sack_cap: int):
        self.weight = weights
        self.value = values
        self.sack_cap = sack_cap
        super().__init__(data)

    def is_goal(self) -> bool:
        return False

    @property
    def sack_weight(self) -> int:
        w = 0
        for i in self.data:
            w += self.weight[i]
        return w

    @property
    def sack_value(self) -> int:
        w = 0
        for i in self.data:
            w += self.value[i]
        return w

    def is_valid(self) -> bool:
        if len(self.weight) != len(self.value):
            return False
        if self.sack_weight > self.sack_cap:
            return False
        for i in self.data:
            if i not in range(len(self.weight)):
                return False
        return True

    def __str__(self):
        s = "{}"
        content = set([(f"w: {self.weight[i]}", f"v: {self.value[i]}") for i in self.data])
        if len(content) > 0:
            s = str(content)

        return f"Knapsack{s}"

    def __hash__(self):
        return hash((self.data, self.weight, self.value, self.sack_cap))


class KnapsackStateFactory(StateFactory):
    def __init__(self, weights: list[float], values: list[float], sack_cap: int):
        super().__init__()
        self.weights = weights
        self.values = values
        self.sack_cap = sack_cap

    def random(self) -> KnapsackState:
        content = set()
        cap = random.randint(0, self.sack_cap)
        items = list(range(len(self.weights)))
        random.shuffle(items)
        cum_weight = 0

        item = items.pop()
        while items and cum_weight + self.weights[item] <= cap:
            content.add(item)
            cum_weight += self.weights[item]
            item = items.pop()

        return KnapsackState(content, self.weights, self.values, self.sack_cap)


class PutIn(Action):
    def __init__(self, item: int):
        self.item: int = item
        super().__init__(1)

    def execute(self, state: KnapsackState) -> KnapsackState:
        content: set[int] = state.data
        content = content.copy()

        content.add(self.item)
        return KnapsackState(content, state.weight, state.value, state.sack_cap)

    def is_enabled(self, state: KnapsackState) -> bool:
        content: set[int] = state.data
        return state.sack_weight + state.weight[self.item] <= state.sack_cap and self.item not in content

    def __str__(self):
        return f"I{self.item}"

    def __hash__(self):
        return hash(self.item)

    def __eq__(self, other):
        return isinstance(other, PutIn) and self.item == other.item



class KnapsackProblem(Problem):
    def __init__(self, content: set[int], weights: list[float], values: list[float], sack_cap: int):
        state = KnapsackState(content, weights, values, sack_cap)
        if not state.is_valid():
            raise ValueError("Either the content is not valid or lists sizes don't match")

        self.weight = weights
        self.value = values
        self.sack_cap = sack_cap
        self.items = set([i for i in range(len(weights))])
        self.actions = [PutIn(i) for i in self.items]
        super().__init__(state)
        self.state_factory = KnapsackStateFactory(weights, values, sack_cap)


    def is_goal(self, state) -> bool:
        return False

    def enabled_actions(self, state: KnapsackState) -> list[PutIn]:
        return [action for action in self.actions if action.is_enabled(state)]
