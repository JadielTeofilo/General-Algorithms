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

col2 - col1 == 1


"""
import collections
import dataclasses
from typing import List, Optional, Union


@dataclasses.dataclass
class Position: 
	row: int
	col: int


DivisorElements = collections.namedtuple(
	'DivisorElements', 'smaller bigger'
)  # Two elements next to each other on a diagonal
Quadrant = collections.namedtuple(
	'Quadrant', 'start end'
)
_DivOrPos = Union[Position, DivisorElements, None]


def search(matrix: List[List[int]], start: Position, 
		   end: Position, target: int) -> Optional[Position]:
	if not matrix or not matrix[0]:
		raise ValueError('Empty matrix')
	if start == end:
		return (start if matrix[start.row][start.col] == target 
				else None)
	divisor_elements: _DivOrPos = get_divisor_elements(
		matrix, start, end, target
	)
	#import pdb;pdb.set_trace()
	# Case element is not on matrix
	if not divisor_elements:
		return None
	# Case where the target is in the diagonal
	if isinstance(divisor_elements, Position):
		return divisor_elements
	quadrants: List[Quadrant] = build_quadrants(
		divisor_elements, start, end
	)
	#print(quadrants)
	# Search the two quadrants left
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
	end = fix_end_position(start, end)
	aux_end = dataclasses.replace(end)
	start = dataclasses.replace(start)
	aux_start = dataclasses.replace(start)
	while (start.row <= end.row and 
		   start.col <= end.col):
		mid: Position = Position(
			row=(start.row + end.row) // 2,
			col=(start.col + end.col) // 2,
		)
		# Returns position if target is on diagonal
		if matrix[mid.row][mid.col] == target:
			return mid
		if matrix[mid.row][mid.col] > target:
			# Returns None for elements not on matrix
			if mid.row == 0 or mid.col == 0:
				return None
			# Returns the divisor elements in 
			# case they border target		
			last: Position = Position(mid.row - 1, mid.col - 1)
			if matrix[last.row][last.col] < target:
				return DivisorElements(last, mid)
			end.row = mid.row - 1
			end.col = mid.col - 1
		else:
			start.row = mid.row + 1
			start.col = mid.col + 1
	return DivisorElements(aux_end, Position(aux_end.row+1, aux_end.col+1))


def fix_end_position(start: Position, 
				     end: Position) -> Position:
	""" Finds the end position of the diagonal 
		according to the matrix size """
	diagonal_size: int = min(end.row - start.row, 
							 end.col - start.col)
	return Position(
		row=start.row + diagonal_size,
		col=start.col + diagonal_size,
	)


def build_quadrants(
	divisors: DivisorElements, 
    start: Position, end: Position
) -> List[Quadrant]:
	"""
		Finds the upper right quadrand and the 
		lower left given the divisor elements
	"""
	lower_quadrant: Quadrant = Quadrant(
		start=Position(divisors.bigger.row, start.col),
		end=Position(end.row, divisors.smaller.col)
	)
	upper_quadrant: Quadrant = Quadrant(
		start=Position(start.row, divisors.bigger.col),
		end=Position(divisors.smaller.row, end.col),
	)
	quadrants: List[Quadrant] = [upper_quadrant, lower_quadrant]
	return [quadrant for quadrant in quadrants 
			if is_valid(quadrant, end)]


def is_valid(quadrant: Quadrant, end: Position) -> bool:
	""" Checks if quadrant is outside of matrix """
	return (quadrant.end.row <= end.row
		    and quadrant.end.col <= end.col
			and quadrant.start.row <= end.row
			and quadrant.start.col <= end.col)



asdf = [
[ 1, 6, 8,10,12],
[ 2, 7, 9,11,13],
[ 3, 8,10,20,22],
[10,11,12,21,24],
]
print(search(asdf, Position(0,0), Position(3,4), 22))
import pdb;pdb.set_trace()
