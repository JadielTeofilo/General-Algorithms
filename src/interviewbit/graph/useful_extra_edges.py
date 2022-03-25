"""
Given a graph of A nodes. Also given the weighted edges in the form of array B.

You are also given starting point C and destination point D.

Also given are some extra edges in the form of vector E.

You need to find the length of the shortest path from C to D if you can use maximum one road from the given roads in E.

All roads are bidirectional.

------


            1 - 4 - 5
            |       |
            8 - 3 ---
                 | 
                 6  

1
3 F



3 F


build a graph with dict from key to edges
    have a second set of edges that are the exceptional ones

Use bfs to find the other node
we can use bidirectional search for this one since its not a directed graph

On the bfs queue have the info that says if it already used the exceptional road and the lenght

iterate on both queues keeping 2 visisted

the visited also says if it was a path with a exceptional 

loop queue
    curr, exceptional, lenght = pop from queue
    check update visited
    check other visited, if there and not two exceptionals, return lenght + lenght
    iterate neighbors
    if not exceptional iterate on exceptionals


O(k^(d/2)) time where k is the max number of edges per node, and d is the distance
O(V+E) space where V is vertices and E edges

"""
import collections
from typing import List, Set, Dict, Deque


Edge = collections.namedtuple('Edge', 'key weight')
QueueNode = collections.namedtuple('QueueNode', 'edge path is_excep')
VisitedMeta = collections.namedtuple('VisitedMeta', 'path is_excep')
Visited = Dict[int, VisitedMeta]


class Graph:

    def __init__(self):
        self.edges: Dict[int, Set[Edge]] = collections.defaultdict(set)
        self.excep: Dict[int, Set[Edge]] = collections.defaultdict(set)
        self.vertices: Set[int] = set()


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @param E : list of list of integers
    # @return an integer
    def solve(self, vertices_num: int, edges: List[List[int]], 
              original: int, target: int, excep: List[List[int]]) -> int:
        graph: Graph = self.build_graph(edges, excep)  # TODO   
        original_queue: Deque[QueueNode] = collections.deque(
            [QueueNode(Edge(original, 0), False, 0)]
        )
        target_queue: Deque[QueueNode] = collections.deque(
            [QueueNode(Edge(target, 0), False, 0)])
        original_visited: Visited = {}
        target_visited: Visited = set()
        while original_queue or target_queue:
            path: Optional[int] = find_path(
                graph,
                original_queue, target_queue, 
                original_visited, target_visited,       
            )
            if path is None:
                path = find_path(
                    graph,
                    target_queue, original_queue, 
                    target_visited, original_visited,
                )
            if path is not None:
                return path
        return -1

    def find_path(self, graph: Graph, queue: Deque[QueueNode], 
                  other_queue: Deque[QueueNode], 
                  visited: Visited, 
                  other_visited: Visited) -> Optional[int]:
        curr: QueueNode = queue.pop()
        if curr.edge.key in visited:
            return None
        visited.add(QueueNode)
        if (curr.edge.key in other_visited and 
            not (curr.is_excep and other_visited[curr.edge.key].is_excep)):
            return curr.path + other_visited[curr.edge.key].path
        neighbors: List[Edges] = list(graph.edges[curr.edge.key])
        if curr.is_excep:
            neighbors.extend(graph.excep[curr.edge.key])
        for neighbor in neighbors:
            queue.append(
                QueueNode(
                    neighbor, curr.path + neighbor.weight, 
                    curr.is_excep
                )
            )

        
        
