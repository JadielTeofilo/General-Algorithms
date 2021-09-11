"""
Magic Index: A magic index in an array A [1 ... n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP

What if the values are not distinct?

In - List[int]

Out - int magix index


If there is more than one, what should I return?
You can return the first one

[-3 -2 -1 3 7 7 7 10 11 12 13 14]
  0  1  2 3 4 5 6 7  8  9  10 11

A[6] = 7

O(log(n)) time complexity where n is the number of numbers
O(1) space complexity 


[0 0 1 2 3 3]


"""
from typing import List, Optional


def find_magic_index(numbers: List[int]) -> Optional[int]:
	"""
		Finds if exists a given number where array index == number
	"""
	if not numbers:
		return None
	start: int = 0
	end: int = len(numbers) - 1
	
	while start <= end:
		mid: int = (start + end) // 2
		if numbers[mid] == mid:
			return mid
		if numbers[mid] < mid:
			start = mid + 1
		else:
			end = mid - 1

	return None


def find_magic_index_duplicates(numbers: List[int]) -> Optional[int]:
	"""
		Finds the magic index on an array with duplicates
	"""
	return magic_index_helper(numbers, start=0, end=len(numbers) - 1)


def magic_index_helper(numbers: List[int], start: int, 
					   end: int) -> Optional[int]:
	if start > end:
		return None
	
	mid: int = (start + end) // 2
	
	if numbers[mid] == mid:
		return mid

	# Does left side
	left_attempt: Optional[int] = magic_index_helper(
		numbers, 
		start=start, 
 	    end=min(mid - 1, numbers[mid])
	)
	if left_attempt:
		return left_attempt

	# Does right side
	return magic_index_helper(
		numbers, 
		start=max(mid + 1, numbers[mid]),
		end=end
	)
	

import pdb;pdb.set_trace()	


