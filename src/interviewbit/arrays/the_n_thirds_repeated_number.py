"""
You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example:

Input: [1 2 3 1 1]
Output: 1 
1 occurs 3 times which is more than 5/3 times.


43344



Pattern majority element

consider first element, iterate until its no longer more than 1/3 of the size of the array
keep two elements, left and right, iterate on numbers
if none are set, set left, then right
if both are set, and new num is equal left or right add one
if diff, subtract one

O(n) time complexity, O(1) space complexity where n is the size of numbers


In - numbers: List[int]
Out - int

"""
import collections
from typing import Dict, List


Count = Dict[int, int]


class Solution:

	def solve(self, numbers: List[int]) -> int:
		count: Count = collections.defaultdict(int)
		for number in numbers:
			self.pop_empty_elements(count)
			if number in count or len(count) < 2:
				count[number] += 1
				continue
			if len(count) == 2:
				self.subract_from_all(count)
				continue
		for key in count:
			if self.is_target(key, numbers):
				return key
		return -1

	def pop_empty_elements(self, count: Count) -> None:
		for key in list(count):
			if count[key] == 0:
				count.pop(key)

	def subract_from_all(self, count: Count) -> None:
		for key in count:
			count[key] -= 1
	
	def is_target(self, key: int, numbers: List[int]) -> bool:
		return numbers.count(key) > (len(numbers) // 3)
				
			

