"""
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,

reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You must do this in-place without altering the nodes’ values.

For example,

Given {1,2,3,4}, reorder it to {1,4,2,3}.


lets say we have a pointer for each of the matched elements
left right

we make left.next = right
last.next = left
(we create a dummy left at the start)
return result.next

we iterate on the linked list 
iterate(root)
    while root
        aux = root.next
        yield root
        root = aux


O(n) time where n is the size of the linked list
O(n) space on the recursion stack


"""
from typing import List, Iterator, Optional


class ListNode:
    def __init__(self, x):
	self.val = x
	self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, root: ListNode) -> ListNode: 
        new_root: ListNode = ListNode(0)
        last: ListNode = new_root
        # 1 2 3 4 5 6 7
        # 1 7 2 6 3 5 
        for left, right in zip(self.iterate(root),
                               self.iterate_rev(root)):
            if last == right:
                last.next = left
                break
            last.next = left
            left.next = right
            right.next = None
            last = right
        return new_root.next

    def iterate(self, node: ListNode) -> Iterator[ListNode]:
        while node:
            aux: Optional[ListNode] = node.next
            yield node
            node = aux

    def iterate_rev(self, node: ListNode) -> Iterator[ListNode]:
        if node.next is None:
            yield node
            return
        yield from self.iterate_rev(node.next)
        yield node


