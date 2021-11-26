"""
Given an array A containing N integers.

You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.


In - numbers: List[int]
Out - int

have a suffix list with the max element to that point
iterate on numbers, considering the curr number as the mid element of the triplet
iterate on the elements on the left to find the left element


O(n^2) where n is the size of the list


"""
import math
from typing import List, Union, Optional


class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, numbers: List[int]) -> int:
		max_suffix: List[int] = self.build_suffixes(numbers)
		max_triplet: Union[float, int] = -math.inf
		for index, number in enumerate(numbers):
			if max_suffix[index] <= number:
				continue
			target_left: Optional[int] = self.find_left_target(
				numbers, index
			)
			if target_left is None:
				continue
			curr_sum: int = (
				target_left	+ number + max_suffix[index]
			)
			max_triplet = max(max_triplet, curr_sum)
		if max_triplet == -math.inf:
			return 0
		return int(max_triplet)

	def find_left_target(self, numbers: List[int], index: int) -> Optional[int]:
		curr_number: int = numbers[index]
		max_number: Union[float, int] = -math.inf
		for i in range(index):
			if numbers[i] >= curr_number:
				continue
			max_number = max(max_number, numbers[i])
		if max_number == -math.inf:
			return None
		return int(max_number)
		
	def build_suffixes(self, numbers: List[int]) -> List[int]:
		last_max: Union[int, float] = -math.inf
		suffixes: List[int] = [0] * len(numbers)
		for i in range(len(numbers) - 1, -1, -1):
			suffixes[i] = int(max(last_max, numbers[i]))
			last_max = suffixes[i]
		return suffixes
