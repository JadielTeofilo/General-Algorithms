"""
Given a binary tree, return the reverse level order traversal of its nodes values. (i.e, from left to right and from last level to starting level).




                1
    2                     3
4       5                        6



Use bfs to iterate on the tree, keep track of the level
normal bfs prints from top down
we pop from the queue and use curr value



have a dict from level to values, fill it, then just iterate on it from last level to first





In - root: TreeNode
Out - List[int]
"""
import collections
from typing import List, Dict, Optional, Iterable


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root: Optional[TreeNode]) -> Iterable[int]:
        levels: Dict[int, List[int]] = collections.defaultdict(list)
        self.fill_levels(root, levels)
        if not levels:
            return []
        max_level: int = max(levels)
        for level in range(max_level, -1, -1):
            yield from levels[level]

    def fill_levels(self, root: Optional[TreeNode], 
                    levels: Dict[int, List[int]], level=0) -> None:
        if not root:
            return
        self.fill_levels(root.left, levels, level + 1)
        self.fill_levels(root.right, levels, level + 1)
        levels[level].append(root.val)

        
