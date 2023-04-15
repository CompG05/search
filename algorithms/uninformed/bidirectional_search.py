from collections import deque
from typing import Optional

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import InvertibleProblem


def join_nodes(d: str, node: Node, other_node: Node):
    if d == 'f':
        f_node, b_node = node, other_node
    else:
        f_node, b_node = other_node, node

    # the first node has the same state as f_node
    b_path = list(reversed(b_node.path()))[1:]
    last_node = f_node
    last_action = b_node.action

    for n in b_path:
        last_action = last_action.inverse()
        last_node = Node(state=n.state,
                         parent=last_node,
                         action=last_action,
                         path_cost=last_node.path_cost + last_action.cost)
        last_action = n.action

    return last_node


def proceed(d: str,
            problem: InvertibleProblem,
            frontier_dir: deque[Node],
            other_frontier: deque[Node]) -> Optional[Node]:
    node = frontier_dir.popleft()
    for other_node in other_frontier:
        if node.state == other_node.state:
            return join_nodes(d, node, other_node)

    frontier_dir.extend(node.expand(problem))

    return None


class BidirectionalSearch(SearchAlgorithm):
    def search(self, problem_f: InvertibleProblem) -> Optional[Node]:
        problem_b = problem_f.inverse()

        frontier_f = deque([Node(problem_f.initial_state)])
        frontier_b = deque([Node(problem_b.initial_state)])

        next_expand = 'f'

        solution = None

        while frontier_f and frontier_b and not solution:
            if next_expand == 'f':
                solution = proceed('f', problem_f, frontier_f, frontier_b)
                next_expand = 'b'
            else:
                solution = proceed('b', problem_b, frontier_b, frontier_f)
                next_expand = 'f'

        return solution


bidirectional_search = BidirectionalSearch()
