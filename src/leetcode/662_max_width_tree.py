"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


do a regular dfs keeping track of levels and distance from mid
have a list of MaxMin objects, update them as you go and update result along the way


O(n) time complexity where n is the num of nodes
O(d) space complexity where d is the depth of the tree

"""
import dataclasses
import math
from typing import Optional, List, Tuple, Union, Iterator


DfsInfo = Tuple[TreeNode, int, int]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclasses.dataclass
class MaxMin:
    min_distance: Union[int, float] = math.inf
    max_distance: Union[int, float] = -math.inf

    def get_diff(self) -> int:
        return self.max_distance - self.min_distance


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result: int = 0
        levels: Dict[int, MaxMin] = collections.defaultdict(MaxMin)
        for node, level, distance in tree_dfs(root, 0, 0):
            max_min: MaxMin = levels[level]
            update_max_min(max_min, distance * level - 1)
            if both_set(max_min):
                result = max(result, max_min.get_diff())
        return result


def tree_dfs(root: Optional[TreeNode], level: int,
             distance: int) -> Iterator[DfsInfo]:
    if not root:
        return
    yield from tree_dfs(root.left, level + 1, distance - 1)
    yield root, level, distance
    yield from tree_dfs(root.right, level + 1, distance + 1)



def update_max_min(max_min: MaxMin, value) -> None:
    max_min.max_distance = max(max_min.max_distance, value)
    max_min.min_distance = min(max_min.min_distance, value)


def both_set(max_min: MaxMin) -> bool:
    return (max_min.max_distance != -math.inf and
            max_min.min_distance != math.inf)

