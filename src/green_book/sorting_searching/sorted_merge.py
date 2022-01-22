"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

In - left: List[int], right: List[int]
Out - None


[ , , , ,1,4,6,7]
[2,3,4,5]

[1]


O(n) time complexity where n is the sum of both array sizes
O(1) space

"""
from typing import List


def sorted_merge(first: List[int], second: List[int]) -> None:
	""" Does inplace sorted merge on the first list """
	if len(first) < len(second):
		raise ValueError('The first list must fit the second')
	right_pointer: int = move_elements_to_the_end(first)
	left_pointer: int = 0
	insert_pointer: int = 0
	while (right_pointer < len(first) 
		   and left_pointer < len(second)):
		if first[right_pointer] < second[left_pointer]:
			first[insert_pointer] = first[right_pointer]
			right_pointer += 1
		else:
			first[insert_pointer] = second[left_pointer]
			left_pointer += 1
		insert_pointer += 1
	while right_pointer < len(first):
		first[insert_pointer] = first[right_pointer]
		right_pointer += 1 
		insert_pointer += 1
	while left_pointer < len(second):
		first[insert_pointer] = second[left_pointer]
		left_pointer += 1
		insert_pointer += 1


def move_elements_to_the_end(first: List[int]) -> int:
	""" Moves all elements to the end of the list, 
		given the list has null elements at the end """
	index_of_last_element: int = -1
	for index, item in enumerate(first):
		if item is None:
			index_of_last_element = index - 1
			break
	insert_pointer: int = len(first) - 1  # Last index
	while index_of_last_element >= 0:
		first[insert_pointer] = first[index_of_last_element]
		insert_pointer -= 1
		index_of_last_element -= 1
	return insert_pointer + 1


first = [1,4,6,7,None, None,None, None]
second = [2,3,4,5]
print(first)
sorted_merge(first, second)
print(first)
import pdb;pdb.set_trace()
