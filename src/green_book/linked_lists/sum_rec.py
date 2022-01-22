import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    value: Optional[int] = None
    next: Optional['Node'] = None
    

def reverse_list(root: Node) -> Node:
    
    previous_element: Optional[Node] = None
    node: Optional[Node] = root
    
    while node:
        next: Optional[Node] = node.next
        node.next = previous_element
        previous_element = node
        node = next
        
    return previous_element
    

left = Node(7, Node(1, Node(6)))
right = Node(5, Node(9, Node(2)))

print(reverse_list(left))
print(reverse_list(right))
