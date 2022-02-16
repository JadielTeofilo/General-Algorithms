"""
Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the sub matrix is equal to 0. (note:  elements might be negative).

Example:

Input

-8 5  7
3  7 -8
5 -8  9


-8 -3 4
3  10 2
5 -3  6

build a cache matrix with the sum up to a given point

1 0 3
2 9 2
      _
1  1  4 
3 12  17
dp[r][c] = nums[r][c] + dp[r-1][c] + dp[c-1][r] - dp[c-1][r-1]

iterate on the positions, for every position iterate on the possible positions bellow it, 
calculate the sum using the dp matrix
sum = dp[end_r][end_c] - dp_left_last_line - dp_above_first_line + dp[start_r-1][end_c-1]


Output

2

O(n^2) time where n is the number of elements in the matrix
O(n^2) space where n is the number of elements in the matrix

In - numbers: List[List[int]] 
Out - int


"""
from typing import List, Tuple, Iterable


Matrix = List[List[int]]


class Solution:
	# @param A : list of list of integers
	# @return an integer
	#-2, -1, 
	# 1, 2
	#
	#-2 -3
	#-1  0
	def solve(self, matrix: Matrix) -> int:
		dp: Matrix = self.build_dp_matrix(matrix) 
		return self.find_sums_equals(dp, 0)

	def find_sums_equals(self, dp: Matrix, target: int) -> int:
		result: int = 0
		for start_row, start_col in self.get_positions(0, 0, dp):
			for end_row, end_col in self.get_positions(start_row, 
													   start_col, dp):
				if self.find_sum(start_row, start_col, 
							end_row, end_col, dp) == target:
					result += 1
		return result

	def find_sum(self, start_row: int, start_col: int, 
				 end_row: int, end_col: int, dp: Matrix) -> int:
		return (self.get_value(dp, end_row, end_col) -
				self.get_value(dp, end_row, start_col - 1) -
				self.get_value(dp, start_row - 1, end_col) +
				self.get_value(dp, start_row - 1, start_col - 1))

	def get_value(self, matrix: Matrix, row: int, col: int) -> int:
		if (not matrix or row >= len(matrix) or col >= len(matrix[0]) 
			or row < 0 or col < 0):
			return 0
		return matrix[row][col]
		
					
	def build_dp_matrix(self, matrix: Matrix) -> Matrix:
		if not matrix:
			return matrix
		dp: Matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
		for row, col in self.get_positions(0, 0, matrix):
			dp[row][col] = (matrix[row][col] + self.get_value(dp, row-1, col) + 
							self.get_value(dp, row, col - 1) - 
							self.get_value(dp, row - 1, col - 1))
		return dp 

	def get_positions(self, row_start: int, col_start: int, 
					  matrix: Matrix) -> Iterable[Tuple[int, int]]:
		if not matrix:
			return
		for row in range(row_start, len(matrix)):
			for col in range(col_start, len(matrix[0])):
				yield row, col
		
