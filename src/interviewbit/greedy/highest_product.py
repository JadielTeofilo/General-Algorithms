"""
Highest Product

Given an array A, of N integers A.

Return the highest product possible by multiplying 3 numbers from the array.

NOTE:  Solution will fit in a 32-bit signed integer.


given two negatives make a positive, we can not ignore the negatives
we can not just take the three bigger numbers

kadanes algo wont work cuz we only want 3 elements

prefix suffix magic might do
with tidy triplets

keep a prefix array with max and min nums up to a given point

iterate on the nums checking the product against the max product

O(n) time complexity
O(n) space complexity

In - numbers: List[int]
Out - int

"""
import collections
import math
from typing import List, Union


Cache = collections.namedtuple('Cache', 'min max')


class Solution:
	# @param A : list of integers
	# @return an integer
	def maxp3(self, numbers: List[int]) -> int:
		prefix: List[Cache] = self.build_prefix(numbers)
		suffix: List[Cache] = self.build_suffix(numbers)
		max_product: Union[int, float] = -math.inf
		for index, number in enumerate(numbers): 
			if index in [0, len(numbers) - 1]:
				continue
			max_product = max(
				max_product, 
				number * prefix[index].min * suffix[index].max,
				number * prefix[index].max * suffix[index].min,
				number * prefix[index].min * suffix[index].min,
				number * prefix[index].max * suffix[index].max,
			)
		return int(max_product)

	def build_prefix(self, numbers: List[int]) -> List[Cache]:
		prefix: List[Cache] = [Cache(math.inf, -math.inf)] * len(numbers)
		for i in range(1, len(numbers)):
			prefix[i] = Cache(min=min(numbers[i-1], prefix[i-1].min),
							  max=max(numbers[i-1], prefix[i-1].max))
		return prefix


	def build_suffix(self, numbers: List[int]) -> List[Cache]:
		suffix: List[Cache] = [Cache(math.inf, -math.inf)] * len(numbers)
		for i in range(len(numbers)-2, -1, -1):
			suffix[i] = Cache(min=min(numbers[i+1], suffix[i+1].min),
							  max=max(numbers[i+1], suffix[i+1].max))
		return suffix

