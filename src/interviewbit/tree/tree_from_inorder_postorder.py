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
O(n) space 

In - in_order: List[int], post_order: List[int]
Out - TreeNode

"""
import collections
from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


Limit = collections.namedtuple('Limit', 'start end')


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, in_order: List[int], 
                  post_order: List[int]) -> Optional[TreeNode]:
        indexes: Dict[int, int] = {
            num: i for i, num in enumerate(in_order)
        }
        post_order_end: Dict[str, int] = {'val': len(post_order) - 1}
        return self.build_tree_helper(
            in_order, post_order, indexes,
            Limit(0, len(in_order) - 1), post_order_end,
        )

    def build_tree_helper(self, in_order: List[int], post_order: List[int], 
                          indexes: Dict[int, int], limit: Limit, 
                          po_end: Dict[str, int]) -> Optional[TreeNode]:
        """

        inor : [ 2, 1, 3 ]
        
        post : [ 2, 3, 1 ]

        limit 0 - 2
        limit 0 - 0, 2 - 2

        """
        if limit.start > limit.end:
            return None
        root_value: int = post_order[po_end['val']]
        root_index: Optional[int] = indexes.get(root_value, None)
        if root_index > limit.end or root_index < limit.start:
            return None
        po_end['val'] -= 1
        curr: TreeNode = TreeNode(root_value)
        curr.right = self.build_tree_helper(
            in_order, post_order, indexes,
            Limit(root_index + 1, limit.end), po_end
        )
        curr.left = self.build_tree_helper(
            in_order, post_order, indexes,
            Limit(limit.start, root_index - 1), po_end
        )
        return curr




