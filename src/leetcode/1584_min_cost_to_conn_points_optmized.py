"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


build a graph: Dict[Point, Set[Tuple[int, Point]]]


build minimum spanning tree cost

dijkstra

have a heap with possible edges, start with anyone and cost 0

O(n^2log n) time complexity
O(n^2) space complexity


"""
import collections
import heapq
from typing import Dict, Set, List, Tuple


Point = collections.namedtuple('Point', 'x y')
Graph = Dict[Point, Set[Tuple[int, Point]]]



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph: Graph = build_graph(points)
        return get_min_cost(Point(*points[0]), graph)


def get_min_cost(start: Point, points: List[List[int]]) -> int:
    distance: Dict[Point, int] = {start: 0}
    visited: Set[Point] = set()
    total_cost: int = 0
    edges: int = 1
    while edges != len(graph):
        min_edge: Tuple[int, Point] = (sys.maxsize, Point(0, 0))

        for point in distance:
            if neighbor in visited:
                continue
            min_edge = min(min_edge, (new_cost, neighbor))

    return total_cost


def get_distance(first: Point, second: Point) -> int:
    return abs(second.x - first.x) + abs(second.y - first.y)




