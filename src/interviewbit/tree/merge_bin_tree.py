"""
Given two Binary Trees A and B, you need to merge them in a single binary tree.

The merge rule is that if two nodes overlap, then sum of node values is the new value of the merged node.

Otherwise, the non-null node will be used as the node of new tree.


iterate on the first keeping track of the equivalent node on the second, 
if first.left is null make it be second.left, same for right
    then return
if change curr to be sum of both

O(max(n,m)) time where n is first nodes and m is num of second nodes.
O(max(logn, logm)) space

"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, first: TreeNode, second: TreeNode) -> TreeNode:
        if second is None or first is None:
            return first or second
        first.val = first.val + second.val
        first.left = self.solve(first.left, second.left) 
        first.right = self.solve(first.right, second.right)
        return first
        
