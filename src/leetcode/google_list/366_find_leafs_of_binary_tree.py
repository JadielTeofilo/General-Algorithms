"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.


What we want is to map the distance each node has to the leaves

List[List[int]]

Iterate on the tree keeping track of the distance to the leaves
Ones with distance zero go to the position 0 of the list and so on

recusion stops when node is null, and returns 0
after using current, return the distance + 1 to the parent


O(n) time complexity where n is the number of nodes
O(h) space complexity depth of the tree

In - root: TreeNode
Out - List[List[int]]

"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []
        self.find_leaves_helper(root, result)
        return result

    def find_leaves_helper(self, root: Optional[TreeNode], 
                           result: List[List[int]]) -> int:
        if not root:
            return 0
        distance_to_leaves: int = max(
            self.find_leaves_helper(root.left, result),
            self.find_leaves_helper(root.right, result),
        )
        if distance_to_leaves == len(result):
            result.append([])
        result[distance_to_leaves].append(root.val)
        return distance_to_leaves + 1



