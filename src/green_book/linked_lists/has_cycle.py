import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    value: Optional[int] = None
    next: Optional['Node'] = None
    
    
def find_cycle_initiator(root: Node) -> Node:
    if not root:
        raise ValueError('List is empty')
    
    collision: Node = find_collision_point(root)
    # From the collision point there is K nodes to the start of the cycle
    # just like there is K nodes from the root to the start of the cycle
    while True:
        if collision == root:
            return collision
        collision = collision.next
        root = root.next
    
    
def find_collision_point(root: Node) -> Node:
    fast_pointer: Node = root
    slow_pointer: Node = root
    while fast_pointer.next and fast_pointer.next.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if fast_pointer == slow_pointer:
            return fast_pointer
    raise ValueError('List has no cycle')
    
    
test = Node(1, Node(2, Node(3, Node(4))))
test.next.next.next.next = test.next
print(find_cycle_initiator(test))
import pdb;pdb.set_trace()
