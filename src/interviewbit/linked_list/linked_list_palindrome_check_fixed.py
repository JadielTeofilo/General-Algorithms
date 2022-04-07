"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

    Expected solution is linear in time and constant in space.

For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.


We know how to reverse a linked list in place, so reverse the second half and compare it

find mid of list

reverse from mid
with the new mid compare with root

O(n) time where n is the size of list
O(1) space



"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def lPalin(self, root: ListNode) -> int:
        mid: ListNode = self.find_mid(root)
        new_mid: ListNode = self.reverse(mid)
        return int(self.compare(new_mid, root))

    def find_mid(self, node: ListNode) -> ListNode:
        slow, fast = node, node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, node: ListNode) -> ListNode:
        last: ListNode = None
        while node:
            aux: ListNode = node.next
            node.next = last
            last = node
            node = aux
        return last

    def compare(self, first: ListNode, second: ListNode) -> bool:
        while first is not None and second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
