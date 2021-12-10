"""
Problem Description

Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.

A = [5, 5, 2, 5, 8]
even preffix
 0  5  5 10 10
odd suffix
15 10 10  8  8 
full_sum
25


remove 1
sum = 12


If full sum even after removal, continue

iterate on numbers
check what would happen if removed current
	take the even prefix (remove curr if even)
	take the odd suffix (remove curr if odd)
	sum both, it equals half the full sum, add one to answer


2 6 4

In - numbers: List[int]
Out - int


O(n) time complexity  where n is the size of the imput list
O(n) space complexity 


"""
from typing import List


class Solution:
	
	def solve(self, numbers: List[int]) -> int:
		if not numbers: 
			return 0
		even_prefix_sum: List[int] = self.get_even_prefix(
			numbers
		)
		odd_suffix_sum: List[int] = self.get_odd_suffix(
			numbers
		)
		total_sum: int = sum(numbers)
		total_count: int = 0
		for index, number in enumerate(numbers):
			if self.is_balanced(index, number, total_sum,
								even_prefix_sum, odd_suffix_sum):
				total_count += 1
		return total_count

	def get_even_prefix(self, numbers: List[int]) -> List[int]:
		even_prefix_sum: List[int] = [0] * len(numbers)
		for index, number in enumerate(numbers):
			if index != 0:
				even_prefix_sum[index] = even_prefix_sum[index - 1]
			if (index + 1) % 2 == 0:
				even_prefix_sum[index] += number			
		return even_prefix_sum

	def get_odd_suffix(self, numbers: List[int]) -> List[int]:
		# 5 5 2 7 8
		odd_suffix_sum: List[int] = [0] * len(numbers)
		for index in range(len(numbers) -1, -1, -1):
			if index != len(numbers) - 1:
				odd_suffix_sum[index] = odd_suffix_sum[index+1]
			if (index + 1) % 2 != 0:
				odd_suffix_sum[index] += numbers[index]
		return odd_suffix_sum

	def is_balanced(self, index: int, curr_value: int, 
					total_sum: int, even_prefix: List[int], 
					odd_suffix: List[int]) -> bool:
		curr_is_even: bool = (index + 1) % 2 != 0  # Since its zero indexed
		prefix_sum: int = even_prefix[index]
		suffix_sum: int = odd_suffix[index]
		# Removes curr from sum
		if curr_is_even:
			prefix_sum -= curr_value
		else:
			suffix_sum -= curr_value
		new_sum = prefix_sum + suffix_sum
		return new_sum == (total_sum - curr_value) // 2

		
		


