"""
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.

In - numbers: List[int], target: int
Out - int


15 16 19 20 25 1 3 4 5 7 10 14

Check edge of the current list being analyzed, if rotated, do both sides, 
else only the target size


O(log(n)) time complexity where n is the size of numbers
This is because, even when he does both sides, one of the sides will be O(1)

"""
from typing import List


def search_rotated(numbers: List[int], target: int) -> int:
	""" 
		Finds index of target on a rotated list numbers 

		Returns -1 if did not find target
	"""
	if not numbers:
		raise ValueError('Numbers can not be empty')		
	return search_helper(numbers, target, 
						 start=0, end=len(numbers) - 1)


def search_helper(numbers: List[int], target: int, 
				  start: int, end: int) -> int:
	""" Does modified bin search to find target on numbers """
	if start > end:
		return -1
	mid: int = (start + end) // 2
	if numbers[mid] == target:
		return mid
	if numbers[mid] >= numbers[end]:
		left_search: int = search_helper(numbers, target, 
										start, mid - 1)
		right_search: int = search_helper(
			numbers, target, mid + 1, end
		)
		return (left_search if left_search != -1 else right_search)
	if numbers[mid] > target:
		return search_helper(numbers, target, start, mid - 1)
	return search_helper(numbers, target, mid + 1, end)


print(search_rotated([15, 16,19, 20, 25, 1, 3, 4, 5,7, 10, 14], 5))
print(search_rotated([15, 16,19, 20, 25, 1, 3, 4, 5,7, 10, 14], 2))
print(search_rotated([15, 16,19, 20, 25, 1, 3, 4, 5,7, 10, 14], 16))
print(search_rotated([15, 1, 3, 4, 5,7, 10, 14], 16))
import pdb;pdb.set_trace()
		
