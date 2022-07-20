"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


for a given node we want to know what is the max sum the left and right sides can offer me
then we update result with curr is curr > 0 else 0 + left_offer if left offer > 0 else 0 and right offer
then we return max(left offer, right offer) + curr


O(n) time complexity where n is the number of nodes
O(logn) space complexity for the recursion

"""
import sys
from typing import List, Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result: Dict[str, int] = {'max': -sys.maxsize}
        find_max_sum(root, result)
        return result['max']

def find_max_sum(node: Optional[TreeNode], 
                 result: Dict[str, int]) -> int:
    if not node:
        return 0
    left_offer: int = find_max_sum(node.left, result)
    right_offer: int = find_max_sum(node.right, result)
    result['max'] = max(
        result['max'], 
        node.val + 
        positive_or_zero(left_offer) + 
        positive_or_zero(right_offer)
    )
    return max(
        positive_or_zero(left_offer), 
        positive_or_zero(right_offer)
    ) + node.val


def positive_or_zero(num: int) -> int:
    return num if num > 0 else 0
    

