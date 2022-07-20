"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.


In - routes: List[List[int]], source: int, target: int 


Out - buses: int (min)


source 1
target 20

A 1 5 9

B 10 12 20

C 5 12


5: [A, C]
12: [B, C]

A <-> C

C <-> B

since we only care about the num of buses, we can just have a generic relation between them 
    build the indexes
    build a graph from this   

we need to find the list of buses that have our starting point
    build a starting_nodes: List[int]
we need to find the list of buses that have our target point
    build a target_nodes: Set[int]

then we can run a BFS until we find a bus is in target nodes
    Add the starting nodes to the queue
    keep a visited
    pop from queue 
    if in target, return cost

QueueNode:
    node: int
    distance: int


O(S*B + E) time complexity where S it the max num of stops, B buses, E the relations (edges)
O(E+B) space complexity

"""
import collections
from typing import List, Dict, Set, Deque, Optional


Graph = Dict[int, Set[int]]
QueueNode = collections.namedtuple('QueueNode', 'node distance')


class Solution:
    def numBusesToDestination(
            self, routes: List[List[int]], 
            source: int, target: int
    ) -> int:
        graph: Graph = build_graph(routes)
        source_nodes: List[int] = [index for index, stops in enumerate(routes) if source in stops]
        target_nodes: Set[int] = set([index for index, stops in enumerate(routes) if target in stops])
        min_distance: Optional[int] = find_min_distance(
            graph, source_nodes, target_nodes
        )
        if min_distance is not None:
            return min_distance
        return -1


def build_graph(routes: List[List[int]]) -> Graph:
    graph: Graph = collections.defaultdict(set)
    indexing: Dict[int, List[int]] = collections.defaultdict(list)
    for index, route in enumerate(routes):
        for stop in route:
            indexing[stop].append(index)
    for buses in indexing.values():
        for bus in buses[1:]:
            graph[buses[0]].add(bus)
            graph[bus].add(buses[0])
    return graph


def find_min_distance(graph: Graph, source_nodes: List[int], 
                      target_nodes: Set[int]) -> Optional[int]:
    queue: Deque[QueueNode] = collections.deque(
        [QueueNode(node=node, distance=1) for node in source_nodes]
    ) 
    visited: Set[int] = set()
    while queue:
        node, distance = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node in target_nodes:
            return distance
        for neighbor in graph.get(node, []):
            queue.append(QueueNode(neighbor, distance + 1))
    



 
