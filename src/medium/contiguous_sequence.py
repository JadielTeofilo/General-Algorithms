"""
 You are given an array of integers (both positive and negative). Find the
contiguous sequence with the largest sum. Return the sum.
EXAMPLE
Input 2, -8, 3, -2, 4, -10
OutputS (i.e., {3, -2, 4})

keep running sum


"""
import math
from typing import Union, List


def max_sum(numbers: List[int]) -> int:
	result: Union[int, float]  = -math.inf
	curr_max: Union[int, float]  = -math.inf
	for number in numbers:
		if curr_max < 0:
			curr_max = number
		else:
			curr_max += number
		result = max(result, curr_max)	
	return int(result)


print(max_sum([2, -8, 3, -2, 4, -10]))
