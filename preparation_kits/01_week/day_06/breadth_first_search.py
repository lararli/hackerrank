"""Module to implement breadth-first search.

This module contains a function that performs breadth-first search on a graph.
The bfs function performs breadth-first search on a
graph given as a list of edges and a starting node.
It returns a list of distances from the starting node to all
other nodes in the graph. The implementation uses a defaultdict to
represent the graph and a queue for the BFS. The distance from the
starting node to itself is 0, and the distance to other nodes is calculated
by adding 6 to the distance of their parent node.

"""

from collections import defaultdict
import os


def bfs(num_nodes, num_edges, edges, starting_node):
    # pylint:disable=unused-argument
    """Perform breadth-first search on a graph.

    Given a graph represented as a list of edges and a starting vertex s, this function
    performs breadth-first search to determine the shortest distance to all nodes.

    Args:
        num_nodes (int): The number of nodes in the graph.
        num_edges (int): The number of edges in the graph.
        edges (list): A list of tuples representing the edges of the graph.
        starting_node (int): The starting node for the search.

    Returns:
        list: A list of distances from the starting node to all other nodes.
    """

    # Create a defaultdict to represent the graph
    graph = defaultdict(list)

    # Add edges to the graph
    for start_node, end_node in edges:
        graph[start_node].append(end_node)
        graph[end_node].append(start_node)

    # Initialize a list to store the distances from s to each node
    distances = [-1] * num_nodes

    # Initialize a queue for BFS
    queue = [starting_node]

    # Distance from starting node to itself is 0
    distances[starting_node - 1] = 0

    # Perform BFS
    while queue:
        node = queue.pop(0)

        for neighbor in graph[node]:
            if distances[neighbor - 1] == -1:
                distances[neighbor - 1] = distances[node - 1] + 6
                queue.append(neighbor)

    # Return the list of distances
    return distances
