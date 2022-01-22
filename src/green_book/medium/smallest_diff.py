"""
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference.

1 3 15 11 2
23 127 235 19 8

In left: List[int], right: List[int]
Out Tuple[int, int]

What happens if there are two with the same diff
return any of them

What happens if there are two elements equal
return zero


1 2 3 8 11 15 23 19 127 235

O(n log n) where n is the sum of the size of both lists
O(n) space complexity where n is the sum of both


"""
import collections
import enum
import math
from typing import List, Union, Optional


class NumberType(enum.Enum):
	first = 1
	second = 2


Result = collections.namedtuple('Result', 'first_value second_value')
NumberData = collections.namedtuple('NumberData', 'value type')


def smallest_diff(first: List[int], second: List[int]) -> Result:
	""" Finds the smallest diff tuple between both lists """
	if not first or not second:
		raise ValueError('One or more empty inputs')
	all_numbers: List[NumberData] = build_all_numbers(first, second)
	all_numbers.sort(key=lambda x: x.value)
	return find_smallest_diff(all_numbers)


def build_all_numbers(first: List[int], 
					  second: List[int]) -> List[NumberData]:
	""" Concatenates both lists with 
		metadata of the origin list 
	"""
	first = [NumberData(number, NumberType.first) 
			 for number in first]
	second = [NumberData(number, NumberType.second) 
			  for number in second]
	return first + second


def find_smallest_diff(numbers: List[NumberData]) -> Result:
	min_diff: Union[float, int] = math.inf
	result: Result =  Result(None, None)
	for i in range(len(numbers) - 1):
		# Skips to next if both are from same list
		if numbers[i + 1].type == numbers[i].type:
			continue
		curr_diff: int = numbers[i + 1].value - numbers[i].value
		if curr_diff < min_diff:
			min_diff = curr_diff
			result = build_result(numbers, i)
	return result


def build_result(numbers: List[NumberData], i: int) -> Result:
	if numbers[i].type == NumberType.first:
		first_value: int = numbers[i].value 
		second_value: int = numbers[i + 1].value
	else:
		first_value: int = numbers[i + 1].value
		second_value: int = numbers[i].value
	return Result(first_value, second_value)


def smallest_diff_better(first: List[int], 
						 second: List[int]) -> List[int]:
	first.sort()
	second.sort()
	first_index: int = 0
	second_index: int = 0
	min_diff: Union[float, int] = math.inf
	result: List[int] = []
	while first_index < len(first) and second_index < len(second):
		if abs(first[first_index] - second[second_index]) < min_diff:
			min_diff = abs(first[first_index] - second[second_index])
			result = [first[first_index], second[second_index]]
		if first[first_index] < second[second_index]:
			first_index += 1
		else:
			second_index += 1
	return result



first = [int(a) for a in ('1 3 15 11 2'.split(' '))]
second = [int(a) for a in ('23 127 235 19 8'.split(' '))]

print(smallest_diff_better(first, second))

