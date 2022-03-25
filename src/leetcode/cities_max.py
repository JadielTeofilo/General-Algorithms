"""
https://leetcode.com/discuss/interview-question/1621880/Google-or-Onsite-or-Maximum-total/1178791

You are given a set of cities, for each you know the anticipated excitement you get by visiting this city. You are also given a set birectional flights, and you need to choose 4 distinct cities A, B, C, D so there are direct flights between A-B, B-C, C-D and total excitement is maximized.

Example,

Input:

N cities:
New York 10000
San Francisco 1000
Texas 500
LA 20000
Chicago 3000
San Jose 900

M flights:
New York <-> San Francisco
New York <-> LA
Chicago <-> LA
San Jose <-> San Francisco

Output:

San Francisco -> New York -> LA -> Chicago
1000 + 10000 + 20000 + 3000 = 34000


------
Wrong:

The idea is that we want to find the max path of 4 nodes
We could start from each node and test each of its neighbors with 4 - 1

solve(node, trips_left) -> max path using that node and with trips left

we can memoize on node and trips left then we will have O(k*v*e)

Reason: 
Path algorithms have to worry about reusing elements previously used, so the memoization does not work.

-------
Take each edge, lets say from B to C what we need is to find a vertex that connects to B that is not C, (lets call it A), and then find a vertex that connects to C that is not B nor A (lets call it D)

We do have to do it the other way around picking first from the C then from B

   5
3 4  6 1

3 4
4 5
4 6
5 6
6 1

B = 4 C = 5
we would pick 6 as A and nothing would be left for D
second time around
we pick D as 6 and 3 as A

we skip edges with either vertices with single connection

---
Precompute the 3 bigest neighbors for each vertex

Iterate on the edges, for each edge get the max possible value using that edge as the mid edge of the answer
    to get max value try two ways
        finding first neighbor from B 
        finding first neighbor from C

return a result


O(V + E) time where V = vertices, E = edges
O(V) space

"""
import collections
import heapq
from typing import List, Dict, Set, Optional, Tuple
import unittest


Graph = Dict[int, List[int]]


class Solution:

    def solve(self, excitement: List[int], edges: List[Tuple[int, int]]) -> int:
        biggest_neighbors: Graph = self.build_graph(edges, excitement)
        result: int = 0 
        for start, end in edges:
            if (len(biggest_neighbors[start]) < 2 
                or len(biggest_neighbors[end]) < 2):
                continue
            curr_max: int = max(
                self.pick_max(start, end, biggest_neighbors, excitement), 
                self.pick_max(end, start, biggest_neighbors, excitement),
            )
            result = max(curr_max, result)
        return result

    def pick_max(self, first: int, second: int, biggest_neighbors: Graph, 
                 excitement: List[int]) -> int:
        exclusion: List[int] = [second]
        first_neighbor: Optional[int] = self.find_first_valid(
            biggest_neighbors[first], exclusion
        )
        if first_neighbor is None:
            return 0
        exclusion = [first, first_neighbor]
        second_neighbor: Optional[int] = self.find_first_valid(
            biggest_neighbors[second], exclusion
        )
        if second_neighbor is None:
            return 0
        return (excitement[first] + excitement[second] + 
                excitement[first_neighbor] + excitement[second_neighbor])
        
    def find_first_valid(self, neighbors: List[int], 
                         exclusion: List[int]) -> Optional[int]:
        for neighbor in neighbors:
            if neighbor in exclusion:
                continue
            return neighbor        
        
    def build_graph(self, edges: List[Tuple[int, int]], 
                    excitement: List[int]) -> Graph:
        graph: Graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        for vertex in graph:
            largest: List[Tuple[int, int]] = heapq.nlargest(3,
                [(excitement[node], node) for node in graph[vertex]]
            )
            graph[vertex] = [node_data[1] for node_data in largest]
        return graph


class Test(unittest.TestCase):
    def test_graph(self) -> None:
        self.assertEquals(Solution().solve(
            [6, 4, 9, 1, 7],
            [(0, 1), (1, 2), (2, 3), (1, 4), (4, 2)],
        ), 26)


if __name__ == '__main__':
    unittest.main()
