"""
Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

    Try to do it in constant space.

Can we edit the input
if so, just iterate count 0s and 1s


O(n) time where n = size list
O(1) space

"""
from typing import Iterator


class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, root: ListNode) -> ListNode:
        zeros: int = 0
        for node in self.get_nodes(root):
            if node.val == 0:
                zeros += 1
        for i, node in enumerate(self.get_nodes(root)):
            node.val = int(i < zeros)
        return root

    def get_nodes(self, root: ListNode) -> Iterator[ListNode]:
        while root is not None:
            yield root
            root = root.next

