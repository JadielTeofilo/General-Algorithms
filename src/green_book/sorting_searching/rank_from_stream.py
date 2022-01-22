"""
Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish
to be able to look up the rank of a number x (the number of values less than or equal to x).
Implement the data structures and algorithms to support these operations. That is, implement
the method track(int x), which is called when each number is generated, and the method
getRankOfNumber(int x), which returns the number of values less than or equal to x (not
including x itself).

Are there duplicates
Yes

Binary search tree
inserts on O(log(n)) where n is the amount of elements on the tree given mildly balancesd inputs
retrieves on O(log(n)) given mildly balanced inputs


track()
In - int 
Out - None
get_rank_of_number()
In - int
out - int

"""
from typing import Optional
import dataclasses


@dataclasses.dataclass
class Node:
	value: int
	left_amount: int = 0
	left: Optional['Node'] = None
	right: Optional['Node'] = None


class StreamRank:

	def __init__(self) -> None:
		self.search_tree: Optional[Node] = None

	def track(self, value: int) -> None:
		"""
			Adds value to the rank tracking tree
		"""
		self.search_tree = self._insert_on_tree(
			self.search_tree, value
		)
	
	def _insert_on_tree(self, node: Node, value: int) -> Node:
		if not node:
			return Node(value)
		if value > node.value:
			node.right = self._insert_on_tree(
				node.right, value
			)
		else:
			node.left = self._insert_on_tree(
				node.left, value
			)
			node.left_amount += 1
		return node

	def get_rank_of_number(self, value: int) -> Optional[int]:
		"""
			Finds value on the ranking three and returns the rank
		"""
		return self._find_rank(
			self.search_tree, value, 0
		)

	def _find_rank(self, node: Node, value: int, 
				   curr_rank: int) -> Optional[int]:
		""" Finds the amount of elements smaller 
			or equal to value 
		"""
		if not node:
			return
		if node.value == value:
			return node.left_amount + curr_rank
		if value > node.value:
			return self._find_rank(
				node.right, value, 
				curr_rank + node.left_amount + 1
			)
		return self._find_rank(
			node.left, value,
			curr_rank
		)


stream = StreamRank()
stream.track(8)
stream.track(11)
stream.track(2)
stream.track(9)
stream.track(9)
stream.track(2)
stream.track(21)
stream.track(4)
stream.track(5)
stream.track(7)
import pdb;pdb.set_trace()
