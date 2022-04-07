"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,

Given 1->4->3->2->5->2 and x = 3,

return 1->2->2->4->3->5.


say we iterate on the nodes

keep two linked lists

smaller and bigger and equal
have a root for each and an iterable

take a given node and add to the respective list

at the end add the equal to end of smaller and bigger to the end o equal, return root of smaller


O(n) time where n num of nodes
O(1) space

"""
import dataclasses
from typing import Iterator


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

@dataclasses.dataclass
class Iterators:
    smaller: ListNode
    bigger: ListNode


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, root: ListNode, target: int) -> ListNode:
        roots: Iterators = Iterators(
            ListNode(-1), ListNode(-1)
        )
        iters: Iterators = Iterators(
            roots.smaller, roots.bigger
        )
        for node in self.get_nodes(root):
            if node.val < target:
                iters.smaller.next = node
                iters.smaller = node
            else:
                iters.bigger.next = node
                iters.bigger = node
        iters.smaller.next = roots.bigger.next
        iters.bigger.next = None
        return roots.smaller.next

    def get_nodes(self, root: ListNode) -> Iterator[ListNode]:
        while root is not None:
            yield root
            root = root.next

            

