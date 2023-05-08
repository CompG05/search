from collections import deque

from algorithms.search_algorithm import Node


def breadth_first_tree_search(problem):
    """
    [Figure 3.7]
    Search the shallowest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """

    frontier = deque([Node(problem.initial_state)])  # FIFO queue

    while frontier:
        node = frontier.popleft()
        if problem.is_goal(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None
