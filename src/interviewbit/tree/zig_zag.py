"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example :

Given binary tree

    3
   / \
  9  20
    /  \
   15   7
 2   4 3  5


Use bfs and keep track of the levels

have a queue with the root
pop from queue
add curr to answer
add children to queue

iterate on the answer and reverse the desired indexes

O(n) time where n = num nodes
O(w) where w is the width of the tree since that is the max size at a given moment on the queue



In - root: TreeNode
"""
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

QueueNode = collections.namedtuple('QueueNode', 'node level')


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        deque = collections.deque()
        deque.append(QueueNode(root, 0))
        result: List[List[int]] = []
        while deque:
            curr, level = deque.popleft()
            if curr is None:
                continue
            if level == len(result):
                result.append([])
            result[level].append(curr.val)
            deque.append(QueueNode(curr.left, level + 1))
            deque.append(QueueNode(curr.right, level + 1))
        self.reverse_odds(result)
        return result

    def reverse_odds(self, numbers: List[List[int]]) -> None:
        for index, nums in enumerate(numbers):
            if index % 2 != 0:
                nums.reverse()






