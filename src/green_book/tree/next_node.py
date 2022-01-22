"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

in: target_node: Node
out: sucessor_node: Node



			5
	2				7
1		3		7		9


In order traversal gives us a sorted list of values, but loses track of duplicates
Are there duplicates in this?


O(N) time where n is the number of nodes
O(log N) Space

"""
from typing import Optional, Union
import dataclasses
import math


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None
	parent: Optional['Node'] = None


def in_order_sucessor(target: Node) -> Node:
	""" Finds the next sucessor """
	if not target:
		raise ValueError('Empty input')
	if target.right:
		return leftmost_node(target.right)
	target_value: int = target.value
	while target.parent:
		target = target.parent
		if target.value > target_value:
			return target	
	raise ValueError('There is no sucessor')


def leftmost_node(node: Node) -> Node:
	""" Recurses on the tree from node finding leftmost node """
	if not node.left:
		return node
	return leftmost_node(node.left)


import pdb;pdb.set_trace()
