"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


have a result_head with next = head

keep a previous head as result_head

iterate keeping count of iterated elements % k
when we get to 0 (start by 1)
    save the next_node
    we make next = null,
    and reverse the list starting from prev_head.next,
    make prev_head.next = the new local_head and make
    the prev_head receive the end of the local list
    and make the local_end.next = next_node


O(n) time complexity
O(1) space complexity

In - head: ListNode, size: int
Out - head


"""
from typing import List, Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return node
        result_head: ListNode = ListNode(next=node)
        prev_head: ListNode = result_head
        count: int = 1
        while node:
            if count > 0:
                count = (count + 1) % k
                node = node.next
                continue
            next_node: ListNode = node.next
            node.next = None
            head, tail = reverse(prev_head.next)
            prev_head.next = head
            prev_head = tail
            tail.next = next_node
            node = next_node
            count = (count + 1) % k
        return result_head.next

def reverse(head: Optional[ListNode]) -> Tuple[Optional[ListNode], 
                                               Optional[ListNode]]:
    last_node: Optional[ListNode] = None
    tail: Optional[ListNode] = head
    while head:
        next_node: ListNode = head.next
        head.next = last_node
        last_node = head
        head = next_node
    return last_node, tail



