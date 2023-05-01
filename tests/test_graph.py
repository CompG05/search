from structures.graph import Graph, UndirectedGraph


def test_inverse_directed_graph():
    g = Graph(dict(
        a=dict(b=2, c=3),
        b=dict(d=4),
        d=dict(d=1),
    ))

    expected = Graph(dict(
        d=dict(d=1, b=4),
        b=dict(a=2),
        c=dict(a=3),
    ))

    assert g.inverse().graph_dict == expected.graph_dict
    for a in g.nodes():
        for b in g.nodes():
            assert g.get(a, b) == expected.get(b, a)

def test_inverse_undirected_graph():
    g = UndirectedGraph(dict(
        a=dict(b=2, c=3),
        b=dict(d=4),
        d=dict(d=1),
    ))

    expected = g

    assert g.inverse().graph_dict == expected.graph_dict
    for a in g.nodes():
        for b in g.nodes():
            assert g.get(a, b) == expected.get(b, a)
