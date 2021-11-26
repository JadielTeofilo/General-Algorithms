"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.

f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.


brute force approach goes on every number
now goes on the other numbers of list calculating result, 
updates max value

In numbers: List[int]
Out int

"""
from typing import List

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArr(self, numbers: List[int]) -> int:
		added_nums: List[int] = self.find_added(numbers) 
		sub_nums: List[int] = self.find_sub(numbers) 
		return max(added_nums) - min(sub_nums)

	def find_added(self, numbers: List[int]) -> List[int]:
		return [number + i for i, number in enumerate(numbers)]

	def find_sub(self, numbers: List[int]) -> List[int]:
		return [-number - i for i, number in enumerate(numbers)]

		
		
