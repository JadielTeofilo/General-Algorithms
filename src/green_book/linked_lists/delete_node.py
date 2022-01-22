import dataclasses
from typing import Optional



@dataclasses.dataclass
class Node:
    value: int
    next: Optional['Node']
    
    
def delete_node(node: Node) -> None:
    if not node.next:
        raise ValueError('Node has to be a middle node')
    next_node: Node = node.next
    node.value = next_node.value
    node.next = next_node.next
    del next_node


import pdb;pdb.set_trace()
