"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

    'L' means to go from a node to its left child node.
    'R' means to go from a node to its right child node.
    'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.

 
                                70     
               1                                     23            
        4               6
    2      7       10         12

start 2 
1 4 2
end 10
1 6 10

brute force
we want to find the min common ancestor
from start you go up until you find the common ancestor
from common ancestor you go down looking for the end

Keep info for each node about wheather it can find the end spot from there ('L' or 'R' or 'C')
    check left can reach it
    check right can reach it

    return True or False if can reach it
    update the reach dict

Find the stack from root to start, pop until a node that can reach end node and build result


O(n) time and space where n is the num of nodes


"""
import enum
from typing import Optional, Dict, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ReachType(enum.Enum):
    left = 1
    right = 2
    current = 3
    impossible = 4

class Solution:
    def getDirections(self, root: Optional[TreeNode], 
                      start_value: int, dest_value: int) -> str:
        reach: Dict[int, ReachType] = {}
        self.update_reach(root, dest_value, reach)
        start_stack: List[TreeNode] = []
        self.find_start_stack(root, start_value, start_stack)
        result: List[str] = []
        common_ancestor: Optional[TreeNode] = None
        while start_stack:
            curr: TreeNode = start_stack.pop()
            if reach.get(curr.val) not in [ReachType.left, 
                            ReachType.right, 
                            ReachType.current]:
                result.append('U')
                continue
            common_ancestor = curr
            break
        if common_ancestor is None:
            raise ValueError('Missing Values')
        result.extend(self.find_path_to(common_ancestor, dest_value, reach))
        return ''.join(result)
    
    def update_reach(self, root: Optional[TreeNode], 
                     target: int, 
                     reach: Dict[int, ReachType]) -> bool:
        if root is None:
            return False
        if root.val == target:
            reach[root.val] = ReachType.current
            return True
        if self.update_reach(root.left, target, reach):
            reach[root.val] = ReachType.left
            return True
        if self.update_reach(root.right, target, reach):
            reach[root.val] = ReachType.right
            return True
        reach[root.val] = ReachType.impossible
        
    def find_start_stack(self, root: Optional[TreeNode], 
                         start: int, start_stack: List[TreeNode]) -> None:
        if root is None:
            return
        start_stack.append(root)
        if root.val == start:
            return True
        if self.find_start_stack(root.left, start, start_stack) or self.find_start_stack(root.right, start, start_stack):
            return True
        start_stack.pop()
        
    def find_path_to(self, root: TreeNode, target: int, 
                     reach: Dict[int, ReachType]) -> List[str]:
        path: List[str] = []
        while root.val != target:
            if reach[root.val] == ReachType.left:
                path.append('L')
                root = root.left
                continue
            if reach[root.val] == ReachType.right:
                path.append('R')
                root = root.right
        return path
            
