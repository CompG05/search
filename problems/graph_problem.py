from problems.problem import InvertibleAction, InvertibleProblem
from structures.graph import Graph


class Edge(InvertibleAction):
    """Represents a transition to another node in a graph"""

    def __init__(self, graph: Graph, source, dest):
        super().__init__()
        self.graph = graph
        self.source = source
        self.dest = dest
        self.cost = graph.get(source, dest)

    def execute(self, source) -> object:
        return self.dest

    def is_enabled(self, source) -> bool:
        return source == self.source and self.dest in self.graph.get(self.source)

    def inverse(self) -> 'Edge':
        return Edge(self.graph.inverse(), self.dest, self.source)

    def __eq__(self, other):
        return self.graph == other.graph \
            and self.source == other.source \
            and self.dest == other.dest \
            and self.cost == other.cost

    def __hash__(self) -> int:
        t = (self.source, self.dest, self.cost)
        return t.__hash__()

    def __repr__(self):
        return self.source.__str__() + " -> " + self.dest.__str__() + " (" + self.cost.__str__() + ")"


class GraphProblem(InvertibleProblem):
    """Represents a single source-single destination graph problem"""

    def __init__(self, graph: Graph, initial, goal):
        self.graph = graph
        self.initial = initial
        self.goal = goal
        super().__init__(self.initial, self.goal)
        self.edges = [Edge(self.graph, source, dest)
                      for source in graph.nodes()
                      for dest in graph.get(source).keys()]

    def is_goal(self, state) -> bool:
        return state == self.goal

    def inverse(self) -> 'GraphProblem':
        return GraphProblem(self.graph.inverse(), self.goal, self.initial)

    def enabled_actions(self, source) -> list[Edge]:
        return [edge for edge in self.edges if edge.source == source]
