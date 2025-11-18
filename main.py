"""
HW01 — Cables and Devices

Implement:
- build_graph(edges, directed=False)
- degree_dict(graph)

Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    """Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.
    """
    graph = {}

    for u, v in edges:
        # Ensure u exists
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        if not directed:
            # For undirected, add reverse edge
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
        else:
            # For directed, ensure v exists even if no outgoing edges
            if v not in graph:
                graph[v] = []

    return graph


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors)."""
    return {node: len(neighbors) for node, neighbors in graph.items()}


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print("Sample edges:", sample)
    g = build_graph(sample, directed=False)
    print("Graph:", g)
    print("Degrees:", degree_dict(g))