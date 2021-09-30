"""
Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.


Problem Constraints

1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format

First argument is an integer array A.

Second argument is an integer B.



Output Format

Return an integer denoting the maximum possible sum of elements you picked.


In - numbers: List[int], picks: int

Out - int


Ex: 
picks = 3
numbers = 2 8 1 2 9 1 7 6
2  8  1  2  9  1  7  6
0  2  10 11 13 22 23 30 36
36 34 26 25 23 14 13 6

Ask your self what are you testing mentally, what are the actual possibilities
You are testing picking 0-x elements at the beginning and x-0 elements at the end

2 8 e 6

"""
import enum
import math
from typing import List, Union, Iterable


class AggregationType(enum.Enum):
	prefix = 1
	sufix = 2


class Solution:

	def solve(self, numbers: List[int], picks: int) -> Union[int, float]:
		prefix: List[int] = self.build_aggregated_sum(numbers, AggregationType.prefix)
		sufix: List[int] = self.build_aggregated_sum(numbers, AggregationType.sufix)
		result: Union[int, float] = -math.inf
		for right_pick in range(picks + 1):
			left_pick: int = picks - right_pick
			current_pick_sum: int = prefix[left_pick] + sufix[right_pick]
			result = max(result, current_pick_sum)
		return result
		
	def build_aggregated_sum(self, numbers: List[int], 
							 type: AggregationType) -> List[int]:
		aggregate: List[int] = [0]
		if type == AggregationType.prefix:
			indexes: Iterable[int] = range(0, len(numbers), 1)
		else:
			indexes: Iterable[int] = range(len(numbers)-1, -1, -1)
		for i in indexes:
			aggregate.append(aggregate[i] + numbers[i])

		return aggregate



