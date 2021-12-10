"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1


Your algorithm should run in O(n) time and use constant space.

Remove all elements <=0 ou > len
 3  4  N  1
 N  4 -3  1
-1  N -3 -4


replace the number with index = number-1 position and keep looping until finding a None or negative
Think duplicates
keep track of the spot where you stoped, after finding a stop point, start again from stop + 1
iterate on the array and find the first None
if no None found, return last + 1

O(n) time complexity where n is the size of the input array
O(1) space

In - numbers: List[int]
Out - int


"""
from typing import List, Optional


class Solution:
	# @param A : list of integers
	# @return an integer
	def firstMissingPositive(self, numbers: List[Optional[int]]) -> int:
		self.remove_invalid(numbers)
		self.reposition_to_right_index(numbers)
		return self.find_first_missing(numbers)

	def remove_invalid(self, numbers: List[Optional[int]]) -> None:
		for index, number in enumerate(numbers):
			if number < 1 or number > len(numbers):
				numbers[index] = None

	def reposition_to_right_index(self, numbers: List[Optional[int]]) -> None:
		for curr_index in range(len(numbers)):
			curr: Optional[int] = numbers[curr_index]
			numbers[curr_index] = None
			while curr is not None and curr > 0:
				aux: Optional[int] = numbers[curr - 1]
				numbers[curr - 1] = -1*curr
				curr = aux
	
	def find_first_missing(self, numbers: List[Optional[int]]) -> int:
		for index, value in enumerate(numbers):
			if value is None:
				return index + 1
		return len(numbers) + 1  # Case that the smallest is outside

				

