"""
Given a linked list A of length N and an integer B.

You need to reverse every alternate B nodes in the linked list A.

1 2 3   4 5 6   7
3 2 1   6 4 5   7

keep track of the first of the cycle
keep index of elements


list of heads 

reverse every 3


"""
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, root: Optional[ListNode], window: int) -> Optional[ListNode]:
        if not root:
            return
        heads: List[ListNode] = self.split_list(root, window)
        for index, head in enumerate(heads):
            if index % 2 != 0:
                continue
            heads[index] = self.reverse(head)
        self.merge(heads)
        return heads[0]
            
    def split_list(self, node: ListNode, window: int) -> List[ListNode]:
        index: int = 0
        split: List[ListNode] = []
        last: Optional[ListNode] = None
        while node:
            if index % window == 0:
                split.append(node)
                if last is not None:
                    last.next = None
            last = node
            index += 1
            node = node.next
        return split

    def reverse(self, node: ListNode) -> ListNode:
        last: Optional[ListNode] = None
        while node:
            aux: Optional[ListNode] = node.next
            node.next = last
            last = node
            node = aux
        return last

    def merge(self, heads: List[ListNode]) -> None:
        for index, head in enumerate(heads):
            if index + 1 >= len(heads):  
                continue
            self.get_last(head).next = heads[index + 1]

    def get_last(self, node: ListNode) -> ListNode:
        while node.next:
            node = node.next
        return node
            
                
            
            
