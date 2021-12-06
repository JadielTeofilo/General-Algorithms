"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.



In - digits: List[int]
Out - str

[30, 30, 34, 32, 50, 90, 3114]

311432 > 323114

30 3

sort using the above comparison to determine the bigger number


O(m*nlogn) where n is the size of numbers and m is thd size of digits the biggest number

"""
from typing import List


class Solution:
	# @param A : tuple of integers
	# @return a strings
	def largestNumber(self, numbers: List[int]) -> str:
		return ''.join(quicksort(numbers))


def quicksort(numbers: List[int]) -> List[str]:
	if not numbers:
		return []
	pivot_index: int = (len(numbers) - 1)//2
	pivot: int = numbers[pivot_index]
	smaller: List[int] = [num for num in numbers if is_smaller(num, pivot)]  #TODO
	bigger: List[int] = [num for num in numbers if not is_smaller(num, pivot)]
	return quicksort(smaller) + [str(pivot)] + quicksort(bigger)

def is_smaller(target: int, other: int) -> bool:
	""" Number is considered smaller if it makes up a 
		bigger number by being concatenated in front 

		This way, such numbers will be on the left """
	return str(target) + str(other) > str(other) + str(target)
