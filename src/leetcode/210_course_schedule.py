"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



need topo sort and cycle detection

the idea is to find the first node that has no requirement and add to result, and remove it from the lookup

create graph from edges and make bi have ai as rependency

iterate on all nodes

check local visited, stop if cycle
check visited, and update it
recurse on all neighbors
add to result

return reversed result




"""
import collections
from typing import List, Dict, Set


Graph = Dict[int, Set[int]]


class Solution:
    def findOrder(self, numCourses: int, 
                  prerequisites: List[List[int]]) -> List[int]:
        graph: Graph = self.build_graph(prerequisites)
        visited: Set[int] = set()
        result: List[int] = []
        has_cycle: Dict[str, bool] = {'cycle': False}
        for node in range(numCourses):
            local_visited: Set[int] = set()
            self.fill_dependencies(node, graph, result, 
                                   visited, local_visited, has_cycle)
            if has_cycle['cycle']:
                return []
        return result[::-1]

    def fill_dependencies(
        self, node: int, graph: Graph, result: List[int], 
        visited: Set[int], local_visited: Set[int], has_cycle: Dict[str, bool]
    ) -> None:
        if node in visited:
            has_cycle['cycle'] = node in local_visited
            return
        visited.add(node)
        local_visited.add(node)
        for neighbor in graph[node]:
            self.fill_dependencies(neighbor, graph, result, 
                                   visited, local_visited, has_cycle)
        result.append(node)

    def build_graph(self, edges: List[List[int]]) -> Graph:
        graph: Graph = collections.defaultdict(set)
        for end, start in edges:
            graph[start].add(end)
        return graph
        
        
