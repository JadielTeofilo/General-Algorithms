"""
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5



when curr has no next, return curr
get mid element and split lists

call divive_conquer on first half and second half


build a merge function

    while both
        pick the smallest to put on the result

    if any of both is not null, use it



O(nlogn) time complexity
O(logn) space complexity where n is the size of the list



"""
from typing import Optional


class ListNode:

    def __init__(self, x):      
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, root: ListNode) -> ListNode:
        if not root or not root.next:
            return root
        mid: ListNode = self.split_in_half(root)
        return self.merge(self.sortList(root), self.sortList(mid))

    def split_in_half(self, root: ListNode) -> ListNode:
        slow, fast = root, root
        last: Optional[ListNode] = None
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.fast.next
        if last is not None:
            last.next = None
        return slow
        
    def merge(self, first: ListNode, second: ListNode) -> ListNode:
        result: ListNode = ListNode(None)
        new_root: ListNode = result
        while first is not None and second is not None:
            if first.val <= second.val:
                result.next = first
                first = first.next
            else:
                result.next = second
                second = second.next
            result = result.next
        result.next = first or second
        return new_root.next
