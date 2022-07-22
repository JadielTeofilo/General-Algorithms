"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.




1 1 0 1 0
1 0 1 1 1 
1 0 1 1 0
1 1 0 1 0


Dp approach
consider each element as the last right element on the matrix
dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1


maybe we can use the input matrix as the dp matrix, check if possible to change it
otherwise we can just keep the last two rows of the dp matrix

In - matrix: Matrix
Out - size: int

"""
import collections
import sys
from typing import List, Any, Iterator


Matrix = List[List[Any]]
Position = collections.namedtuple('Position', 'row col')


class Solution:
    def maximalSquare(self, matrix: Matrix) -> int:
        result: int = 0
        for row, col in get_positions(matrix):
            if row == 0 or col == 0:
                matrix[row][col] = int(matrix[row][col])
            elif matrix[row][col] == '0':
                matrix[row][col] = 0
            else:
                matrix[row][col] = min(
                    matrix[row-1][col-1],
                    matrix[row][col-1],
                    matrix[row-1][col],
                ) + 1
            result = max(matrix[row][col], result)
        return result * result


def get_positions(matrix: Matrix) -> Iterator[Position]:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            yield Position(row, col)


