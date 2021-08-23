"""
Validate 8ST: Implement a function to check if a binary tree is a binary search tree.


in - treeroot: Node
out - bool


Does this binary tree supports duplicates?
yes and left <= current < right

			5
	2				7
1		3		6		8

O(N) time complexity
O(H) space complexity

"""
import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def is_bst(tree_root: Node) -> bool:
	return is_bst_helper(tree_root, min_=None, max_=None)


def is_bst_helper(node: Node, min_: Optional[int], max_: Optional[int]) -> bool:
	if not node:
		return True
	if ((max_ is not None and node.value > max_) 
		or not is_bst_helper(node.left, min_, node.value)):
		return False
	
	if ((min_ is not None and node.value <= min_)
		or not is_bst_helper(node.right, node.value, max_)):
		return False

	return True


import pdb;pdb.set_trace()
