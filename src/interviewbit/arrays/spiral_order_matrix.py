"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.


Input Format:

The first and the only argument contains an integer, A.

Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.



In - size: int
Out - Matrix


size = 4


1  2  3  4 
13 14 15 6
12 17 16 7 
11 10 9  8 

we iterate on the formed matrix filling the values
row layer -> col size-layer -> row size-layer (reversed) -> col layer (reversed)
starts values are same as the layer
end values is at size-layer








"""
from typing import List


Matrix = List[List[int]]


class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, size: int) -> Matrix:
		matrix: Matrix = [[0] * size for _ in range(size)]
		last: int = size - 1
		count: int = 0
		for layer in range(size):
			for is_reversed in [False, True]:
				count = self.fill_row(  #TODO
					matrix, start=Position(layer, layer),
					end=Position(layer, last - layer), 
					count=layer, is_reversed=is_reversed
				)
				count = self.fill_col(
					matrix, start=Position(layer, last - layer),
					end=Position(last - layer, last - layer),
					count=layer, is_reversed=is_reversed
				)
		return matrix



