"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.



1 2 3
4 5 6
7 8 9
Return the following:
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


In - matrix: List[List[int]]
Out - List[List[int]]


Iterate on the first line and then on the last column
generate diagonal starting from the above values
to generate diagonal, just decrease one on the line and one on the column until there are no more valid places


"""
import collections
from typing import List, Iterable


Matrix = List[List[int]]
Position = collections.namedtuple('Position', 'row col')


class Solution:
	# @param A : list of list of integers
	# @return a list of list of integers
	def diagonal(self, matrix: Matrix) -> Matrix:
		if not matrix or not matrix[0]:
			return [[]]
		result: Matrix = []
		for position in self.first_line_positions(len(matrix)):
			result.append(self.generate_diagonal(position, matrix))
		for index, position in enumerate(self.last_column_positions(len(matrix))):
			if index == 0:
				continue
			result.append(self.generate_diagonal(position, matrix))
		return result

	def first_line_positions(self, size: int) -> Iterable[Position]:
		for i in range(size):
			yield Position(0, i)

	def last_column_positions(self, size: int) -> Iterable[Position]:
		for i in range(size):
			yield Position(i, size - 1)

	def generate_diagonal(self, position: Position, matrix: Matrix) -> List[int]:
		diagonal: List[int] = []
		while self.is_valid(position, matrix):
			diagonal.append(matrix[position.row][position.col])
			position = Position(position.row + 1, position.col - 1)
		return diagonal

	def is_valid(self, position: Position, matrix: Matrix) -> bool:
		size = len(matrix)
		if position.row < 0 or position.col < 0:
			return False
		return position.row < size and position.col < size
			
