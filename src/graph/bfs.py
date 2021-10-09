############ BFS of a graph ############
import neat_graph
from typing import Set
import collections


def bfs(graph: neat_graph.Graph, starting_vertex: int) -> None:
    """ Goes through the graph (connected or not) with bfs and prints it """
    visited: Set[int] = set()
    bfs_helper(graph, starting_vertex, visited)
    for vertex in graph.vertices:  # Iterates on every vertex in case of non connected graph
        bfs_helper(graph, vertex, visited)


def bfs_helper(graph: neat_graph.Graph, starting_vertex:int, visited: Set[int]) -> None:
    """ Does BFS on connected graph and prints nodes """
    queue: collections.deque[int] = collections.deque()
    queue.append(starting_vertex)
    while queue:
        vertex: int = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        print(vertex)
        for neighbor in graph.vertices[vertex]:
            queue.append(neighbor)


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
    bfs(graph, 1)

