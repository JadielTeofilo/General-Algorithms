"""
Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.

In - None
Out - List[List[Optional[int]]]



0 1
1 2
2 3

1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0
0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0



This is a variation of the Sudoku prolem 

On the sudoku problem the way to generate a board is the following:
	Choose a number
	On the first row the ways are ways(0, 0) + ways(0, 1) .. ways(0, 8). Meaning the ways considering that you have that number on that position.
	You recurse into that to build all possibilities, always checking for valid positions.

Pattern 17 If the problem at some point presents a matrix that at a given row there will always be only one element set, you should use a List[Tuple[value, column]] to represent it.


"""
from typing import List, Iterable, Optional


Way = List[Optional[int]]
SIZE: int = 8


def queen_ways() -> Iterable[Way]:
	""" 
		Finds different ways of arranging 
		queens on a SIZExSIZE grid
	"""
	# Initialize the first row with column zero
	yield from ways_helper(row=0, current_way=[None] * SIZE)


def ways_helper(row: int, current_way: Way) -> Iterable[Way]:
	"""
		Recurses to find the queen ways 

		Arguments:
			row: current row being analysed
			current_way: An array of rows that says which column 
				is set on that row
	"""
	if row >= SIZE:
		yield current_way.copy()
		return
	for column in range(SIZE):
		if is_valid(row, column, current_way):
			current_way[row] = column
			yield from ways_helper(row + 1, current_way)


def is_valid(row: int, column: int, current_way: Way) -> bool:
	"""
		Checks if there is a queen on same row, column 
		or diagonal
	"""
	# Same row is granted not to have a queen, since we are 
	# iterating on columns of same row
	
	for prev_row in range(row):
		# Same column
		if column == current_way[prev_row]:
			return False
		# Same diagonal
		col_diff: int = abs(column - current_way[prev_row])
		row_diff: int = abs(row - prev_row)
		if col_diff == row_diff:
			return False

	return True


import pdb;pdb.set_trace()
