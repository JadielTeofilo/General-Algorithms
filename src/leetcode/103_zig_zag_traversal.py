"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


                1
        2               3
4                   5       6
    7            8      9

1
3 2
4 5 6
9 8 7

regular bfs with a queue
uses a separete queue for each level to put the level elements


1 0 
2 1 3 1

every odd level should be inserted inverted on the output



"""
import collections
from typing import List, Optional, Union, Deque, Iterator, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Result = List[Union[Deque[int], List[int]]]
QueueData = Tuple[TreeNode, int]


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: Result = []
        for node, level in bfs_traversal(root):  
            if level == len(result):
                if len(result) > 0:
                    result[level - 1] = list(result[level - 1])
                result.append(collections.deque())
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)
        return result


def bfs_traversal(node: Optional[TreeNode]) -> Iterator[QueueData]:
    if not node:
        return []
    queue: Deque[QueueData] = collections.deque([(node, 0)])
    while queue:
        curr, level = queue.popleft()
        if not curr:
            continue
        yield curr, level
        queue.append((curr.left, level + 1))
        queue.append((curr.right, level + 1))


