"""
 BiNode: Consider a simple data structure called BiNode, which has pointers to two other nodes. The
data structure BiNode could be used to represent both a binary tree (where nodel is the left node
and node2 is the right node) or a doubly linked list (where nodel is the previous node and node2
is the next node). Implement a method to convert a binary search tree (implemented with BiNode)
into a doubly linked list. The values should be kept in order and the operation should be performed
in place (that is, on the original data structure)


						5
			3						8
	
	2_						7				9


2 <->  3 


build_list(node: BiNode) -> BiNode

left: BiNode = build_list(node.left)

last(left).right, node.left = node, last(left)

right: BiNode = build_list(node.right)
first(right).left, node.right = node, first(right)


O(n) time complexity where n is the amount of nodes on the three


"""
import collections
import dataclasses
from typing import Optional


@dataclasses.dataclass
class BiNode:
	value: int
	left: Optional['BiNode'] = None
	right: Optional['BiNode'] = None


def convert_to_list(root: BiNode) -> Optional[BiNode]:
	return first(build_list(root))


def build_list(node: BiNode) -> Optional[BiNode]:
	if not node:
		return 
	left_list: Optional[BiNode] = build_list(node.left)
	last_of_left: Optional[BiNode] = last(left_list) if left_list else None
	if last_of_left:
		last_of_left.right = node
	node.left = last_of_left
	
	right_list: BiNode = build_list(node.right)
	first_of_right: Optional[BiNode] = (first(right_list) 
										if right_list else None)
	if first_of_right:
		first_of_right.left = node
	node.right = first_of_right
	return node


def first(node: BiNode) -> BiNode:
	if not node:
		raise ValueError('Empty input')
	if node.left:
		return first(node.left)
	return node


def last(node: BiNode) -> BiNode:
	if not node:
		raise ValueError('Empty input')
	if node.right:
		return last(node.right)
	return node


print(convert_to_list(BiNode(5, BiNode(3, BiNode(1)), BiNode(8, BiNode(7), BiNode(9)))))

