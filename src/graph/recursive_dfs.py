####### Depth first search recursive ##########
import neat_graph
from typing import Set, List


def dfs(graph: neat_graph.Graph, curr_node: int) -> None:
    """ Does DFS on graph and prints all vertices (integer value) """
    visited: Set[int] = set()
    dfs_helper(graph, curr_node, visited)  # Starts iteration from selected node
    # Makes sure all vertices are visited, in case of a non connected graph
    for vertex in graph.vertices:
        dfs_helper(graph, vertex, visited)


def dfs_helper(graph: neat_graph.Graph, curr_node: int, visited: Set[int]) -> None:
    """ Does DFS recursion starting from a given node """
    if curr_node in visited:
        return
    visited.add(curr_node)
    print(curr_node)
    for node in graph.vertices[curr_node]:
        dfs_helper(graph, node, visited)


if __name__ == '__main__':
    graph: neat_graph.Graph = neat_graph.Graph()
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(3,5)
    graph.add_edge(3,1)
    graph.add_edge(3,1)
    graph.add_edge(1,3)
    print(graph, end='\n')
    import pdb;pdb.set_trace()
    dfs(graph, 1)

