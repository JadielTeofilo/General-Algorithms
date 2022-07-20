"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.



                        1 0
            2 0                         7 1
    3 0                         3 2                 8 3
        3 1               2 4         2 5                 1 7

better to think which index a given node is on its level

keep track of the level
parent_index * 2
parent_index * 2 + 1

have a list for levels with max and min values

"""
import dataclasses
import sys
from typing import List, Optional


INF = sys.maxsize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclasses.dataclass
class Level:
    max_index: int = -INF
    min_index: int = INF


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels: List[Level] = []
        fill_levels(root, levels, 0, 0)
        result: int = 1
        return max([level.min_index - level.max_index + 1 
                    for level in levels])


def fill_levels(
    root: Optional[TreeNode], levels: List[Level], 
    node_index: int, level_index
) -> None:
    if not root:
        return
    if len(levels) == level_index:
        levels.append(Level())
    fill_levels(root.left, levels, node_index * 2, level_index + 1)
    levels[level_index].max_index = max(
        levels[level_index].max_index, node_index
    )
    levels[level_index].min_index = min(
            levels[level_index].min_index, node_index
    )
    fill_levels(root.right, levels, node_index * 2 + 1, level_index + 1)



