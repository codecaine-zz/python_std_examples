# graphlib - Functionality to operate with graph-like structures

The `graphlib` module is part of Python's standard library and provides an API for working with directed graphs. While it is not as commonly used as some other graph libraries like NetworkX, it can be useful for specific use cases where you need a simple, lightweight solution.

Here are comprehensive code examples demonstrating various functionalities in the `graphlib` module:

```python
import graphlib

# Example 1: Creating and manipulating a DirectedGraph

def create_and_manipulate_directed_graph():
    """
    This example demonstrates how to create a DirectedGraph and perform basic operations.
    """

    # Create a new DirectedGraph instance
    dg = graphlib.DirectedGraph()

    # Add nodes to the graph
    dg.add_node('A')
    dg.add_node('B')
    dg.add_node('C')

    # Add edges between nodes
    dg.add_edge(('A', 'B'))
    dg.add_edge(('B', 'C'))

    # Print nodes and edges in the graph
    print("Nodes:", list(dg.nodes()))
    print("Edges:", list(dg.edges()))

    # Check if a node is in the graph
    print("Node A exists:", dg.has_node('A'))

    # Check if an edge exists between two nodes
    print("Edge (A, B) exists:", dg.has_edge(('A', 'B')))

    # Remove a node and all its edges
    dg.remove_node('B')
    print("After removing node B:")
    print("Nodes:", list(dg.nodes()))
    print("Edges:", list(dg.edges()))

# Example 2: Topological Sorting

def perform_topological_sort():
    """
    This example demonstrates how to perform a topological sort on a DirectedGraph.
    """

    # Create a new DirectedGraph instance
    dg = graphlib.DirectedGraph()

    # Add nodes and edges
    dg.add_node('A')
    dg.add_node('B')
    dg.add_node('C')
    dg.add_edge(('A', 'B'))
    dg.add_edge(('B', 'C'))

    # Perform topological sort
    try:
        sorted_nodes = list(dg.toposort())
        print("Topological Sort:", sorted_nodes)
    except graphlib.CycleError as e:
        print(f"Graph contains a cycle: {e}")

# Example 3: Finding Strongly Connected Components

def find_strongly_connected_components():
    """
    This example demonstrates how to find strongly connected components in a DirectedGraph.
    """

    # Create a new DirectedGraph instance
    dg = graphlib.DirectedGraph()

    # Add nodes and edges
    dg.add_node('A')
    dg.add_node('B')
    dg.add_node('C')
    dg.add_edge(('A', 'B'))
    dg.add_edge(('B', 'C'))
    dg.add_edge(('C', 'A'))

    # Find strongly connected components
    scc = dg.strongly_connected_components()
    print("Strongly Connected Components:", list(scc))

# Run the examples
if __name__ == "__main__":
    create_and_manipulate_directed_graph()
    perform_topological_sort()
    find_strongly_connected_components()
```

### Explanation:

1. **Creating and Manipulating a DirectedGraph:**
   - We create an instance of `graphlib.DirectedGraph`.
   - We add nodes and edges to the graph.
   - We print nodes, edges, and check for node and edge existence.
   - We remove a node and verify the changes.

2. **Topological Sorting:**
   - We perform a topological sort on a DirectedGraph that does not contain cycles.
   - We handle potential `CycleError` exceptions if the graph contains cycles.

3. **Finding Strongly Connected Components:**
   - We find strongly connected components in a DirectedGraph using the `strongly_connected_components` method.
   - This method is useful for analyzing the structure of a directed graph to identify groups of nodes where each node can reach every other node within that group.

These examples provide a basic understanding of how to use the `graphlib` module for various graph operations. You can further explore the documentation and additional methods available in the module for more advanced use cases.

## Table of Contents

1. [Creating and manipulating a DirectedGraph](#example-1-creating-and-manipulating-a-directedgraph)
2. [Topological Sorting](#example-2-topological-sorting)
3. [Finding Strongly Connected Components](#example-3-finding-strongly-connected-components)
