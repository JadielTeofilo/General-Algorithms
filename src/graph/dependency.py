"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). 

All of a project's dependencies must be built before the project is. 

Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
EXAMPLE
In:
projects: a, b, c, d, e, f
dependencies:
 (a, d), (f, b), (b, d), (f, a),
 (d, c)
Out: f, e, a, b, d, c


topological sort

modified DFS


iterate on all vertices
result list
f -> a -> f

use local visited to check for duplicates

f -> b -> d -> c


"""
import collections
from typing import Dict, Set, List


Neighbors = Dict[int, Set[int]]


class Graph:

	def __init__(self) -> None:
		self.neighbors: Neighbors = collections.defaultdict(set)

	def insert(self, origin: int, target:int) -> None:
		self.neighbors[origin].add(target)

	def topologicly_sorted(self) -> List[int]:
		visited: Set[int] = set()
		result: List[int] = []
		# Itetares on all vertices in case of disconnected graph
		for vertex in self.neighbors:
			if vertex in visited:
				continue
			local_visited: Set[int] = set()
			self._sort_helper(local_visited, visited, 
							  result, vertex)
			visited.update(local_visited)
		return result[::-1]  # Reverts the result from DFS

	def _sort_helper(self, local_visited: Set[int], visited: Set[int],
					 result: List[int], vertex: int) -> None:
		""" Updates result with the reverse topo sorted order """
		if vertex in local_visited:
			raise ValueError('Cycle found')
		if vertex in visited:
			return
		local_visited.add(vertex)
		for neighbor in self.neighbors.get(vertex, []):
			self._sort_helper(local_visited, visited, result, neighbor)
		result.append(vertex)

		
asdf = Graph()
asdf.insert(1, 5)
asdf.insert(6, 1)
asdf.insert(6, 2)
asdf.insert(6, 3)
asdf.insert(2, 1)
asdf.insert(3, 1)
asdf.insert(2, 5)
asdf.insert(4, 7)
print(asdf.topologicly_sorted())

import pdb;pdb.set_trace()
			
