"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
   \
    4
The root-to-leaf path 1->2 represents the number 12.

The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.


we need to do a tree traversal
we need to pass down the curr number * 10 + the curr digit
when we get to a leaf, just add curr to the total % 1003

O(n) time complexity where n is nodes
O(log n) space where n is the num of nodes, caused by the recursion 

In - root: TreeNode
Out - int

"""
from typing import List, Dict, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, root: TreeNode) -> int:
        result: Dict[str, int] = {'count': 0}
        self.build_result(root, result, curr=0)
        return result['count']

    def build_result(self, node: Optional[TreeNode], 
                     result: Dict[str, int], curr: int) -> None:
        if not node:
            return 
        new_curr: int = curr * 10 + node.val
        if node.left is None and node.right is None:
            result['count'] = (result['count'] + new_curr) % 1003
        self.build_result(node.left, result, new_curr)
        self.build_result(node.right, result, new_curr)



