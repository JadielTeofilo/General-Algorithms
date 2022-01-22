##### Graph implementation list of adjacencies #####
import dataclasses
from typing import List, Any, Optional


@dataclasses.dataclass
class GraphNode:
    value: int
    edges: List['GraphNode'] = dataclasses.field(default_factory=list)


class Graph:

    def __init__(self) -> None:
        self.vertices: List[GraphNode] = []

    def add_edge(self, from_value: int, to_value: int) -> None:
        from_node: GraphNode = self._create_node(from_value)
        to_node: GraphNode = self._create_node(to_value)
        for vertex in from_node.edges:
            if vertex == to_node:
                return
        from_node.edges.append(to_node)
        
    def _create_node(self, value: int) -> GraphNode:
        """Creates node if not already there"""
        node: Optional[GraphNode] = self.search(value)
        if not node:
            node = GraphNode(value=value)
            self.vertices.append(node)
        return node

    def search(self, node_value: int) -> Optional[GraphNode]:
        for vertex in self.vertices:
            if vertex.value == node_value:
                return vertex
        return None

    def remove_edge(self, from_value: int, to_value: int) -> None:
        from_node: Optional[GraphNode] = self.search(from_value)
        to_node: Optional[GraphNode] = self.search(to_value)
        if not from_node or not to_node:
            raise ValueError('One or more vertices not found')
        from_node.edges.remove(to_node)

    def __str__(self) -> str:
        graph_values: List[str] = []
        for vertex in self.vertices:
            graph_values.append(str(vertex))
        return '\n'.join(graph_values)


if __name__ == '__main__':
    graph = Graph()
    print(graph)
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(3,5)
    graph.add_edge(3,1)
    graph.add_edge(3,1)
    graph.add_edge(1,3)
    graph.remove_edge(3,1)
    print(graph)


