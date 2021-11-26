"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.


[9, 9]

iterate on the numbers left to right
keep goes, if sum > 10 output is mod 10 and curr receives 1
if goes is zero, continue normally until the end


have a result list and append elements to it
return it reversed

In - numbers: List[int]
Out - int

"""
from typing import List


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def plusOne(self, numbers: List[int]) -> List[int]:
		goes: int = 1
		result: List[int] = []
		for i in range(len(numbers) - 1, -1, -1):
			curr: int = numbers[i] + goes
			goes = 1 if curr >= 10 else 0
			result.append(curr % 10)
		# In case there is a goes at the last element
		result.append(goes)
		self.remove_trailing_zeros(result)
		result.reverse()
		return result

	def remove_trailing_zeros(self, numbers: List[int]) -> None:
		for i in range(len(numbers) - 1, -1, -1):
			if numbers[i] != 0:
				break
			numbers.pop()

