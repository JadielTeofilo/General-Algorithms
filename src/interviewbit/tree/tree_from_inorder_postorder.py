"""
Given inorder and postorder traversal of a tree, construct the binary tree.

    Note: You may assume that duplicates do not exist in the tree.

Example :

Input : 
        Inorder : [2, 3, 1, 4]
        Postorder : [3, 2, 4, 1]

Return : 
              1 
          2      4
            3 

the last element is the root
split the inorder with the root
for the post order, check if there is a left side, if so send the nums[:-1] to left and nums[:-2] to right


O(n) time complexity
O(1) space 

In - in_order: List[int], post_order: List[int]
Out - TreeNode

"""
import collections
from typing import List


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


Boundery = collections.namedtuple('Boundery', 'start end')


class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, in_order: List[int], 
                      post_order: List[int]) -> TreeNode:
            return self.build_from_orders(
                boundery_in=Boundery(0, len(in_order) - 1), in_order, 
                boundery_post=Boundery(0, len(post_order) - 1), post_order
            )
    
        def build_from_order(
            self, boundery_in: Boundery, in_order: List[int],
            boundery_post: Boundery, post_order: List[int]
        ) -> TreeNode:
            if boundery_in.start > boundery_in.end:
                return None
            root_val: int = post_order[boundery_post.end]
            root_index: int = bisect.bisect_left(in_order, root_val)
            current: TreeNode = TreeNode(root_val)
            current.left = self.build_from_order(
                Boundery(boundery_in.start, root_index - 1), in_order, 
                Boundery(boundery_post.start, boundery_post.end - 1), 
                post_order
            )
            new_boundery_post_end: int = (boundery_post.end - 
                                          (2 if current.left else 2))
            current.right = self.build_from_order(
                Boundery(root_index + 1, boundery_in.end), in_order, 
                Boundery(), post_order
            )
            return current
            
            

