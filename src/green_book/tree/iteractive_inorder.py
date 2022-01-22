######## DFS of Tree with a stack ##########
from typing import Optional, List, Set
import dataclasses


@dataclasses.dataclass
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def iteractive_in_order(root: Node) -> None:
    """ Does an iteractive DFS and returns
            the stack when value is found """
    stack: List[Node] = []
    stack.append(root)
    visited: Set[int] = set()
    # Does Iteractive DFS
    while stack:
        node: Node = stack[-1]
        if node.left and node.left.value not in visited:
            stack.append(node.left)
            continue
        print(node.value)
        visited.add(node.value)
        stack.pop()
        if node.right and node.right.value not in visited:
            stack.append(node.right)


root = Node(3, Node(7, Node(1)), Node(2, Node(5, Node(4, None, Node(6))), Node(9)))
iteractive_in_order(root)
