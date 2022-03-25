"""
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node

B[i][0] to node B[i][1].

Find whether a path exists from node 1 to node A.

Return 1 if path exists else return 0.

In - target: int, edges: List[List[int]]
Out - int (0 or 1)


we can use BFS to traverse the graph from node 1
build a graph from the input (to have key value pairs)
keep a visited
add the start to queue
pop it, check/add to visited, add all neighbors
if curr is target, return 1
return 0 


O(d) where d is the distance between them
O(n) where n is the num of nodes

"""
import collections
from typing import List, Set, Dict



class Graph:

    def __init__(self) -> None:
        self.vertices: Set[int] = set()
        self.edges: Dict[int, Set[int]] = collections.defaultdict(set)
    
    def insert_edge(self, start: int, end: int) -> None:
        self.vertices.add(start)
        self.vertices.add(end)
        self.edges[start].add(end)
    

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, target: int, edges: List[List[int]]) -> int:
        graph: Graph = self.build_graph(edges)
        deque = collections.deque()
        deque.append(1)
        visited: Set[int] = set()
        while deque:
            curr: int = deque.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr == target:
                return 1
            for neighbor in graph.edges[curr]:
                deque.append(neighbor)
        return 0

    def build_graph(self, edges: List[List[int]]) -> Graph:
        graph: Graph = Graph()
        for start, end in edges:
            graph.insert_edge(start, end)
        return graph
