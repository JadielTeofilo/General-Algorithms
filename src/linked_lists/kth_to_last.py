import dataclasses
from typing import Optional, Union


@dataclasses.dataclass
class Node:
    value: int
    next: Optional['Node']
    

def kth_to_last(root: Optional[Node], k: int) -> Node:
    if not root or k <= 0:
        raise ValueError('Incorrect input')
    slow_pointer: Node = root
    # Move the fast pointer to the starting position
    fast_pointer: Optional[Node] = move_pointer(root, k)  # TODO implement
    
    while fast_pointer:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
        
    return slow_pointer


def move_pointer(node: Optional[Node], times: int) -> Optional[Node]:
    while times > 0: 
        if not node:
            raise ValueError('Position outside list')
        times -= 1
        node = node.next
    return node


def kth_to_last_recursive(root: Optional[Node], k: int) -> Union[Node, int]:
    if not root:
        return k
    result: Union[Node, int] = kth_to_last_recursive(root.next, k)
    if isinstance(result, int):
        if result <= 1:
            return root
        return result - 1
    else:
        return result


import pdb;pdb.set_trace()
