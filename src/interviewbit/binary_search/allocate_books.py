"""
Given an array of integers A of size N and an integer B.

College library has N bags,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.


In - nums: List[int], bags: int
Out - min_sum: int

3
2 3 5 1 2 8 8

It is basically about finding partitions that minimize the max on any given bag 

one way to do it is to generate all possible partitions
				
						2 3 5 1 2 8 8 (2)
	2|3 5 1 2 8 8, (1)

basically building all possible contíguous blocks 

solve(nums: List[int], runnig_sum: List[int], partitions: int, start: int)

memoize the start and get a O(n^2) time complexity

Other option is:

start with the max bag sum of sum(nums) and try building the bags

2
3 2 2 8 3  sum = 18

start = 1, end = max_bag
pivot = (start + end) // 2
iterate on nums until the sum gets to pivot
	decrease one from partition, reset the sum and continue 
at the end, if partition > 0 
	start = pivot + 1
else:
	end = pivot - 1



"""
import sys
from typing import List


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, nums: List[int], bags: int) -> int:
		# [1] 1
		max_bag: int = sum(nums)  # 1 
		start: int = 1
		end: int = max_bag  # 1
		result: int = sys.maxsize
		if bags > len(nums):
			return -1
		while start <= end:
			pivot: int = (start + end) // 2  # 1
			partitions: int = self.find_partitions(nums, pivot)
			if partitions <= bags:
				end = pivot - 1
				result = min(result, pivot)
			else:
				start = pivot + 1
		return result 

	def find_partitions(self, nums: List[int], size: int) -> int:
		# 3,2,2,4,1,4
		# 5
		curr_partitions: int = 0
		curr_sum: int = 0
		for i, num in enumerate(nums):
			curr_sum += num  # 4
			# Stops already if a single element wont fit with curr size
			if num > size:
				return sys.maxsize
			if (curr_sum == size or 
				(i + 1 < len(nums) and curr_sum + nums[i+1] > size)): 
				curr_sum = 0
				curr_partitions += 1  # 5
			elif i == len(nums) - 1:  # Adds one at the last index
				curr_partitions += 1  # 
		return curr_partitions


