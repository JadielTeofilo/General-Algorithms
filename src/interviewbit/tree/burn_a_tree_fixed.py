"""
Given a binary tree denoted by root node A and a leaf node B from this tree.

 It is known that all nodes connected to a given node (left child, right child and parent) get burned in 1 second. Then all the nodes which are connected through one intermediate get burned in 2 seconds, and so on.

You need to find the minimum time required to burn the complete binary tree.


 Tree :      1 
            / \ 
           2   3 
          /   / \
         4   5   6

1
6

2

5

The catch is that its easy to know how long it would take from the root, its just the depth of the tree, 
we iterate on the tree adding meta data to a hash: depth data, if the burn is coming from bellow curr node, time the fire took to get here

depth = max(left.depth, right.depth)
fire_origin = left.fire or right.fire
time = from burning node to here 
result = min(time + opposite side depth, result)

O(n) time where n is nodes
O(n) space

the other easier way is to keep track of all parent relations, and handle the problem as a graph, bfs keeping visited and all

build parents
start from burning node
check visited
add one to result if curr node adds a non visited to queue
add parent, left, right to queue using bfs

O(n) time
O(n) space

"""
import collections
from typing import List, Dict, Optional, Set


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val: int = x
        self.left: Optional['TreeNode']= None
        self.right: Optionl['TreeNode'] = None


class MetaData:
    def __init__(self):
        self.fire_origin: bool = False
        self.time: int = 0  # Time taken to burn a tree with curr element as root
        self.depth: int = 0


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, root: TreeNode, value: int) -> int:
        cache: Dict[int, MetaData] = collections.defaultdict(MetaData)
        self.update_tree(root, value, cache)
        return cache[root.val].time

    def update_tree(self, node: Optional[TreeNode], target: int, 
                    cache: Dict[int, MetaData]) -> None:
        if not node:
            return 
        self.update_tree(node.left, target, cache)
        self.update_tree(node.right, target, cache)
        left_depth: int = cache[node.left.val].depth if node.left else 0
        right_depth: int = cache[node.right.val].depth if node.right else 0
        cache[node.val].depth = 1 + max(left_depth, right_depth)
        cache[node.val].fire_origin = ((cache[node.left.val].fire_origin if node.left else False) or 
                            (cache[node.right.val].fire_origin if node.right else False))
        if node.left and cache[node.left.val].fire_origin:
            cache[node.val].time = (cache[node.left.val].time + 1 + 
                        (cache[node.right.val].depth if node.right else 0))
        elif node.right and cache[node.right.val].fire_origin:
            cache[node.val].time = (cache[node.right.val].time + 1 +
                         (cache[node.left.val].depth if node.left else 0))
        if node.val == target:
            cache[node.val].fire_origin = True

    
