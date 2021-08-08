############ Topological sort with DFS ############
""" Make a normal DFS and add node to result when there are no more dependents of it, return reverse of this list """
import neat_graph

from typing import List, Set


def topological_sort(graph: neat_graph.Graph) -> List[int]:
    visited: Set[int] = set()
    result: List[int] = []
    for vertex in graph.vertices:
        sort_helper(graph, vertex, result, visited)
    return result[::-1]  # reverse result before returning
        

def sort_helper(graph: neat_graph.Graph, starting_vertex: int, 
                      result: List[int], visited: Set[int]) -> None:
    """ DFS implementation to update the sorted result list """
    if starting_vertex in visited:
        return
    visited.add(starting_vertex)
    for neighbor in graph.vertices.get(starting_vertex, []):
        sort_helper(graph, neighbor, result, visited)
    # Add to result when all the dependents have been added
    result.append(starting_vertex)


if __name__ == '__main__':
    graph: neat_graph.Graph = neat_graph.Graph()
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(2,5)
    graph.add_edge(4,2)
    graph.add_edge(4,5)
    print(graph, end='\n')
    import pdb;pdb.set_trace()
    topological_sort(graph)

