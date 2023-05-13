import pytest

from problems.knapsack import PutIn, TakeOut, KnapsackState, KnapsackProblem

#          0   1   2   3   4   5   6
weights = [5, 10, 30, 15, 40, 25, 50]
values = [1, 2, 7, 3, 9, 6, 12]
cap = 75


def s(content):
    return KnapsackState(content, weights, values, cap)


action_is_enabled_config = [
    (PutIn(1), s({6, 5}), False),
    (PutIn(2), s({6}), False),
    (PutIn(6), s({1, 3}), True),
    (PutIn(2), s({1, 2, 3}), False),
    (TakeOut(1), s({}), False),
    (TakeOut(3), s({6, 5}), False),
    (TakeOut(1), s({1}), True),
    (TakeOut(2), s({1, 2, 3}), True),
]


@pytest.mark.parametrize("action, state, expected", action_is_enabled_config)
def test_action_is_enabled(action, state, expected):
    return action.is_enabled(state) == expected


execute_action_config = [
    (PutIn(6), s({1, 3}), s({1, 3, 6})),
    (PutIn(1), s({2, 4}), s({1, 2, 4})),
    (TakeOut(1), s({1, 2}), s({2})),
    (TakeOut(6), s({1, 6}), s({1})),
    (TakeOut(3), s({3}), s({})),
]


@pytest.mark.parametrize("action, state, expected", execute_action_config)
def test_action_execute(action, state, expected):
    return action.execute(state) == expected


enabled_actions_config = [
    (s({6, 5}), [PutIn(i) for i in []] + [TakeOut(i) for i in [5, 6]]),
    (s({6}), [PutIn(i) for i in [0, 1, 3, 5]] + [TakeOut(i) for i in [6]]),
    (s({1, 3}), [PutIn(i) for i in [0, 2, 4, 5, 6]] + [TakeOut(i) for i in [1, 3]]),
    (s({1, 2, 3}), [PutIn(i) for i in [0]] + [TakeOut(i) for i in [1, 2, 3]]),
    (s({}), [PutIn(i) for i in [0, 1, 2, 3, 4, 5, 6]] + [TakeOut(i) for i in []]),
]


@pytest.mark.parametrize("state, expected", enabled_actions_config)
def test_enabled_actions(state, expected):
    problem = KnapsackProblem(set(), weights, values, cap)

    return problem.enabled_actions(state) == expected
