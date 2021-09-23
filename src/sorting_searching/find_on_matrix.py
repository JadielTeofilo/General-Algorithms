"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element

In - matrix: List[List[int]], number: int
Out - Position

What happens if you have more than one element?
return anyone


regular binary search, translating start, end and mid point to matrix row, col points


O(logn) time complexity where n is the number of elements on the matrix
O(logn) space complexity from the recursion where n is the num of matrix elem 


"""
from typing import List, Optional
import collections


Position = collections.namedtuple('Position', 'row col')


def search(matrix: List[List[int]], number: int) -> Optional[Position]:
	""" Finds the position of number on the matrix """
	if not matrix or not matrix[0]:
		return
	matrix_size: int = len(matrix) * len(matrix[0])
	return binary_search(matrix, number, 
						 start=0, end=matrix_size - 1)


def binary_search(matrix: List[List[int]], 
				  number: int, start: int, 
			      end: int) -> Optional[Position]:
	if start > end:
		return
	mid: int = (start + end) // 2
	mid_position: Position = find_position(matrix, mid)
	if matrix[mid_position.row][mid_position.col] == number:
		return mid_position
	if matrix[mid_position.row][mid_position.col] > number:
		return binary_search(matrix, number, start, mid - 1)
	return binary_search(matrix, number, mid + 1, end)


def find_position(matrix: List[List[int]], index: int) -> Position:
	""" 
		Finds the correspondant position on 
		the matrix for a given array like index 
	"""
	columns: int = len(matrix[0])
	return Position(row=(index // columns), col=(index % columns))


asdf = [
[1,3,4,5],
[6,8,9,10],
[11,32,43,54],
]
print(search(asdf,
11
))
import pdb;pdb.set_trace()
