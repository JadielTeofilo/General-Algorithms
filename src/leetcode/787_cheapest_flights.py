"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


dijkstra seems to be the way


distance: Dict[int, int]  # to, cost

we need to keep track of the num of stops (nodes in between)

using a heap

have the heap take the source and cost = 0, stops = 0
pop from heap

if already in the distance with smaller number of stops, skip it

if stops bigger then allowed, skip it
we update the distance to the curr node
add all neighbors to the heap adding the cost + curr_cost and stops + 1

return the cost if target on distance, else -1




5
[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
0
2
2



"""
import collections
import heapq
import sys
from typing import List, Dict, Set, Tuple


Graph = Dict[int, Set[Tuple[int, int]]]
HeapValue = collections.namedtuple('HeapValue', 'cost stops node')


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], 
                          src: int, dst: int, k: int) -> int:
        graph: Graph = build_graph(flights)
        heap: List[HeapValue] = [HeapValue(0, 0, src)]
        distance: Dict[int, Tuple[int, int]] = dict()
        while heap:
            cost, stops, curr = heapq.heappop(heap)
            if (curr in distance and stops > distance[curr][1]) or stops > k + 1:
                continue
            if curr == dst:
                return cost
            distance[curr] = cost, stops
            for neighbor, new_cost in graph[curr]:
                heapq.heappush(
                    heap, 
                    HeapValue(cost + new_cost, stops + 1, neighbor)
                )
        return -1


def build_graph(edges: List[List[int]]) -> Graph:
    graph: Graph = collections.defaultdict(set)
    for start, end, price in edges:
        graph[start].add((end, price))
    return graph
