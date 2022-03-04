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
3


5

The catch is that its easy to know how long it would take from the root, its just the depth of the tree, 
we iterate on the tree adding: depth data, if the burn is coming from bellow curr node, time the fire took to get here

O(n) time where n is nodes
O(1) space

the other easier way is to keep track of all parent relations, and handle the problem as a graph, bfs keeping visited and all

build parents
start from burning node
check visited
add one to result if curr node adds a non visited to queue
add parent, left, right to queue using bfs


"""
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
        parents: Dict[int, TreeNode] = self.build_parents(root)  # TODO
        node: TreeNode = self.find_node(root, value)  # TODO
        visited: Set[int] = set()
        queue = collections.deque()
        queue.append(node)
        time: int = 0
        while queue:

