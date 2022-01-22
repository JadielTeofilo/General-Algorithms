"""
in: Node pointer

out: None

set 

"""
import dataclasses
from typing import Set, Optional
import unittest


@dataclasses.dataclass
class Node:
    value: int
    next: Optional['Node']


def remove_duplicates(root: Node) -> Node:
    if not root:
        return
    visited: Set[int] = set()
    node: Optional[Node] = root
    last_node: Optional[Node] = None
    while node:
        if node.value in visited:
            remove_node(node, last_node)  # TODO implement it
            node = last_node.next
        else:
            visited.add(node.value)
            last_node = node
            node = node.next
    return root


def remove_node(node_to_remove: Node, previous_node: Node) -> None:
    next: Node = node_to_remove.next
    previous_node.next = next
    del node_to_remove
    

class Test(unittest.TestCase):
    
    def test(self) -> None:
        self.assertEqual(remove_duplicates(Node(1, Node(2, Node(3, Node(1, Node(3, None)))))), 
                         Node(1, Node(2, Node(3, None))))


if __name__ == '__main__':
    unittest.main()
        

