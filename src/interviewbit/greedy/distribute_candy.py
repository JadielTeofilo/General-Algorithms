"""

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Input Format:

The first and the only argument contains N integers in an array A.

Output Format:

Return an integer, representing the minimum candies to be given.


In - children

Out - int


1 2 8 3 9 0 0 2 2
0 0 1 0 1 0 0 0 0

1 2 3 2
1 2 3 1

1 5 2 1
      

6 5 4
2 1 0
3 2 


1 2 5 1




Can we have negative values?
yes

we could build pre calculation telling num of consecutive smaller elements to the right
iterate on numbers, looking at prev
if smaller then prev, set value to one, if bigger add one to prev value
if suffix value - curr value <=0 make value += suffix value

O(n) space and time where n is the num of children

"""
from typing import List


class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, children: List[int]) -> int:
		suffix: List[int] = self.build_suffix(children)
		result: List[int] = [0] * len(children)
		for i, child in enumerate(children):
			if i == 0 or child < children[i - 1]:
				value: int = 1
			elif child == children[i - 1]:
				value: int = result[i - 1]
			else:
				value: int = result[i - 1] + 1
			self.adjust_candy(result, suffix, i)
		return sum(result)

	def adjust_candy(self, result: List[int], 
					 suffix: List[int], i: int) -> None:
		diff: int = suffix[i] - result[i]
		if diff > 0:
			return
		result[i] = suffix[i] + 1

	def build_suffix(self, children: List[int]) -> List[int]:
		""" Builds suffix cache that says the num of 
			consecutive desc elements to the right
		"""
		suffix: List[int] = [0] * len(children)
		for i in range(len(children) - 2,  -1, -1):
			if children[i] > children[i + 1]:
				suffix[i] = suffix[i + 1] + 1
			elif children[i] == children[i + 1]:
				suffix[i] = suffix[i + 1]
		return suffix


			

	

