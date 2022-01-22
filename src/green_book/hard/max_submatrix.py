"""
Max Submatrix: Given an NxN matrix of positive and negative integers, write code to find the
submatrix with the largest possible sum.


There are N^2 diff sizes of matrix, the brute force way is to go through them. O(N^4) time complexity
for each of them we go through the matrix and make the sums


1 -2 2 5
-2 1 2 1
2 -5 3 -2
3 -3 3 1

(row, col)

 1,1 -1,-1  1,1  6,6
-2,-1 -1,-2 1

row_sum = left.row_sum + curr
sub_matrix_sum = left.row_sum + curr + top.sub_matrix_sum


build dp matrix
go through matrix, find the sum for every possible size of matrix from that position

keep the max sum of submatrix
return sum

In - matix: List[List[int]]
Out - int


"""
import collections
import logging
import math
from typing import List, Union, Iterable


Position = collections.namedtuple('Position', 'row col')
Matrix = List[List[int]]
Sum = collections.namedtuple('Sum', 'row matrix')


def max_submatrix(matrix: Matrix) -> int:
    # TODO check input
    logging.basicConfig(level=logging.DEBUG)
    dp: Matrix = build_accumulated_sum(matrix)
    max_sum: Union[int, float] = -math.inf
    logging.debug(dp)
    for position in find_matrix_positions(matrix):
        for rows in range(len(matrix)):
            for cols in range(len(matrix[0])):
                max_sum = max(find_matrix_sum(dp, rows, cols, position), 
                              max_sum)
    return int(max_sum)


def find_matrix_positions(matrix: Matrix) -> Iterable[Position]:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            yield Position(row, col)


def build_accumulated_sum(matrix: Matrix) -> Matrix:
    dp: List[List[Sum]] = [[Sum(None, None)] * len(matrix) for _ in 
                           range(len(matrix[0]))]  # Builds empty matrix
    for position in find_matrix_positions(matrix):
        dp[position.row][position.col] = find_sum_for_dp(
            matrix, dp, position
        )
    # Extract only the submatrix sums from Sum
    accumulated_sum: Matrix = [[0] * len(matrix) for _ in 
                               range(len(matrix[0]))]
    for row, col in find_matrix_positions(matrix):
        accumulated_sum[row][col] = dp[row][col].matrix
    return accumulated_sum


def find_sum_for_dp(matrix: Matrix, dp: List[List[Sum]], 
                    position: Position) -> Sum:
    # Finds the row sum
    current: int = matrix[position.row][position.col]
    left_row_sum: int = (dp[position.row][position.col - 1].row 
                 if position.col > 0 else 0)
    row_sum: int = current + left_row_sum
    # Finds the submatrix sum
    top_matrix_sum: int = (dp[position.row - 1][position.col].matrix
                           if position.row > 0 else 0)
    matrix_sum: int = top_matrix_sum + row_sum
    return Sum(row_sum, matrix_sum)


def find_matrix_sum(cache: Matrix, rows: int, cols: int, 
                    first_position: Position) -> int:
    """
    Finds the sum of elements on a submatrix of
    the cache matrix from first_position
    """
    last_of_first_row: Position = Position(first_position.row, 
                                           first_position.col + cols)
    last_of_first_col: Position = Position(first_position.row + rows,
                                           first_position.col)
    last_of_submatrix: Position = Position(first_position.row + rows,
                                           first_position.col + cols)
    if is_outside(last_of_submatrix, cache):
        return 0
    upper_quadrant: int = (cache[last_of_first_row.row-1][last_of_first_row.col] 
                           if last_of_first_row.row > 0 else 0)
    left_quadrant: int = (cache[last_of_first_col.row][last_of_first_col.col-1]
                          if last_of_first_col.col > 0 else 0)
    upper_left_quadrant: int = (cache[first_position.row-1][first_position.col-1]
                                if first_position.row > 0 and first_position.col > 0
                                else 0)
    submatrix_quadrant: int = cache[last_of_submatrix.row][last_of_submatrix.col]
    return (submatrix_quadrant - 
            (upper_quadrant + left_quadrant - upper_left_quadrant))


def is_outside(position: Position, matrix: Matrix) -> bool:
    return (position.row < 0 or position.col < 0 
            or position.row >= len(matrix) 
            or position.col >= len(matrix[0]))


print(max_submatrix(
[
[1, -2, 2, 5],
[-2, 1, 2, 1],
[2, -5, 3, -2],
[3, -3, 3, 1],
]
))
