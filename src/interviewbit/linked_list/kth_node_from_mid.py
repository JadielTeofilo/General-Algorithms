"""


You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

If no such element exists, then return -1.

NOTE:

    Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.


1 -> 2 -> 3 -> 4 -> 5 -> 6
          _                 _


Find mid with slow and fast pointers
keep the last B elements with queue


Iterate two pointers
    stop when fast is null or fast.next is null

    the slow is the mid then
    add elements to queue, pop if bigger then B

return first popleft of queue


O(n) time complexity where n is the size of the list
O(B) space where b is the size of the target

Possible to do O(1) space but it would be slower (traverse twice)


In ListNode, int
Out int


"""
import collections
from typing import Deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, root: ListNode, kth: int) -> int:
        """
            A : [ 468 -> 335 ]
                         _
            B : 1
        """
        fast, slow = root, root
        deque: Deque[int] = collections.deque([root.val])
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            deque.append(slow.val)
            if len(deque) > kth + 1:
                deque.popleft()
        if len(deque) != kth + 1:
            return -1
        return deque.popleft()


