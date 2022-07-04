"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



2 3 6 9

4 8 9 10

1 2 3


use a divide and conquer approach, its just like merge sort when we get to the end 

call a merge function for every two lists
keep doing this until there is only one list


time complexity of merging two lists of size n and m is O(n) where n is the size of the bigger list
n n n n n n
 m   m   m
   v   m
     g

O(m log k) where m is the size of all lists combined and k is the size of the lists


Another approach is to use a heap to get the min element every time, put all first elements on the heap, after you use a element, you put the next one of that heap in the line

"""
import collections
import heapq
from typing import List, Optional


HeapValue = collections.namedtuple('HeapValue', 'val node')


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        heap: List[HeapValue] = get_heap(lists)
        result: ListNode = ListNode()
        result_head: ListNode = result
        while heap:
            val, node = heapq.heappop(heap)
            result.next = node
            if node.next:
                heapq.heappush(
                    heap, 
                    HeapValue(node.next.val, node.next)
                )
            node.next = None
            result = result.next
        return result_head.next


def get_heap(lists: List[Optional[ListNode]]) -> List[HeapValue]:
    heap: List[HeapValue] = []
    for root in lists:
        heap.append(HeapValue(root.val, root))  #TODO fix this, you cant heap tuples with objects
    heapq.heapify(heap)
    return heap



