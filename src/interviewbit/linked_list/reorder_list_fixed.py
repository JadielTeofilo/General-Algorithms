"""
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,

reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You must do this in-place without altering the nodes’ values.

For example,

Given {1,2,3,4}, reorder it to {1,4,2,3}.


Notice that the mapping is the same of what a palindrome check does
just revert the second half of list and match with first



"""
from typing import List, Iterator, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, root: ListNode) -> Optional[ListNode]:
        mid: ListNode = self.find_mid(root)
        new_mid: ListNode = self.reverse(mid.next)
        mid.next = None
        new_root: ListNode = ListNode(0)
        last: ListNode = new_root
        # 1 2    5 4 3 
        # 1 5 2 4 
        for left, right in zip(self.iterate(root),
                               self.iterate(new_mid)):
            last.next = left
            left.next = right
            last = right
        return new_root.next
    
    def find_mid(self, node: ListNode) -> ListNode:
        slow, fast = node, node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, node: ListNode) -> ListNode:
        last: Optional[ListNode] = None
        while node:
            aux: ListNode = node.next
            node.next = last
            last = node
            node = aux
        return last

    def iterate(self, node: ListNode) -> Iterator[ListNode]:
        while node is not None:
            aux: ListNode = node.next
            yield node
            node = aux
