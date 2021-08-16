import dataclasses
from typing import Optional, List


@dataclasses.dataclass
class Node:
    value: Optional[int] = None
    next: Optional['Node'] = None
    
    
def find_intersection(left: Node, right: Node) -> Optional[Node]:
    if not left or not right:
        raise ValueError('One or more empty inputs')
    
    left_stack: List[Node] = build_stack_from_list(left)
    right_stack: List[Node] = build_stack_from_list(right)
    
    return find_intersection_from_stacks(left_stack, right_stack)


def build_stack_from_list(root: Node) -> List[Node]:
    stack: List[Node] = []
    pointer: Optional[Node] = root
    while pointer:
        stack.append(pointer)
        pointer = pointer.next
    return stack


def find_intersection_from_stacks(left_stack: List[Node], 
                                  right_stack: List[Node]) -> Optional[Node]:
    # If there is an intersection, the last element is the same
    if left_stack[-1] != right_stack[-1]:
        return None
    
    last_visited: Optional[Node] = None
    
    while left_stack and right_stack:
        left_node: Node = left_stack.pop()
        right_node: Node = right_stack.pop()
        
        if left_node != right_node:
            return last_visited
        
        last_visited = left_node  # Can be any of the two, they`re the same
        
    return None  # If its the same list
    

inter = Node(4, Node(5, Node(6)))

left = Node(1, Node(2, Node(3, Node(4, inter))))

right = Node(10, Node(12, inter))

print(find_intersection(left, right))
