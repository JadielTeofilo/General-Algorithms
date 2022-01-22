"""
 Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
integers. For example, in the array {5, 8, 6, 2, 3, 4, 6 }, {8, 6} are peaks and {5, 2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

In - numbers: List[int]
Out - List[int]


sort and then use two pointers to build the new list

O(nlogn) time complexity where n is the amount of elements
O(n) space complexity where n is the amount of elements

"""
from typing import List, Iterable, Tuple


def sorting_peaks_and_valleys(numbers: List[int]) -> List[int]:
	""" 
		Builds a new list of numbers making interchanging 
		peaks and valleys, 
		
		ex numbers: 8 4 2 3 1
		output: 8 1 4 2 3
	"""
	numbers.sort()
	result: List[int] = []
	
	start: int = 0
	end: int = len(numbers) - 1
	while start < end:
		result.extend([numbers[start], numbers[end]])
		start += 1
		end -= 1
	if start == end:
		result.append(numbers[start])  # Adds the remaining mid element

	return result


"""
O(n) for implementation without sorting
5 1 3 4 4 5

"""
def peaks_and_valleys(numbers: List[int]) -> List[int]:
	"""
		Changes array of numbers so that it is formed 
		of peaks and valleys
	"""	
	for left, mid, right in sliding_window(numbers):
		if is_a_valley(numbers[left], numbers[mid], numbers[right]):
			continue
		create_valley(numbers, left, mid, right)

	return numbers


def create_valley(numbers: List[int], left: int, 
				  mid: int, right: int) -> None:
	if numbers[left] < numbers[right]:	
		swap(numbers, left, mid)
	else:
		swap(numbers, right, mid)
	

def sliding_window(
	numbers: List[int], size=3
) -> Iterable[Tuple[int, int, int]]:
	""" Builds a generator for indexes on a sliding window """
	for i in range(0, len(numbers), 2):
		left: int = i
		# For elements outside the list, 
		# use the same index, 
		# since it will still be a valid valley
		mid: int = i + 1 if i + 1 < len(numbers) else i
		right: int = i + 2 if i + 2 < len(numbers) else i
		yield left, mid, right


def is_a_valley(left_num: int, mid_num: int, right_num: int) -> bool:
	return left_num >= mid_num <= right_num


def swap(numbers: List[int], first: int, second: int) -> None:
	numbers[first], numbers[second] = numbers[second], numbers[first]



print(peaks_and_valleys([2,3,4,5,6,6,8,10]))
print(peaks_and_valleys([5,3,1,2,3]))
print(peaks_and_valleys([5,3,1,6]))

import pdb;pdb.set_trace()

