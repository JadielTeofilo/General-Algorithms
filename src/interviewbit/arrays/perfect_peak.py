"""
Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.

In - numbers: List[int]
Out - int (1 or 0)


1 2 8 0 1 9 0 10

build prefix array with max num
build suffix array with min num
Iterate from 1:-1 and look for the target val

O(n) space and time where n is the size of the inputed list


"""
from typing import List


class Solution:
	# @param A : list of integers
	# @return an integer
	def perfectPeak(self, numbers: List[int]) -> int:	
		if not numbers:
			return 0
		suffix: List[int] = self.build_suffix(numbers)
		prefix: List[int] = self.build_prefix(numbers)
		for index, number in enumerate(numbers):
			if index == 0 or index == len(numbers) - 1:
				continue
			if (number > prefix[index - 1] or 
				number < suffix[index + 1]):
				return 1
		return 0

	def build_suffix(self, numbers: List[int]) -> List[int]:
		suffix: List[int] = [0] * len(numbers)
		suffix[-1] = numbers[-1]
		for index in range(len(numbers)-2, -1, -1):
			suffix[index] = min(numbers[index], suffix[index + 1])
		return suffix

	def build_prefix(self, numbers: List[int]) -> List[int]:
		prefix: List[int] = []
		prefix.append(numbers[0])
		for index in range(1, len(numbers)):
			prefix.append(max(prefix[index - 1], numbers[index]))
		return prefix
		
