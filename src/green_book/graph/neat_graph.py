
##### Dict Graph implementation list of edges #####
from typing import Dict, Set
import collections


class Graph:

    def __init__(self) -> None:
        self.vertices: Dict[int, Set[int]] = collections.defaultdict(set)

    def add_edge(self, source: int, destination: int) -> None:
        self.vertices[source].add(destination)

    def remove_edge(self, source: int, destination: int) -> None:
        self.vertices[source].discard(destination)

    def __str__(self) -> str:
        return str(self.vertices)


if __name__ == '__main__':
    graph: Graph = Graph()
    print(graph)
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(3,5)
    graph.add_edge(3,1)
    graph.add_edge(3,1)
    graph.add_edge(1,3)
    graph.remove_edge(3,1)
    print(graph)

