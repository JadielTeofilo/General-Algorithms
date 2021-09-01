"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes
"""
import collections
from typing import Set


class Graph:
    
    def __init__(self):
        self.neighbors: Dict[int, Set[int]] = collections.defaultdict(set)
        
    def insert(self, target: int, origin: int) -> None:
        self.neighbors[origin].add(target)
        
    def remove(self, target: int, origin: int) -> None:
        self.neighbors[origin].dicard(target)
        

def has_route(graph: Graph, target: int, origin: int) -> bool:
    if not target or not origin or not graph.neighbors:
        raise ValueError('Empty inputs')
    return (_find_route(graph, target=target, origin=origin) or
            _find_route(graph, target=origin, origin=target))


def _find_route(graph: Graph, origin: int, target: int) -> bool:
    """ Checks existence of route from origin to target with a BFS """
    queue: collections.deque = collections.deque()
    queue.append(origin)
    visited: Set = set()
    
    while queue:
        node: int = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == target:
            return True
        for neighbor in graph.neighbors[node]:
            queue.append(neighbor)

    return False


import pdb;pdb.set_trace()
