"""
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.


Input Format

First and only argument is an integer array A.


Output Format

Return 1 if any such integer p is found else return -1.

3 2 1 3

1 2 3 3
0 1 2 3
len = 4


sort the array
iterate checking number == (len(numbers) - 1 - index)
return true in that case
return false


O(1) space (best case python sort)
O(nlogn) time complexity


In - numbers: List[int]
Out - bool


Can we change the input array?
yup 

"""
from typing import List


class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, numbers: List[int]) -> int:
		numbers.sort()
		for index, number in enumerate(numbers):
			if ((index + 1) < len(numbers) 
				and number == numbers[index + 1]):
				continue
			if number == (len(numbers) - 1 - index):
				return 1
		return -1


