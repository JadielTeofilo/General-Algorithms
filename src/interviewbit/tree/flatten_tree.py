"""

Given a binary tree, flatten it to a linked list in-place.

Example :

Given


     1
      \   \
       2    5
        \    \
        3    6
        4


for a given node we want 
old_right = node.right
node.right = node.left
node.left = None
update right with old_right
    iterate on the new right and set the last node.right with the desired nodes


                    1 
                2       5
            3
              4


The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Note that the left child of all nodes should be NULL.


O(n) time complexity where n is nodes
O(1) space

"""
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        old_right: Optional[TreeNode] = root.right
        root.right = root.left
        root.left = None
        self.update_leaf(root, old_right)
        return root

    def update_leaf(self, node: Optional[TreeNode], 
                    new_leaf: Optional[TreeNode]) -> None:
        while node is not None and node.right is not None:
            node = node.right
        if node:
            node.right = new_leaf

                
