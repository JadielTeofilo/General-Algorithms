import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    value: Optional[int] = None
    next: Optional['Node'] = None
    

def sum(left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
    """ 
        Does the sum between two numbers, 
        represented as linked lists right and left
    """
    if not left and not right:
        return
    if not left or not right:
        return left or right
    
    left_node: Optional[Node] = left
    right_node: Optional[Node] = right
    result: Optional[Node] = Node()
    result_node: Optional[Node] = result
    goes: int = 0
    
    while left_node and right_node:
        current_sum: int = left_node.value + right_node.value + goes
        goes = 1 if current_sum > 9 else 0
        current_sum %= 10
        result_node = update_result(result_node, current_sum)
        right_node = right_node.next
        left_node = left_node.next
        
    if left_node or right_node:
        result_node.next = left_node or right_node
    
    if goes == 1:
        update_result(result_node, 1)
    
    return result.next


def update_result(result: Optional[Node], value: int) -> Optional[Node]:
    if not result:
        return
    if not result.next:
        result.next = Node(value=value)
        result = result.next
    else:
        result = result.next
        result.value += value
        
    return result


left = Node(7, Node(1, Node(6)))
right = Node(5, Node(9, Node(2)))

print(sum(left, right))

left = Node(7, Node(1, Node(6)))
right = Node(4)

print(sum(left, right))

left = Node(7, Node(1, Node(6)))
right = Node(4, Node(3))

print(sum(left, right))

left = Node(9, Node(7, Node(8)))
right = Node(6, Node(8, Node(5)))

print(sum(left, right))
