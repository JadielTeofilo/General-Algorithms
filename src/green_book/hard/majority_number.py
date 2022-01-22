"""
Majority Element: A majority element is an element that makes up more than half of the items in
an array. Given a positive integers array, find the majority element. If there is no majority element,
return -1. Do this in O( N) time and O( 1) space.

In - List[int]
Out - int

use quick select


run the partition algo and continue the recursion on the bigger side

1 5 9 2 5 9 5 5 5
1 2 3 5 5 5 5 5 9 9
1 2 5 5 5 5 5 9 9

partition(w)

"""
from typing import List, Optional


def find_majority_element(numbers: List[int]) -> int:
	# TODO validate input
	half: int = len(numbers) // 2  # 4
	start: int = 0
	end: int = len(numbers) - 1
	last_pivot: Optional[int] = None
	# 1 5 9 2 5 9 5 5 5
	while start <= end:  # 2 <= 6
		if all_elements_are_the_same(numbers, start, end):
			return numbers[start]
		pivot: int = find_pivot(start, end, numbers, last_pivot) # 3
		last_pivot = numbers[pivot]
		pivot = partition(numbers, start, end, pivot)  # 1
		# 1 2 5 5 5 5 5 9 9
		if (left_size(pivot, start) <= half and
			right_size(pivot, end) <= half):
			# There is no majority to be found
			return -1
		if left_size(pivot, start) > right_size(pivot, end):
			# Follows to the left side
			end = pivot
		else:
			# Follows to the right side
			start = pivot + 1
	return -1


def left_size(pivot: int, start: int) -> int:
	return (pivot - start) + 1

def right_size(pivot: int, end: int) -> int:
	return end - pivot


def partition(numbers: List[int], start: int, 
			  end: int, pivot: int) -> int:
	print(start, end, pivot, numbers)
	pivot_value: int = numbers[pivot]
	while start <= end:
		
		while numbers[start] < pivot_value:
			start += 1
		while numbers[end] > pivot_value:
			end -= 1

		if start <= end:
			numbers[start], numbers[end] = numbers[end], numbers[start]
			start += 1
			end -= 1
	print(numbers)
	return start


def find_pivot(start: int, end: int, 
			   numbers: List[int], last_pivot: int) -> int:
	initial: int = (start + end) // 2
	if numbers[initial] != last_pivot:
		return initial
	left: int = initial
	right: int = initial
	# Finds the closer element that is different from last pivot
	# Stops when both are outside the array
	while not left < 0 and not right >= len(numbers):
		left -= 1
		if left >= 0 and numbers[left] != last_pivot:
			return left
		right += 1
		if right < len(numbers) and numbers[right] != last_pivot:
			return right
	raise ValueError('There is no pivot different from last pivot')


def all_elements_are_the_same(numbers: List[int], start: int, 
							  end: int) -> bool:
	if not numbers:
		raise ValueError('Empty list')
	value: int = numbers[0]
	for i in range(start, end + 1):
		if value != numbers[i]:
			return False
	return True


print(find_majority_element([1,5,9,2,5,9,5,5,5]))
