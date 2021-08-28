"""
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl .
A tree T2 is a subtree of T1 if there exists a node n in Tl such that the subtree of n is identical to T2 .
That is, if you cut off the tree at node n, the two trees would be identical.

In - first_root: Node, second_root: Node
Out - bool


			  2
	2					2
3		5			1		7


	2
3		5

Are there duplicate values on the tree?
Yes

O(n + m*k) time complexity - where k is the amount of elements on first 
tree that are equal to the root of the second

"""
from typing import Optional, Iterator
import dataclasses


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def is_subtree(root: Node, subtree_root: Node) -> bool:
	if not root or not subtree_root:
		raise ValueError('Empty inputs')
	for node in traverse_tree(root):
		if trees_are_equal(node, subtree_root):
			return True
	return False


def traverse_tree(node: Node) -> Iterator[Node]:
	if not node:
		return
	yield from traverse_tree(node.left)
	yield node
	yield from traverse_tree(node.right)


def trees_are_equal(first: Node, second: Node) -> bool:
	if not first or not second:
		return first == second
	if first.value != second.value:
		return False
	return (trees_are_equal(first.left, second.left) and 
			trees_are_equal(first.right, second.right))

root = Node(2, Node(2, Node(2, Node(3, Node(1)), Node(5))), Node(2, Node(1, Node(7))))
sub_tree = Node(2, Node(3), Node(5))

import pdb;pdb.set_trace()
