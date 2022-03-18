"""
Given a Binary Tree A consisting of N nodes.

You need to find all the cousins of node B.

NOTE:

    Siblings should not be considered as cousins.
    Try to do it in single traversal.
    You can assume that Node B is there in the tree A.
    Order doesn't matter in the output.


we just need to keep track of which level we are at
and which parent
have a list telling the elements on a given level
when we arrive at our target, dont add it to the levels
update a dict telling the index of the desired level


"""
from typing import List, Dict, Optional


# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root: Optional[TreeNode], target: int) -> List[int]:
        levels: List[List[int]] = []
        target_level: Dict[str, int] = {'level': -1}
        self.solve_helper(root, target, levels, None, target_level)
        return [a for a, b in levels[target_level['level']] if b != target_level['parent']]

    def solve_helper(self, root: Optional[TreeNode], target: int, 
                     levels: List[List[int]], parent: int, 
                     target_level: Dict[str, int], level: int = 0) -> None:
        if not root:
            return
        if level == len(levels):
            levels.append([])
        if root.val != target:
            levels[level].append((root.val, parent))
        else:
            target_level['level'] = level
            target_level['parent'] = parent
        self.solve_helper(root.left, target, levels, root, target_level, level + 1)
        self.solve_helper(root.right, target, levels, root, target_level, level + 1)

        


