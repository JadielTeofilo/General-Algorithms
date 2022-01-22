"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""
import dataclasses
from typing import Optional, List


@dataclasses.dataclass
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


class Bstree:
    
    def __init__(self) -> None:
        self.root: Optional[Node] = None
        
    def insert(self, value: int) -> None:
        self.root = self.insert_helper(value, self.root)
        
    def insert_helper(self, value: int, node: Node) -> Node:
        """ Finds spot to insert and inserts new value recursively """
        if not node:
            return Node(value)
        if value > node.value:
            node.right = self.insert_helper(value, node.right)
        else:
            node.left = self.insert_helper(value, node.left)
        return node
    
    def __str__(self) -> str:
        return str(self.root)
    

def build_bstree_from_sorted_list(nums: List[int]) -> Bstree:
    if not nums:
        raise ValueError('Empty input')
    tree: Bstree = Bstree()
    # build_helper(tree, nums, start=0, end=len(nums) - 1)
    tree.root = build_helper_single_pass(nums, start=0, end=len(nums) - 1)
    return tree


def build_helper(tree: Bstree, nums: List[int], start: int, end: int) -> None:
    """ Builds recursively a BST divide and conquer style """
    if start > end:
        return
    mid: int = (start + end) // 2
    tree.insert(nums[mid])  # Inserts the mid point on tree
    # Calls it self to build the rest
    build_helper(tree, nums, start=start, end=mid-1)
    build_helper(tree, nums, start=mid+1, end=end)
    

def build_helper_single_pass(nums: List[int], start: int, end: int) -> Optional[Node]:
    """ Builds recursively a BST divide and conquer style """
    if start > end:
        return None
    mid: int = (start + end) // 2
    node: Node = Node(nums[mid])
    # Calls it self to build the rest
    node.left = build_helper_single_pass(nums, start=start, end=mid-1)
    node.right = build_helper_single_pass(nums, start=mid+1, end=end)
    return node


import pdb;pdb.set_trace()
