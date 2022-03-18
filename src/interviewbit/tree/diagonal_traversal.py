"""
Consider lines of slope -1 passing between nodes.

Given a Binary Tree A containing N nodes, return all diagonal elements in a binary tree belonging to same line.

NOTE:

    See Sample Explanation for better understanding.
    Order does matter in the output.
    To get the same order as in the output traverse the tree same as we do in pre-order traversal.


Input 1:

            1
          /   \
         4      2
        / \      \
       8   5      3
          / \    /
         9   7  6

Output 1:

 [1, 2, 3, 4, 5, 7, 6, 8, 9]

Theory
If we know how deep to the left each node went we know which diagonal it bellongs

Have a hash add the new info to the graph, hash the value of the node


iterate inorder traversal putting each node on each array

return the merge of the arrays

O(n) time where n is num of nodes
O(n) space

"""
import collections
from typing import List, Dict, Optional


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root: Optional[TreeNode]) -> List[int]:
        node_meta: Dict[int, List[int]] = collections.defaultdict(list)
        self.build_meta(root, node_meta)
        result: List[int] = []
        for diag in range(max(node_meta) + 1):
            result.extend(node_meta[diag])
        return result

    def build_meta(self, node: Optional[TreeNode], meta: Dict[int, List[int]], 
                   diagonal: int = 0) -> None:
        if not node:
            return
        self.build_meta(node.left, meta, diagonal + 1)
        meta[diagonal].append(node.val)
        self.build_meta(node.right, meta, diagonal)
        
        

        

