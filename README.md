HW01 — Cables and Devices

Story  
I need to model a small office network. Each device is connected by cables. The input is a list of pairs like [('PC1','SW1'), ('SW1','PR1')]. I have to build a graph and calculate degrees.

Technical details  
- Input: list of (u,v) pairs
- Output:
  - build_graph(edges, directed=False): returns a dict where each node maps to a list of neighbors
  - degree_dict(graph): returns a dict where each node maps to its degree (number of neighbors)
- Constraints:
  - Node names are strings
  - No external libraries
  - Duplicates allowed
- Complexity:
  - build_graph: O(E) time, O(V+E) space
  - degree_dict: O(V+E)

Steps  
1. Understand: An edge means two devices connected by a cable. Undirected means both directions.
2. Rephrase: Make a dictionary of nodes and their neighbors.
3. I/O: Input is a list of tuples, output is a dict.
4. Plan: Loop through edges, add u→v and v→u if undirected.
5. Pseudocode:
graph = {}
for (u,v) in edges:
    if u not in graph: graph[u] = []
    graph[u].append(v)
    if not directed:
        if v not in graph: graph[v] = []
        graph[v].append(u)
return graph

Hints  
- Write code from pseudocode
- Debug with a small example
- Optimize: O(E) time, O(V+E) space

FAQ  
Q: Python version? A: 3.10 or 3.11  
Q: Read from stdin? A: No  
Q: Big-O? A: build_graph O(E), degree_dict O(V+E)  
Q: Duplicates? A: Allowed  
Q: Self-loop? A: Allowed  