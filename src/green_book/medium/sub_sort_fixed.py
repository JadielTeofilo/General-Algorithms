"""
Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted
elements mthrough n, the entire array would be sorted. Minimize n - m (that is, find the smallest
such sequence).
EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9)

The idea is to identify tree blocks, left, mid and right
Increase mid than to fix the misplaced values

"""
import dataclasses
from typing import Union, List


@dataclasses.dataclass
class Range:
	start: int = 0
	end: int = 0


def sub_sort(numbers: List[int]) -> Range:  # 5 4
	""" Finds the range, that, if sorted would 
		sort the whole array 
	"""
	# TODO check for empty and sorted input
	mid: Range = find_mid_range(numbers)  # start = 1 end = 0
	left_max: int = max(numbers[:mid.end + 1])  # max([5])
	right_min: int = min(numbers[mid.start:])  # min(4)
	increase_range(mid, left_max, right_min, numbers)
	return mid


def find_mid_range(numbers: List[int]) -> Range:
	range_: Range = Range()
	for i in range(1, len(numbers)):
		if numbers[i-1] > numbers[i]:
			range_.start = i
			break
	for i in range(len(numbers)-2, -1, -1):
		if numbers[i] < numbers[i-1]:
			range_.end = i - 1
			break
	return range_
		

def increase_range(mid: Range, left_max: int, 
				   right_min: int, numbers: List[int]) -> None:
	""" Updates the mid range by checking the max and 
		min values ahead and before """
	for i in range(0, mid.start): 
		if numbers[i] > right_min:
			mid.start = i
			break
	for i in range(len(numbers)-1, mid.end, -1):
		if numbers[i] < left_max:
			mid.end = i
			break


print(sub_sort([ 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
print(sub_sort([5, 4]))

