##### Graph implementation list of edges #####
from typing import List, Tuple


class SimpleGraph:
    
    def __init__(self) -> None:
        self.edges: List[Tuple[int, int]] = []

    def add_edge(self, source: int, destination: int) -> None:
        self.edges.append((source, destination))
        return

    def __str__(self) -> str:
        return str(self.edges)


if __name__ == '__main__':
    graph: SimpleGraph = SimpleGraph()
    graph.add_edge(1,2)
    graph.add_edge(2,2)
    graph.add_edge(3,2)
    graph.add_edge(3,4)
    print(graph)

