def build_graph(edges, directed=False):
    """Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.
    """
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        if not directed:
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
        else:
            if v not in graph:
                graph[v] = []

    return graph


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors)."""
    return {node: len(neighbors) for node, neighbors in graph.items()}