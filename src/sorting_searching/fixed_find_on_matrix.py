"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.

In - matrix: List[List[int]], start: Position, end: Position
Out - Position


What happens if the target is present more than once?
Just return any position

[
[ 1, 6, 8,10]
[ 2, 7, 9,11]
[ 3, 8,10,20]
[10,11,12,21]
]


"""
import collections
from typing import List, Optional, Union


Position = collections.namedtuple('Position', 'row, col')
DivisorElements = collections.namedtuple(
	'DivisorElements', 'smaller bigger'
)
Quadrant = collections.namedtuple(
	'Quadrant', 'start end'
)
_DivOrPos = Union[Position, DivisorElements]


def search(matrix: List[List[int]], start: Position, 
		   end: Position, target: int) -> Optional[Position]:
	if not matrix or not maxtrix[0]:
		raise ValueError('Empty matrix')
	if start == end:
		return (start if matrix[start.row][start.col] == target 
				else None)
	divisor_elements: _DivOrPos = get_divisor_elements(
		matrix, start, end
	)  # TODO
	# Case where the target is in the diagonal
	if isinstance(divisor_elements, Position):
		return divisor_elements
	quadrants: List[Quadrant] = build_quadrants(  # TODO
		divisor_elements, start, end
	)
	for quadrant in quadrants:
		result: Optional[Position] = search(
			matrix, quadrant.start, quadrant.end, target
		)
		if result is not None:
			return result
	return None

def get_divisor_elements(matrix: List[List[int]], 
						 start: Position, 
						 end: Position, target: int) -> _DivOrPos:
	"""
		Finds either two elements in the main diagonal 
		that borders the target or the element in the 
		main diagonal that has the target value
	"""
	# For the case of unsquare matrix
	start, end = fix_positions(start, end)  # TODO
	
	row: int = start.row
	col: int = start.col
		
