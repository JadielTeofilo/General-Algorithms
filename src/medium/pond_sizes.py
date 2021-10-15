"""
 Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. 

A value of zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. 

The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.


Its kind of a graph problem, we can turn it into a graph and check the size of all connected graphs

In - grid: List[List[int]]
Out - sizes: List[int]


O(V+E) time complexity where V is the amount of nodes on the graph and E the edges
O(V+E) space complexity 

"""
import collections
from typing import Dict, Set, List, Iterable, Optional


Key = collections.namedtuple('Key', 'row col')


class Graph:

	def __init__(self) -> None:
		self.vertices: Dict[Key, Set[Key]] = collections.defaultdict(set)
	
	def insert(self, origin: Key, target: Optional[Key]) -> None:
		if not target:
			self.vertices[origin] = set() 
		self.vertices[origin].add(target)
		

def pond_sizes(grid: List[List[int]]) -> Iterable[int]:
	# TODO Check size of grid
	graph: Graph = turn_into_graph(grid)
	return connected_subgraphs_sizes(graph)


def turn_into_graph(grid: List[List[int]]) -> Graph:
	options: List[Key] = [
		Key(+1, 0),
		Key(+1, -1),
		Key(+1, +1),
		Key(-1, -1),
		Key(-1, +1),
		Key(-1, 0),
		Key(0, +1),
		Key(0, -1),
	]
	graph: Graph = Graph()
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] != 0:
				continue
			graph.insert(origin=Key(row, col), target=None)
			for option in options:
				target: Key = Key(row+option.row, col+option.col)
				if not is_valid(target, grid):
					continue
				if grid[target.row][target.col] != 0:
					continue
				graph.insert(origin=Key(row, col), target=target)
	return graph


def is_valid(target: Key, grid: List[List[int]]) -> bool:
	if target.row < 0 or target.col < 0:
		return False
	if target.row >= len(grid) or target.col >= len(grid[0]):
		return False
	return True


def connected_subgraphs_sizes(graph: Graph) -> Iterable[int]:
	visited: Set[Key] = set()
	for vertex in graph.vertices:
		if vertex in visited:
			continue
		yield _count_connections(vertex, visited, graph)


def _count_connections(root: Key, visited: Set[Key], graph: Graph) -> int:
	stack: List[Key] = [root]
	count: int = 0
	while stack:
		vertex: Key = stack.pop()
		if vertex in visited:
			continue
		count += 1
		visited.add(vertex)
		for neighbor in graph.vertices[vertex]:
			stack.append(neighbor)
	return count
	

asdf = [
[0,2,1,0],
[0,1,0,1],
[1,1,0,1],
[0,1,0,1],
]
print([a for a in pond_sizes(asdf)])
import pdb;pdb.set_trace()	
