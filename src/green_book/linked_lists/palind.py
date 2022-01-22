from typing import Optional
import dataclasses


@dataclasses.dataclass
class Node:
    value: Optional[str] = None
    next: Optional['Node'] = None
    

def is_palindrome(root: Node) -> bool:
    result: Optional[bool] = is_palindrome_helper(root=Node(next=root), curr_node=root)
    print(root)
    return bool(result)


def is_palindrome_helper(root: Node, curr_node: Optional[Node]) -> Optional[bool]:
    if not curr_node:
        return None
    result: Optional[bool] = is_palindrome_helper(root, curr_node.next)
    if isinstance(result, bool):
        return result
    left: Node = root.next
    right: Optional[Node] = curr_node
    # Case when pointers are at the same node
    if left == right:
        return True
    if left.value != right.value:
        return False
    # Case when pointers are next to each other
    if left.next == right:
        return True
    root.next = left.next
    return None


print(is_palindrome(Node('a')))
print(is_palindrome(Node('a', Node('b'))))
print(is_palindrome(Node('a', Node('b', Node('a')))))
print(is_palindrome(Node('a', Node('b', Node('a', Node('b'))))))
print(is_palindrome(Node('a', Node('b', Node('b', Node('a'))))))
