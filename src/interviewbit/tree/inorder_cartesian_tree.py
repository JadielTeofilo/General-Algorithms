"""
Given an inorder traversal of a cartesian tree, construct the tree.

    Cartesian tree :  is a heap ordered binary tree, where the root is greater than all the elements in the subtree.

    Note: You may assume that duplicates do not exist in the tree.

Example :

Input : [1 2 8]

Return :   
          8
         /
        2     7
       /
      1      5


the normal way to insert on a heap is to insert on the last level on the first empty space from left to right

The main point is to notice that the root is the biggest element from the list
Find it, then just call the recursion on each side

O(n log n) time complexity where n is size of list, we will go on every node
O(logn) space due to recursion

"""
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, nums: List[int], start=0, end=None) -> Optional[TreeNode]:
        if end is None:
            end = len(nums)
        if start == end:
            return
        index_of_max: int = nums.index(max(nums[start:end]))  # TODO improve this
        curr: TreeNode = TreeNode(nums[index_of_max])
        curr.left = self.buildTree(nums, start, index_of_max)
        curr.right = self.buildTree(nums, index_of_max + 1, end)
        return curr

        


