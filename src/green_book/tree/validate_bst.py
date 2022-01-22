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
from typing import Union, Optional
import enum


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


class Side(enum.Enum):
	left = 1
	right = 2


def is_binary_search_tree(tree_root: Node) -> bool:
	return is_bst_helper(tree_root) is not False


def is_bst_helper(node: Node, side: Optional[Side] = None) -> Union[int, bool]:
	if not node:
		return True
	
	right_test: Union[int, bool] = is_bst_helper(node.right, Side.right)
	left_test: Union[int, bool] = is_bst_helper(node.left, Side.left)
	
	# Returns false if any of the nodes bellow are false
	if right_test is False or left_test is False:
		return False

	# Returns false if left or right have problems
	if ((right_test is not True and right_test <= node.value) or
		(left_test is not True and left_test > node.value)):
		return False

	right_test = node.value if right_test is True else right_test
	left_test = node.value if left_test is True else left_test
	if side == Side.left:
		return max(node.value, right_test)
	if side == Side.right:
		return min(node.value, left_test)
	return node.value


import pdb;pdb.set_trace()
	
