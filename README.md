HW01 — Cables and Devices (Build a Graph + Degrees)

Story intro  
You manage a small office network. Each device is linked to others by a cable. You get a list of cable pairs. You need a data model to answer simple questions like “who is connected to whom?” and “how many cables touch each device?”

Technical description  
- Input: A list of edges like [('PC1','SW1'), ('SW1','PR1')]. Edges are undirected (a cable links both ways).
- Output:
  - build_graph(edges, directed=False): returns a dictionary mapping node → list of neighbors
  - degree_dict(graph): returns a dictionary mapping node → degree (number of neighbors)
- Constraints:
  - Node names are strings
  - No external libraries
  - Duplicates allowed
- Expected complexity:
  - build_graph: O(E) time, O(V+E) space
  - degree_dict: O(V+E)

ESL scaffold with the 8 Steps  
Steps 1–5  
1. Read & Understand: An edge means two devices connected by a cable. Undirected means both directions.
2. Rephrase: Make a dictionary mapping each node to its neighbors.
3. Identify I/O: Input is a list of (u,v) pairs. Output is a dict node → list of neighbors.
4. Break down: Loop through edges, add u→v and v→u if undirected. Ensure keys exist.
5. Pseudocode:
graph = {}
for (u,v) in edges:
    if u not in graph: graph[u] = []
    graph[u].append(v)
    if not directed:
        if v not in graph: graph[v] = []
        graph[v].append(u)
return graph

Steps 6–8  
- Write code: Turn pseudocode into Python.
- Debug: Print graph for a small example.
- Optimize: O(E) time, O(V+E) space.

FAQ  
Q: Python version? A: 3.10 or 3.11  
Q: Should I read from stdin? A: No. Write the functions. Tests import them.  
Q: Big-O? A: build_graph O(E), degree_dict O(V+E)  
Q: Duplicates? A: Allowed  
Q: Self-loop? A: Allowed; degree counts twice in undirected  