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


the other easier way is to keep track of all parent relations, and handle the problem as a graph, bfs keeping visited and all

build parents
start from burning node
check visited
add one to result if curr node adds a non visited to queue
add parent, left, right to queue using bfs


"""
import collections
from typing import List, Dict, Optional, Set

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, root: TreeNode, value: int) -> int:
        parents: Dict[int, Optional[TreeNode]] = {}
        self.build_parents(root, parents)
        node: Optional[TreeNode] = self.find_node(root, value)
        visited: Set[int] = set()
        queue = collections.deque()
        # Its a bfs where we keep track of the layer number we`re at
        queue.append((node, 0))
        time: int = 0
        while queue:
            curr, layer = queue.popleft()
            if not curr:
                continue
            has_new_neighbor: bool = False
            time = max(layer, time)
            for neighbor in [curr.left, curr.right, parents[curr.val]]:
                if neighbor is not None and neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor, layer + 1))
        return time

    def build_parents(self, node: Optional[TreeNode], 
                      parents: Dict[int, Optional[TreeNode]], 
                      parent: Optional[TreeNode] = None) -> None:
        if not node:
            return
        self.build_parents(node.left, parents, node)
        parents[node.val] = parent
        self.build_parents(node.right, parents, node)
    
    def find_node(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if not node:
            return
        if node.val == value:
            return node
        found_left: TreeNode = self.find_node(node.left, value)
        if found_left is not None:
            return found_left
        return self.find_node(node.right, value)


