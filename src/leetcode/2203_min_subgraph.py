"""
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.



dikjstra is the way to go for distance in weigthed graphs

notice its a directed graph
you have to reach from src1 to dst
you have to reach from src2 to dst

we could do a djkstra from each, but we would not know the weight, cuz of the possibly overlapping part. 

the only case where we dont have overlaping nodes is if the dst is the extacly mid

we can find the mid and the distance between dst and this mid, the problem is that se cant make the dijkstra of dst, cuz its directed. We make the dijkstra of the reversed graph 


dijkstra
    have an empty cost dict
    have a heap with cost, vertex, initialized with 0, start
    skip elements already on cost
    pop from heap and insert new cost, vertex based on the neighbor of curr
    update curr cost
    return cost

build graph 
build reversed graph

iterate on all nodes, updating max of cost(src1, n) + cost(sr2, n) + cost(dst, n, reversed)

works cuz any path that has repeated nodes will have bigger weight


O(n*log(e)) time complexity where n is the num of nodes and e edges, cuz of neighbors iteration
O(n) space for the graph build

"""
import collections
import math
import heapq
from typing import List, Dict, Set, Union


HeapValue = collections.namedtuple('HeapValue', 'cost node')
GraphNode = collections.namedtuple('GraphNode', 'weight key')
Graph = Dict[int, Set[GraphNode]]


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], 
                      src1: int, src2: int, dest: int) -> int:
        graph: Graph = self.build_graph(edges)
        rev_graph: Graph = self.build_graph(edges, reverse=True)
        cost_src1: Dict[int, int] = self.dijkstra(graph, src1)
        cost_src2: Dict[int, int] = self.dijkstra(graph, src2)
        cost_dest: Dict[int, int] = self.dijkstra(rev_graph, dest)
        min_weight: Union[int, float] = math.inf
        for node in range(n):
            if (node not in cost_src1 or node not in cost_src2 
                or node not in cost_dest):
                continue
            min_weight = min(
                min_weight, 
                cost_src1[node] + cost_src2[node] + cost_dest[node]
            )
        if min_weight == math.inf:
            return - 1
        return min_weight
        
    def dijkstra(self, graph: Graph, node: int) -> Dict[int, int]:
        cost: Dict[int, int] = {}
        heap: List[HeapValue] = [HeapValue(0, node)]
        while heap:
            curr: HeapValue = heapq.heappop(heap)
            if curr.node not in cost:
                cost[curr.node] = curr.cost
                for neighbor in graph[curr.node]:
                    heapq.heappush(
                        heap, 
                        HeapValue(
                            curr.cost + neighbor.weight, neighbor.key
                        )
                    )
        return cost

    def build_graph(self, edges: List[List[int]], 
                   reverse: bool = False) -> Graph:
        graph: Graph = collections.defaultdict(set)
        for edge in edges:
            if reverse:
                graph[edge[1]].add(GraphNode(edge[2], edge[0]))
            else:
                graph[edge[0]].add(GraphNode(edge[2], edge[1]))
        return graph


