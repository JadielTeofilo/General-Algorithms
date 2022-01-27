"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.


"""
from typing import Optional, List, Tuple, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Pairs = List[Tuple[Optional[TreeNode], Optional[TreeNode]]]


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        pairs: Pairs = []
        self.fill_pairs(root, pairs, last={'node': None})
        if len(pairs) == 1:
            pairs[0][0].val, pairs[0][1].val = pairs[0][1].val, pairs[0][0].val
        else:
            pairs[0][0].val, pairs[1][0].val = pairs[1][0].val, pairs[0][0].val
    
    def fill_pairs(self, root: Optional[TreeNode], 
                   pairs: Pairs, 
                   last: Dict[str, Optional[TreeNode]]) -> None:
        if not root:
            return
        self.fill_pairs(root.left, pairs, last)
        if last['node'] is not None and last['node'].val > root.val:
            pairs.append((last['node'], root))
        last['node'] = root
        self.fill_pairs(root.right, pairs, last)
        
