############## Reverse linked List in place ###############
""" Iterate on the linked list keeping track of the latest value """
import dataclasses
from typing import Optional, Any


@dataclasses.dataclass
class Node:
    value: Any
    next: Optional['Node']


def revert(root: Node) -> Optional[Node]:
    curr: Optional[Node] = root
    last: Optional[Node] = None
    while curr:
        next: Optional[Node] = curr.next
        curr.next = last
        last = curr
        curr = next
    return last


def merge(list_a: Optional[Node], list_b: Optional[Node]) -> Optional[Node]:
    """ Remember to use an empty Node as a starting point """
    """ Merge two sorted lists into a resulting sorted list """
    result_root: Optional[Node] = Node(None, None)
    result_pointer: Optional[Node] = result_root
    while list_a and list_b:
        if list_a.value < list_b.value:
            result_pointer.next = list_a
            list_a = list_a.next
        else:
            result_pointer.next = list_b
            list_b = list_b.next
        result_pointer = result_pointer.next
    # Get any remaining items into the result list
    result_pointer.next = list_a if list_a else list_b
    
    return result_root.next
    


if __name__ == '__main__':
    linked_list = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    print(revert(linked_list))
    import pdb;pdb.set_trace()

