"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).



In - value: int, root: TreeNode

Out - amount of paths



						   6
			1							2
	9				4			-1				3
2		3					-2		6

value = 5

1 - 4
6 - 2 - -1 - -2
2 - 3
-1 - 6

Brute force
For each node try all possibilities


O(N^2) time complexity
O(N) space complexity

"""
from typing import Optional, Dict, List
import dataclasses


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def paths_with_sum(root: Node, value: int) -> int:
	""" 	
		Finds the amount of paths on the tree that 
		sum up to value
	"""
	if not root or not value:
		raise ValueError('Empty inputs')
	result: Dict[str, int] = {'sum': 0}
	paths_with_sum_helper(root, value, result)
	return result['sum']


def paths_with_sum_helper(node: Node, target: int, 
						  result: Dict[str, int]) -> List[int]:
	"""
		Recurses on the tree finding the possible sums 
		of left and right and adding the result when finding 
		sum that equals value 
		
		Args: 
			node: Node to recurse from
			target: sum target
			result: dict to update sum 
		Returns:
			list of possible sums from node downards

	"""
	if not node:
		return []
	left_sums: List[int] = paths_with_sum_helper(node.left, target, result)
	right_sums: List[int] = paths_with_sum_helper(node.right, target, result)
	
	sum_to_every_element(left_sums, node.value)
	sum_to_every_element(right_sums, node.value)

	possible_sums: List[int] = left_sums + right_sums + [node.value]
		
	result['sum'] += possible_sums.count(target)
	
	return possible_sums



def sum_to_every_element(elements: List[int], value: int) -> None:
	for i in range(len(elements)):
		elements[i] += value

asdf = Node(6, Node(1, Node(9, Node(2), Node(3)), Node(4)), Node(2, Node(-1, Node(-2), Node(6)), Node(3)))
print(paths_with_sum(asdf, 5))
import pdb;pdb.set_trace()



