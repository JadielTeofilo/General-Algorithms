"""
Given a binary tree A consisting of N nodes, return a 2-D array denoting the vertical order traversal of A.

Go through the example and image for more details.

NOTE:

    If 2 or more Tree Nodes shares the same vertical level then the one with earlier occurence in the level-order traversal of tree comes first in the output.
    Row 1 of the output array will be the nodes on leftmost vertical line similarly last row of the output array will be the nodes on the rightmost vertical line.


We need to keep track of the number of left moves it makes, and number of right moves
use a dict to group the elements
use queue to treverse the tree bfs style
turn dict into list (iterate from min key to max key)


O(n) time complexity
O(w) space where w is the width of the tree


"""
import collections
from typing import List, Optional, Dict


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


QueueNode = collections.namedtuple('QueueNode', 'node level')


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        deque = collections.deque()
        deque.append(QueueNode(root, 0))
        levels: Dict[int, List[int]] = collections.defaultdict(list)
        while deque:
            node, level = deque.popleft()
            if not node:
                continue
            levels[level].append(node.val)
            deque.append(QueueNode(node.left, level - 1))
            deque.append(QueueNode(node.right, level + 1))
        return self.build_result(levels)

    def build_result(self, levels: Dict[int, List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        min_level: int = min(levels)
        max_level: int = max(levels)
        for level in range(min_level, max_level + 1):
            result.append(levels[level])
        return result

