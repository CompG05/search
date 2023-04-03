from algorithm.solver import Solver
from problems.missionaries_cannibals import *
from problems.problem import *
from algorithm.uninformed.depth_first_search import depth_first_tree_search, depth_first_graph_search

first_class_searchers = [depth_first_tree_search, depth_first_graph_search]

initial_state = MCState((3, 3, 0, 0))
M_action = MCAction(1, 0)
C_action = MCAction(0, 1)
MM_action = MCAction(2, 0)
CC_action = MCAction(0, 2)
MC_action = MCAction(1, 1)
mc_problem = Problem(initial_state, [M_action, C_action, MM_action, CC_action, MC_action])


def test_mc_enabled_actions():
    state = MCState((2, 2, 1, 1))
    assert set(mc_problem.enabled_actions(state)) == {MC_action, MM_action}

    state.data = (0, 2, 1, 1)
    assert set(mc_problem.enabled_actions(state)) == set()

    state.data = (1, 1, 1, 1)
    assert set(mc_problem.enabled_actions(state)) == {M_action, MC_action}

    state.data = (2, 1, 2, 2)
    assert set(mc_problem.enabled_actions(state)) == {M_action, MC_action, MM_action}


def test_mc_actions_execute():
    state = MCState((2, 1, 2, 2))
    assert (M_action.execute(state)).data == (1, 1, 3, 2)

    assert (MM_action.execute(state)).data == (0, 1, 4, 2)

    assert (MC_action.execute(state)).data == (1, 0, 3, 3)

    state.data = (0, 2, 2, 0)
    assert (C_action.execute(state)).data == (0, 1, 2, 1)

    assert (CC_action.execute(state)).data == (0, 0, 2, 2)


def test_mc_solving():
    m1, c1, m2, c2 = initial_state.data
    solver = Solver(mc_problem, initial_state)
    for searcher in first_class_searchers:
        solver.set_algorithm(searcher)
        solution = solver.solve()

        print("Searcher: ", searcher)
        print("Action sequence: ", solution.action_sequence)
        print("Path length: ", len(solution.action_sequence))
        print("Path cost: ", solution.path_cost)
        print()

        assert solution.final_state.data == (0, 0, m1 + m2, c1 + c2)
