"""
Baby Names: Each year, the government releases a list of the 10,000 most common baby names
and their frequencies (the number of babies with that name). The only problem with this is that
some names have multiple spellings. For example, "John" and "Jon" are essentially the same name
but would be listed separately in the list. Given two lists, one of names/frequencies and the other
of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each
name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and
Johnny are synonyms. (It is both transitive and symmetric.) In the final list, any name can be used
as the "real" name.

In - names: Dict[str, int], equivalents: List[Tuple[str, str]]
Out - Dict[str, int]


Have a graph with the relations
Do a DFS on the graph, for each connected graph generate an output key



"""
import collections
from typing import List, Dict, Tuple, Set


class Graph:

	def __init__(self) -> None:
		self.vertices: Set[str] = set()
		self.edges: Dict[str, Set[str]] = collections.defaultdict(set)

	def add_edge(self, origin: str, target: str) -> None:
		self.vertices.add(origin)
		self.vertices.add(target)
		self.edges[origin].add(target)
		self.edges[target].add(origin)

	def add_vertex(self, value: str) -> None:
		self.vertices.add(value)


def fix_baby_names(
	names: Dict[str, int], 
	equivalents: List[Tuple[str, str]],
) -> Dict[str, int]:
	""" Deduplicates equivalent names and 
		finds the real count """
	# TODO check for empty inputs
	graph: Graph = build_graph(names, equivalents)
	visited: Set[str] = set()
	fixed_names: Dict[str, int] = {}
	for vertex in graph.vertices:
		if vertex in visited:
			continue
		fixed_names[vertex] = find_graph_count(
			vertex, graph, visited, names
		)
	return fixed_names


def find_graph_count(
	vertex: str, graph: Graph, visited: Set[str], 
	names: Dict[str, int] 
) -> int:
	""" Does the DFS and sums all nodes values"""
	if vertex in visited:
		return 0
	visited.add(vertex)
	count: int = 0
	count += names.get(vertex, 0)
	for neighbor in graph.edges[vertex]:
		count += find_graph_count(neighbor, graph, visited, names)
	return count
	

def build_graph(names: Dict[str, int], 
				equivalents: List[Tuple[str, str]]) -> Graph:
	graph: Graph = Graph()
	for name in names:
		graph.add_vertex(name)
	for origin, target in equivalents:
		graph.add_edge(origin, target)
	return graph


print(fix_baby_names({'jhon': 15, 'jon': 12, 'C': 13, 'K':4, 'Ch':19}, [('jhon', 'jon'), ('jhon', 'jhonny'), ('C', 'K'), ('C', 'Ch')]))
