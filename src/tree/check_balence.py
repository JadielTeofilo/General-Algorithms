"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.


in - tree root

out - bool


			1
	2				3
5		6		7		8

time complexity = O(n)
space = O (H)


"""
import dataclasses
from typing import Optional, Union


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def is_balanced(tree_root: Node) -> bool:
	return is_balanced_helper(tree_root) is not False


def is_balanced_helper(node: Node) -> Union[int, bool]:
	""" Returns the max height of a node or false if it is not balanced """
	if not node:
		return 0
	left_test: Union[int, bool] = is_balanced_helper(node.left)
	right_test: Union[int, bool] = is_balanced_helper(node.right)
	# Returns False if nodes below are unbalanced
	if left_test is False or right_test is False:
		return False
	if (left_test > right_test + 1 or 
		right_test > left_test + 1):
		return False
	return max(left_test, right_test) + 1


import pdb;pdb.set_trace()
