"""
Given a 2D integer matrix A of size N x M.

From A[i][j] you can move to A[i+1][j], if A[i+1][j] > A[i][j], or can move to A[i][j+1] if A[i][j+1] > A[i][j].

The task is to find and output the longest path length if we start from (0, 0).

NOTE:

If there doesn't exist a path return -1.


 A = [  [1, 2, 3, 4]
        [2, 2, 3, 4]
        [3, 2, 3, 4]
        [4, 5, 6, 7]
     ]

at each step we can choose to go right or down
max(solve(down), solve(right))
pass on a visited 
remove curr from visited at the end





"""
import collections
from typing import List, Set, Tuple


Matrix = List[List[int]]
Pair = collections.namedtuple('Pair', 'row col')
Cache = Set[Pair]


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def solve(self, matrix: Matrix) -> int:
		if not matrix or not matrix[0]:
			return -1
		visited: Cache = set()
		return self.get_max_path(matrix, Pair(0, 0), visited)

	def get_max_path(self, matrix: Matrix, position: Pair, 
					 visited: Cache) -> int:
		if position in visited:
			return 0
		visited.add(position)
		down: Pair = Pair(position.row + 1, position.col)
		right: Pair = Pair(position.row, position.col + 1)
		max_path: int = 0
		if self.is_valid(position, down, matrix):
			max_path = self.get_max_path(matrix, down, visited)
		if self.is_valid(position, right, matrix):
			max_path = max(max_path, self.get_max_path(matrix, right, visited))
		visited.discard(position)
		return max_path+1
		
	def is_valid(self, position: Pair, other: Pair, matrix: Matrix) -> bool:
		if self.out_bounds(position, matrix) or self.out_bounds(other, matrix):
			return False
		return matrix[position.row][position.col] < matrix[other.row][other.col]

	def out_bounds(self, position: Pair, matrix: Matrix) -> bool:
		return (position.col < 0 or position.row < 0 or 
				position.col > len(matrix[0]) or 
				position.row > len(matrix))
		
