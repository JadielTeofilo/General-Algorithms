"""
Problem Description

Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

NOTE: You should make minimum number of comparisons.


In - numbers: List[int]
Out - Sum

[2, 1 , 4 , 6, 2 , 9 ]

We could use two heaps, one max, other min 
Or just iterate on the array keeping track of min and max
	The comparison num here is 2*n
Or use divide and conquer
T(n) = 2 + 2*T(n/2)
...
T(2) = 1
T(1) = 0



Problem Constraints

1 <= N <= 105

-109 <= A[i] <= 109



Input Format

First and only argument is an integer array A of size N.


Output Format

Return an integer denoting the sum Maximum and Minimum element in the given array.



"""
import math
from typing import Union


class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A) -> int:
		min_: Union[float, int] = math.inf
		max_: Union[float, int] = -math.inf
		for number in A:
			if number < min_:
				min_ = number
			if number > max_:
				max_ = number
		return int(max_ + min_)
