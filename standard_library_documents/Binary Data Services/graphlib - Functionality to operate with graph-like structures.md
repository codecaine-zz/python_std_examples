# graphlib — Functionality to operate with graph-like structures

Here's an example of all possible use cases for the `graphlib` module in Python:

```python
import networkx as nx  # For creating and manipulating graphs
from graphlib import CycleError, TopologicalSortError
import matplotlib.pyplot as plt  # For visualizing the graph

# Create a new directed acyclic graph (DAG)
G = nx.DiGraph()

# Add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Add edges between nodes
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')  # This creates a cycle in the graph

try:
    # Attempt to perform topological sort on the graph
    G_topo = nx.topological_sort(G)
except TopologicalSortError as e:
    print(f"Topological sort failed: {e}")

try:
    # Perform DFS traversal on the graph
    nx.dfs_tree(G)
except CycleError as e:
    print(f"Cycle detected in the graph: {e}")

# Create a new undirected graph
G_undir = nx.Graph()

# Add nodes to the undirected graph
G_undir.add_node('D')
G_undir.add_node('E')

# Add edges between nodes in the undirected graph
G_undir.add_edge('D', 'E')
G_undir.add_edge('E', 'D')

try:
    # Perform DFS traversal on the undirected graph
    nx.dfs_tree(G_undir)
except CycleError as e:
    print(f"Cycle detected in the undirected graph: {e}")

# Create a new weighted directed acyclic graph (W-DAG)
G_weighted = nx.DiGraph()

# Add nodes to the W-DAG
G_weighted.add_node('F')
G_weighted.add_node('G')

# Add edges between nodes with weights
G_weighted.add_edge('F', 'G', weight=2)

try:
    # Perform topological sort on the W-DAG
    nx.topological_sort(G_weighted)
except TopologicalSortError as e:
    print(f"Topological sort failed: {e}")

# Visualize the graph using matplotlib
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20)

plt.show()
```

The above code snippet demonstrates the following use cases:

*   Creating and manipulating directed acyclic graphs (DAGs) with `graphlib`.
*   Attempting to perform topological sort on a graph.
*   Performing depth-first search (DFS) traversal on a graph, including handling cycles in both DAGs and undirected graphs.
*   Creating and manipulating weighted directed acyclic graphs (W-DAGs).
*   Visualizing the structure of a graph using matplotlib.
