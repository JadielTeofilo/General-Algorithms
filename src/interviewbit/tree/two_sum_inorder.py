"""
Given a binary search tree A, where each node contains a positive integer, and an integer B, you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise.



The key here is to use the sorted property to avoid have O(n) space usage like the regular two sum


to do that we keep a pointer on the biggest element and one on the smallerst
if the sum of min + max is bigger then the target, we decrease the max
if smaller, we increase the min


O(n) time complexity where n is the num of nodes
O(log n) where n is the num of nodes

"""
from typing import List, Optional, Iterable


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root: TreeNode, target: int) -> int:
        big_traversal: Iterable[int] = self.inorder(root, True)  
        big: Optional[int] = next(big_traversal, None)
        for small in self.inorder(root):  
            if big is None or big == small:
                return 0
            while (big is not None and (big + small) > target):
                big = next(big_traversal, None)
            if big is not None and big + small == target:
                return 1
        return 0

    def inorder(self, root: Optional[TreeNode], 
                is_reversed: bool = False) -> Iterable[int]:
        if not root:
            return
        if is_reversed:
            first: Optional[TreeNode] = root.right
            sec: Optional[TreeNode] = root.left
        else:
            first: Optional[TreeNode] = root.left
            sec: Optional[TreeNode] = root.right
        
        yield from self.inorder(first, is_reversed)
        yield root.val
        yield from self.inorder(sec, is_reversed)
