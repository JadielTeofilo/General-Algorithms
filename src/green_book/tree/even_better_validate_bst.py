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
O(1) space complexity

But considers that there is no duplicate on the graph

"""
import dataclasses
from typing import Optional, Iterator, Union
import math


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def is_bst(tree_root: Node) -> bool:
	""" Checks if the in order traversal yields a ordered list """
	last: Union[float, int] = -math.inf
	for value in in_order_traversal(tree_root):
		print(value)
		if value < last:
			return False
		last = value
	return True


def in_order_traversal(node: Node) -> Iterator[int]:
	if not node:
		return
	yield from in_order_traversal(node.left)
	yield node.value
	yield from in_order_traversal(node.right)


import pdb;pdb.set_trace()
