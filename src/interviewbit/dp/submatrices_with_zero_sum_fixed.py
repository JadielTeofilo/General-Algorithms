"""
Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the sub matrix is equal to 0. (note:  elements might be negative).


_     _
-8 5  7 
3  7 -8
5 -8  9


-8 5
 3 7
= 7

 0  0 0
-8 -3 4
 3 10 2
 5  3 12

For each row, calculate the running sum. 
For each pair of columns, calculate the sum of the row inside those columns.
Keep the running sum of that sum, using it as the pattern ever growing bars suggest


O(m*m*n) time complexity where m =col n=row
O(m*n) space


In - matrix: List[List[int]]
Out - int

"""
import collections
from typing import List, Iterable, Dict


Matrix = List[List[int]] 
Pair = collections.namedtuple('Pair', 'first_col second_col')


class Solution():

	def solve(self, matrix: Matrix) -> int:
		if not matrix or not matrix[0]:
			return 0
		matrix_sum: Matrix = self.build_matrix_sum(matrix)
		result: int = 0
		for first_col, second_col in self.get_col_pairs(matrix): 
			cache: Dict[int, int] = collections.defaultdict(int)
			cache[0] = 1  # The start of the running sum is zero, hence gets 1
			row_sum: int = 0 
			for row in range(len(matrix)):
				row_sum += self.get_row_sum(matrix_sum, first_col, 
											    second_col, row) 
				if row_sum in cache:
					result += cache[row_sum]
				cache[row_sum] += 1

		return result

	def build_matrix_sum(self, matrix: Matrix) -> Matrix:
		matrix_sum: Matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
		for row in range(len(matrix)):
			matrix_sum[row][0] = matrix[row][0]
			for col in range(1, len(matrix[0])):
				matrix_sum[row][col] = matrix[row][col] + matrix_sum[row][col - 1]
		return matrix_sum
			
	def get_row_sum(self, matrix_sum: Matrix, first_col: int, 
					second_col: int, row: int) -> int:
		start_sum: int = (matrix_sum[row][first_col - 1] 
						  if first_col > 0  else 0)
		return matrix_sum[row][second_col] - start_sum

	def get_col_pairs(self, matrix: Matrix) -> Iterable[Pair]:
		for first in range(len(matrix[0])):
			for second in range(first, len(matrix[0])):
				yield Pair(first, second)
