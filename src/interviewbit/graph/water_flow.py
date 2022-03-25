"""
Given an N x M matrix A of non-negative integers representing the height of each unit cell in a continent, the "Blue lake" touches the left and top edges of the matrix and the "Red lake" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the number of cells from where water can flow to both the Blue and Red lake.

 Blue Lake ~   ~   ~   ~   ~ 
        ~  1   2   2   3  (5) *
        ~  3   2   3  (4) (4) *
        ~  2   4  (5)  3   1  *
        ~ (6) (7)  1   4   5  *
        ~ (5)  1   1   2   4  *
           *   *   *   *   * Red Lake

 Water can flow to both lakes from the cells denoted in parentheses.



The goal is to find nodes that have edges that reach both sides
brute force is to do bfs from every node and check if it reaches both the sides

better to keep the information, so have another matrix a dp matrix that has info on weather a given node can reach blue and red

set the first row and col with blue
set last row and col with red
dp[row][col].blue = (dp[row - 1][col].blue if smaller) or (dp[row][col - 1].blue if smaller)
same for red but [row + 1][col] [row][col + 1] (has to be build from last to first row)


iterate on the dp matrixand count the nums of times blue and red are set


O(n*m) time complexity where row= n col=m
O(n*m) space

"""
import dataclasses
from typing import List, Tuple

Matrix = List[List[int]]


@dataclasses.dataclass
class Reach:
    blue: bool = False
    red: bool = False


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, matrix: Matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        dp: List[List[Reach]] = [[Reach() for _ in range(cols)] for _ in range(rows)]
        self.fill_reds(dp, matrix)
        self.fill_blues(dp, matrix)
        return self.count_blues_with_reds(dp)

    def fill_reds(self, dp: List[List[Reach]], matrix: Matrix) -> None:
        for row in range(len(matrix)):
            dp[row][-1].red = True
        for col in range(len(matrix[0])):
            dp[-1][col].red = True
        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[0]) - 1, -1, -1):
                if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
                    continue
                dp[row][col].red = self.get_reach(dp, row, col, 'red', matrix)

    def fill_blues(self, dp: List[List[Reach]], matrix: Matrix) -> None:
        for row in range(len(matrix)):
            dp[row][0].blue = True
        for col in range(len(matrix[0])):
            dp[0][col].blue = True
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    continue
                dp[row][col].blue = self.get_reach(dp, row, col, 'blue', matrix, -1)
 
    def get_reach(self, dp: List[List[Reach]], row: int, 
                  col: int, color: str, matrix: Matrix, sign: int = 1) -> bool:
        spots: List[Tuple[int, int]] = [
            (row + 1 * sign, col),
            (row, col + 1 * sign),
        ]
        for new_row, new_col in spots:
            
            if (not self.is_valid(matrix, new_row, new_col) or
                matrix[new_row][new_col] > matrix[row][col]):
                continue
            if getattr(dp[new_row][new_col], color):
                return True
        return False
        
    def count_blues_with_reds(self, dp: List[List[Reach]]) -> int:
        counter: int = 0
        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if dp[row][col].red and dp[row][col].blue:
                    counter += 1
        return counter

    def is_valid(self, matrix: Matrix, row: int, col: int) -> bool:
        if row >= len(matrix) or row < 0 or col >= len(matrix[0]) or col < 0:
            return False
        return True
