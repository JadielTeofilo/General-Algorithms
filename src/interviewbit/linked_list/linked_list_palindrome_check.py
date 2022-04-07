"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

    Expected solution is linear in time and constant in space.

For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.

With recursion:
have an iterator for the list
and a reversed

iterate comparing

O(n) time 
O(n) space from recursion stack

In - list_node: ListNode
Out - int


"""
from typing import Iterator


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, root: ListNode) -> int:
        for left, right in zip(self.iterate(root), 
                               self.iterate_rev(root)):
            if left == right:
                break
            if left.val != right.val:
                return 0
        return 1

    def iterate(self, node: ListNode) -> Iterator[ListNode]:
        while node:
            yield node
            node = node.next
                        
    def iterate_rev(self, node: ListNode) -> Iterator[ListNode]:
        if node.next is None:
            return [node]
        yield from self.iterate_rev(node.next)
        yield node


        
