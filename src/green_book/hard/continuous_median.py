"""
Continuous Median: Numbers are randomly generated and passed to a method. Write a program
to find and maintain the median value as new values are generated.


median is the 50th percentil

3 7 2 9 2 1

sort and get the element in the middle

either keep a sorted list and insert sorted (O(n))

Another approach is to use two heaps, a min and max heap, insertions are roughtly log(n) 


max [2] min [7]

decide where to insert (the one with the smallest amount)
check if it would violate the two heaps
inserts
rebalances if needed
	


to get the median just take one from the largest heap or pick from one of them

In number: int
Out None

"""
import collections
import heapq
from typing import List


Value = collections.namedtuple('Value', 'indexing val')


class MedianHandler:

	def __init__(self) -> None:
		self.min_heap: List[Value] = []
		self.max_heap: List[Value] = []

	def insert(self, number: int) -> None:
		target_heap: str = self.find_heap_to_insert(number)
		indexing: int = (-number if target_heap == 'max_heap'
						 else number)
		heapq.heappush(getattr(self, target_heap), 
					   Value(indexing, number))
		if self.needs_rebalancing():
			self.rebalance()

	def find_heap_to_insert(self, number: int) -> str:
		"""
 			Finds which heap should be inserted in
			The first condition is the size, choosing the smaller.
			The second condition is if it keeps the property 
			all_elements(max_heap) < all_elements(min_heap)
		"""
		if len(self.min_heap) < len(self.max_heap):
			top_from_max: Value = self.max_heap[0]
			if number <= top_from_max.val: 
				return 'max_heap'
			return 'min_heap'
		else:
			if not self.min_heap:
				return 'max_heap'
			bot_from_min: Value = self.min_heap[0]
			if number >= bot_from_min.val:
				return 'min_heap'
			return 'max_heap'

	def needs_rebalancing(self) -> bool:
		return abs(len(self.min_heap) - len(self.max_heap)) > 1

	def rebalance(self) -> None:
		if len(self.min_heap) < len(self.max_heap):
			target: List[Value] = self.min_heap
			origin: List[Value] = self.max_heap
		else:
			target: List[Value] = self.max_heap
			origin: List[Value] = self.min_heap
		value: Value = heapq.heappop(origin)
		# Flips the indexing to cope with the max_heap inversion
		new_value: Value = Value(value.indexing*-1, value.val)
		heapq.heappush(target, new_value)			

	def get_median(self) -> int:
		target_heap: List[Value] = self.find_heap_with_median()
		return target_heap[0].val

	def find_heap_with_median(self) -> List[Value]:
		if len(self.min_heap) > len(self.max_heap):
			return self.min_heap
		elif len(self.max_heap) > len(self.min_heap):
			return self.max_heap
		if self.max_heap or self.min_heap:
			return self.max_heap or self.min_heap
		raise ValueError('Empty median')
			

asdf = MedianHandler()
import pdb;pdb.set_trace()
