"""
16.16 Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted. Minimize n - m(that is, find the smallest such sequence). 
EXAMPLE
Input 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 15, 16, 18, 19
Output: (3, 9)

In - numbers: List[int]
Out - Range


1 2 3 7 8 2

create a max_before and min_ahead list
max_before None 1 2 3 7 8
min_ahead 2 2 2 2 2 None

O(n) space and time complexity where n is the size of numbers

"""
import collections
import math
from typing import Union, List, Optional


Range = collections.namedtuple('Range', 'start end')


def sub_sort(numbers: List[int]) -> Range:
	""" 
		Finds the smallest sub range, that, if 
		sorted makes the whole list sorted 
	"""
	max_before: List[Union[float, int]] = build_max_before(numbers)
	min_after: List[Union[float, int]] = build_min_after(numbers)
	return Range(find_start(numbers, min_after),
				 find_end(numbers, max_before)) 


def build_max_before(numbers: List[int]) -> List[Union[int, float]]:
	max_before: List[Union[int, float]] = []
	curr_max: Union[int, float] = -math.inf
	for number in numbers:
		max_before.append(curr_max)
		curr_max = max(curr_max, number)
	return max_before


def build_min_after(numbers: List[int]) -> List[Union[int, float]]:
	# 1 2 3 4 5
	# 2 3 4 5 inf
	size: int = len(numbers)
	min_after: List[Union[int, float]] = [math.inf] * size
	curr_min: Union[int, float] = math.inf
	for index, number in enumerate(numbers[::-1]):
		min_after[size - 1 - index] = curr_min
		curr_min = min(number, curr_min)
	print(min_after)
	return min_after


def find_start(numbers: List[int], 
			   min_after: List[Union[int, float]]) -> Optional[int]:
	for i in range(len(numbers)):
		if numbers[i] > min_after[i]:
			return i
	return None


def find_end(numbers: List[int], 
			 max_before: List[Union[int, float]]) -> Optional[int]:
	for i in range(len(numbers) - 1, -1, -1):
		if numbers[i] < max_before[i]:
			return i
	return None


print(sub_sort([1,2,3,9,10,4,5,5]))
print(sub_sort([ 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 15, 16]))
import pdb;pdb.set_trace()
