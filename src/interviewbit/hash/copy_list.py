"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list
          _
1 -> 2 -> 3
     _
1 -> 2

keep a visited 
    
last
root 

                    1
        2                       4                       
1           3               2   

dfs on the tree skiping visited nodes
receive two node from the elements bellow (next and random)
stop when no unvisited children is found
add a node and return 



with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1

You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.

O(n) time complexity 
O(n) space complexity cuz recursion


"""
from typing import List, Dict, Set, Optional


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head: RandomListNode) -> Optional[RandomListNode]:
        visited: Dict[int, RandomListNode] = dict()
        root = self.copy_list(head, visited)
        while head:
            if head.random:
                visited[head.label].random = visited[head.random.label]
            head = head.next
        return root

    def copy_list(self, head: RandomListNode, 
                  visited: Dict[int, RandomListNode]) -> Optional[RandomListNode]:
        if not head:
            return
        if head.label in visited:
            return visited[head.label]
        curr: RandomListNode = RandomListNode(head.label)
        visited[head.label] = curr
        next_copy, random_copy = None, None
        if head.next:
            next_copy = self.copy_list(head.next, 
                                                       visited)
        curr.next = next_copy
        return curr
