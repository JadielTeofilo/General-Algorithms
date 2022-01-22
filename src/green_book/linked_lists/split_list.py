import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    
    value: int
    next: Optional['Node']


@dataclasses.dataclass
class LinkedList:
    
    start: Optional[Node] = None
    end: Optional[Node] = None
    
    def insert_at_the_end(self, node: Node) -> None:
        if self.end:
            self.end.next = node
            self.end = self.end.next
        else:
            self.start = node
            self.end = node
    
    
def split_list(linked_list: LinkedList, partition: int) -> Node:
    node: Optional[Node] = linked_list.start
    if not node:
        raise ValueError('Invalid Empty list')
    left_list: LinkedList = LinkedList()
    right_list: LinkedList = LinkedList()
    while node:
        next = node.next
        node.next = None
        if node.value < partition:
            left_list.insert_at_the_end(node)
        else:
            right_list.insert_at_the_end(node)
        node = next
    result: LinkedList = merge_lists(left_list, right_list)
    return result.start
    
    
def merge_lists(left: LinkedList, right: LinkedList) -> LinkedList:
    left.end.next = right.start
    return left


asdf = LinkedList()
asdf.insert_at_the_end(Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1, None))))))))
print(asdf.start)
print(split_list(asdf, 5))
