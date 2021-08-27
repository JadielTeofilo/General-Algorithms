"""
Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for get Random Node, and explain how you would implement the rest of the methods.

Keep track of how many nodes we have below each node

traverse the tree in the following manner 
	cound elements on the left + right + 1, do a rand on that value and 
then randomizes a number on that range and iterates O(N) till it and returns it
memory O(log N)

random.seed(time.time())
random.randint(0, size)

OR

keep all values on a list as well so we know the value and can access it on O(log(N))
memory O(N)

Question
Do we have repeated values in out bst


"""
from typing import Optional
import dataclasses
import random
import time


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None
	size: int = 1


class Tree:

	def __init__(self) -> None:
		self.root: Node = None

	def get_random_node(self) -> Node:
		if not self.root:
			raise ValueError('Empty Tree')
		return self.random_node_helper(self.root)

	def random_node_helper(self, node: Node, 
						   random_value: Optional[int] = None) -> Node:
		""" Does the recursion between the tree nodes to 
			find the randomized node
			
			Args:
				node: is the starting point of recursion
				random_value: is the randomized value used to find the node
			Returns:
				A randomized Node.
		"""
		if not random_value:
			random.seed(time.time())
			random_value: int = random.randint(0, node.size - 1)
		left_size: int = node.left.size if node.left else 0
		right_size: int = node.right.size if node.right else 0 
		# Based on the random value, decides where to go
		if random_value < left_size:
			return self.random_node_helper(node.left, random_value)
		elif random_value == left_size:
			return node
		else:
			return self.random_node_helper(
				node.right, 
				random_value - left_size - 1  # Offsets to the right size
			)


asdf = Node(5, Node(3, Node(2), Node(4), 3), Node(8, Node(7), Node(6), 3), 7)
tree = Tree()
tree.root = asdf
tree.get_random_node()
import pdb;pdb.set_trace()
