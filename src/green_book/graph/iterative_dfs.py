######## DFS with a stack ##########
import neat_graph
from typing import Set, List


def dfs(graph: neat_graph.Graph, starting_node: int) -> None:
    """ Does the DFS of the graph from starting_node and prints nodes """
    visited: Set[int] = set()
    dfs_helper(graph, starting_node, visited)  # Does the dfs from the selected starting node
    # Tries to do the dfs on every node to check for non connected graphs
    for vertex in graph.vertices:
        dfs_helper(graph, vertex, visited)


def dfs_helper(graph: neat_graph.Graph, curr_node: int, visited: Set[int]) -> None:
    """ Does the DFS with a stack """
    stack: List[int] = []
    if curr_node in visited:
        return
    visited.add(curr_node)
    stack.append(curr_node)
    while stack:
        node: int = stack.pop()
        print(node)
        for edge in graph.vertices[node]:
            if edge in visited:
                continue
            visited.add(edge)
            stack.append(edge)


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

