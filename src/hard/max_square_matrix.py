"""
Max Square Matrix: Imagine you have a square matrix, where each cell (pixel) is either black or
white. Design an algorithm to find the maximum subsquare such that all four borders are filled with
black pixels.

In - matrix: List[List[int]]
Out - List[List[int]]


Do we care about the diagonal? 
nope

0 1 0 0 0 0 0 0
1 0 0 0 0 1 1 0
1 1 1 1 1 0 0 1
1 0 0 0 0 1 0 1
1 0 0 0 0 1 1 1
1 0 0 0 1 0 0 1
1 1 1 1 0 0 0 1 
0 0 0 0 0 0 0 1


Have a DP matrix that keeps track of information about previous pixels
    case its a one, None
    case its a zero, look left and up
        case left or up are zeros with no closing bounderies set it as no closing bounderies
        case bottom or right are the end, set as no closing
        set your local matrix position according to top and left
Find all target squares, iterate on the matrix to find the biggest square

O(n*m) time and space complexity where n is the rows, and m the columns

TODO THIS IS A WRONG IMPLEMENTATION, MUST BE REDONE, THE INTERIOR OF THE SUBMATRIX DOES NOT HAVE TO BE ZEROS.


"""
import collections
from typing import List

Position = collections.namedtuple('Position', 'row col')
Cache = collections.namedtuple('Cache', 'value is_unbound position')


def max_square_matrix(matrix: List[List[int]]) -> List[List[int]]:
    # TODO validate input
    dp: List[List[Cache]] = mark_squares(matrix)
    return find_max_square(dp)


def mark_squares(matrix: List[List[int]]) -> List[List[Cache]]:
    rows: int = len(matrix)
    columns: int = len(matrix[0])
    dp: List[List[Cache]] = [[Cache(None, None, None)] * columns for _ in range(rows)]
    for row in range(rows):
        for col in range(columns):
            curr: int = matrix[row][col]
            cache: Cache = Cache(None, None, None)
            if curr == 1:
                cache = Cache(1, None, None)
            elif (is_at_border(matrix, row, col) or
                  surrounded_by_unbound(dp, row, col)):
                cache = Cache(0, True, None)
            else:
                cache = Cache(
                    0, False, find_submatrix_position(dp, row, col) 
                )
            dp[row][col] = cache
    return dp


def is_at_border(matrix: List[List[int]], row: int, col: int) -> bool:
    return row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])


def surrounded_by_unbound(dp: List[List[Cache]], row: int, col) -> bool:
    """
        Checks if top or left elements are unbound
    """
    return dp[row - 1][col].is_unbound or dp[row][col - 1].is_unbound


def find_submatrix_position(dp: List[List[Cache]], row: int, col: int) -> Position:
    """ 
        Receives the coodinates of a matrix position that is 
        not at the border or surrounded by unbound and finds 
        its sub matrix position according 
        to left and top places
    """
    up: Position = Position(row - 1, col)
    up_node: Cache = dp[up.row][up.col]
    sub_matrix_row: int = (up_node.position.row + 1 
                           if up_node.value != 1 else 0)
    left: Position = Position(row, col - 1)
    left_node: Cache = dp[left.row][left.col]
    sub_matrix_col: int = (left_node.position.col + 1
                           if left_node.value != 1 else 0)
    return Position(sub_matrix_row, sub_matrix_col)


def find_max_square(dp: List[List[Cache]]) -> List[List[int]]:
    max_size: int = 0
    matrix_end_position: Position = Position(None, None)
    for row in range(len(dp)):
        for col in range(len(dp[0])):
            # Case it is not the end of a square matrix
            if (dp[row][col].value == 1 or 
                dp[row][col].position.row != dp[row][col].position.col):
                continue
            if dp[row][col].position.row > max_size:
                matrix_end_position = dp[row][col].position
                max_size = dp[row][col].position.row
    return build_submatrix(dp, matrix_end_position, max_size)


def build_submatrix(dp: List[List[Cache]], 
                 end_position: Position, size: int) -> List[List[int]]:
    start_position: Position = Position(end_position.row - size, 
                                        end_position.col - size)
    matrix: List[List[int]] = [[0] * size for _ in range(size)]
    return matrix


print(max_square_matrix(
    [
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ]
    ))
