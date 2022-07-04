"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)




1 -> 2 -> 3

2 -> 1 -> 3


1 2 3 4 5

2 1 3 4 5

create a new result_head: ListNode and make it the new prev
curr receives head

while curr.next

next_node = curr.next  # 2
curr.next = next_node.next  # 1 -> 3
next_node.next = curr # 2 -> 1
prev.next = next_node # head -> 2

curr = curr.next

1 3

2 1 4 3 5

O(n) where n is the size of the linked list




"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_head: Optional[ListNode] = ListNode(next=head)
        prev: Optional[ListNode] = result_head
        curr: Optional[ListNode] = head
        while curr and curr.next:
            next_node: ListNode = curr.next
            curr.next = next_node.next
            next_node.next = curr
            prev.next = next_node
            prev = curr
            curr = curr.next
        return result_head.next

