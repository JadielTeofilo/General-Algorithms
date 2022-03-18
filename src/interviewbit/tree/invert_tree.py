"""
Given a binary tree A, invert the binary tree and return it.

 Inverting refers to making left child as the right child and vice versa.


iterate on nodes
postorder
stop when not node
curr.left, curr.right = curr.left, curr.right


O(n) time where n = nodes
O(log n) space from recursion n = nodes

"""
from typing import Optional


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


