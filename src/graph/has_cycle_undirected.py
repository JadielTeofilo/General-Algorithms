################ Graph cycle detection UnDirected graph ################
""" Have a local visited and an outer visited, local visited can not repeat """
from typing import Set, Optional

import neat_graph


def has_cycle(graph: neat_graph.Graph) -> bool:
    visited: Set[int] = set()
    for vertex in graph.vertices:
        if has_cycle_helper(graph, vertex, visited):
            return True
    return False

def has_cycle_helper(graph: neat_graph.Graph, 
                               starting_vertex: int, visited: Set[int], 
                               local_visited: Optional[Set[int]] = None,parent: Optional[int]=None) -> bool:
    """ Returns True if the DFS from starting_vertex hits a repeated node """
    local_visited = set() if not local_visited else local_visited
    if starting_vertex in local_visited:
        return True
    local_visited.add(starting_vertex)
    if starting_vertex in visited:
        return False
    visited.add(starting_vertex)
    for neighbor in graph.vertices.get(starting_vertex, []):
        if neighbor == parent:
            continue
        if has_cycle_helper(graph, neighbor, visited, local_visited, starting_vertex):
            return True
    return False


if __name__ == '__main__':
    graph: neat_graph.Graph = neat_graph.Graph()
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(3,5)
    graph.add_edge(3,1)
    graph.add_edge(3,1)
    print(graph, end='\n')
    has_cycle(graph)
    import pdb;pdb.set_trace()
