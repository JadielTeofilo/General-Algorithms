"""
Problem Description

Given a sorted array A containing N integers both positive and negative.

You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

Try to this in O(N) time.

-12 -11 -2 -1 1 2 5 9 20 26

12 11 2 1 1 2 5 9 20 26


-2 1 3
4 1 9


Split in two lists, left  and right (negatives and positives)
Remove the signal and merge them with merge sorted
generate squares

In - numbers: List[int]
Out -  List[int]


"""
import collections
from typing import List


TwoLists = collections.namedtuple('TwoLists', 'left right')


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def solve(self, numbers: List[int]) -> List[int]:
		two_lists: TwoLists = self.split_list(numbers)
		result: List[int] = self.merge_sorted(two_lists)
		return [int(number**2) for number in result]

	def split_list(self, numbers: List[int]) -> TwoLists:
		""" Splits the list into the negative numbers and positive ones 
			Makes the negatives positive """
		return TwoLists(
			[number * -1 for number in numbers if number < 0],
			[number for number in numbers if number >= 0],
		)

	def merge_sorted(self, two_lists: TwoLists) -> List[int]:
		left_size: int = len(two_lists.left)
		right_size: int = len(two_lists.right)	
		merged: List[int] = []
		i, j = 0, 0
		while i < left_size and j < right_size:
			if two_lists.left[i] < two_lists.right[j]:
				merged.append(two_lists.left[i])
				i += 1
			else:
				merged.append(two_lists.right[j])
				j += 1
		if i < left_size:
			merged.extend(two_lists.left[i:])
		else:
			merged.extend(two_lists.right[j:])
		return merged



