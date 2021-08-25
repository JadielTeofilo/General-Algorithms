"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.


In - tree_root: Node, origin: int, target: int

Out - value: int 

Assume we dont have repeated values

								3	

			7									2
	1									5				9
								4
										6

3 2 5 4 6
3 2 9

6 4 5 2 3
9 2 3


O(V) time complexity
O(log N) space complexity on a balanced bin tree

"""
from typing import Optional, List, Set
import dataclasses


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def common_ancesstor(root: Node, origin: int, target: int) -> int:
	""" Finds the common ancessestor on the tree """
	if not root or not origin or not target:
		raise ValueError('Empty inputs')
	path_to_origin: List[int] = get_path_to_node(root, origin)
	path_to_target: List[int] = get_path_to_node(root, target)
	path_to_origin.reverse()
	path_to_target.reverse()
	return first_common_element(path_to_origin, path_to_target)


def get_path_to_node(root: Node, node_value: int) -> List[int]:
	""" Does an iteractive DFS and returns 
		the stack when value is found """
	stack: List[Node] = []
	stack.append(root)
	visited: Set[int] = set()
	# Does Iteractive DFS and stops when finds value
	while stack:
		node: Node = stack[-1]
		if node.left and node.left.value not in visited:
			stack.append(node.left)
		elif node.right and node.right.value not in visited:
			stack.append(node.right)
		elif node.value != node_value:
			visited.add(node.value)
			stack.pop()
		else:
			break	
	if not stack:
		raise ValueError('Node value not on stack')
	result: List[int] = [node.value for node in stack]
	return result


def first_common_element(left: List[int], right: List[int]) -> int:
	left_cache: Set[int] = set(left)
	for item in right:
		if item in left_cache:
			return item
	raise ValueError('Lists have no intersection')

root = Node(3, Node(7, Node(1)), Node(2, Node(5, Node(4, None, Node(6))), Node(9)))
print(common_ancesstor(root, 6, 9))
import pdb;pdb.set_trace()
