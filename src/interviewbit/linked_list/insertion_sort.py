"""

Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3



start with an empty list, if empty, add to it, else, look for the place to insert


O(n^2) time complexity
O(1) space


In - root: ListNode
Out - ListNode

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, root: ListNode) -> ListNode:
        result: ListNode = ListNode(None)
        new_root: ListNode = result
        while root:
            aux: ListNode = root.next
            self.insert(root, result)
            root = aux
        return new_root.next

    def insert(self, node: ListNode, result: ListNode) -> None:
        while result.next:
            if result.next.val > node.val:
                aux: ListNode = result.next
                result.next = node
                node.next = aux
                return
            result = result.next
        else:
            result.next = node
            node.next = None
            

