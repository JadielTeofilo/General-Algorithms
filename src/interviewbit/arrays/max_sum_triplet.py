"""
Problem Description

Given an array A containing N integers.
You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.



Problem Constraints
3 <= N <= 105.
1 <= A[i] <= 108.


Input Format
First argument is an integer array A.
numbers: List[int]

Output Format
Return a single integer denoting the maximum sum of triplet as described in the question.
int


1 -2 9 2 5 -2 1 29 1 -2

							_

		1				-2				9			2				5			-2			1
	9	2	5


The brute force is try all possibilities starting at a given spot

with memoization the time complexity would be O(n^2)

solve(numbers, tiplet_index)

what happens when there is no triplet


"""
import collections
import math
from typing import List, Optional, Union, Dict


Position = collections.namedtuple('Position', 'val level')
Cache = Dict[Position, Optional[int]]


class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, numbers: List[int]) -> Optional[int]:
		cache: Cache = {}
		return self._solve(numbers, cache)

	def _solve(self, numbers: List[int], cache: Cache,
			   start: int = 0, min_: Union[int, float] = math.inf, 
			   level: int = 1) -> Optional[int]:
		if start >= len(numbers) or level > 3: 
			return 0
		if (min_, level) in cache:
			return cache[(min_, level)]
		max_sum: Union[int, float] = -math.inf
		for i in range(start, len(numbers)):
			if numbers[i] <= min_:
				continue
			curr_sum: Optional[int] = self._solve(
				numbers, cache, start=i + 1, 
				min_=numbers[i], level=level + 1
			)
			if curr_sum is None:
				continue
			max_sum = max(max_sum, numbers[i] + curr_sum)
		cache[Position(min_, level)] = (int(max_sum)
									    if max_sum != -math.inf else None)
		return cache[(min_, level)]
			
