"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

0 1 1 1
1 0 1 1
1 0 1 1


The idea is to try each element as the bottom right element. The biggest matrix that it can make (size of the side) is also the number of *square* submatrices with this element as the bottom right most

dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

O(ROW*COL) time complexity
O(1) space complexity cuz we can use the matrix it self as our dp matrix


"""
from typing import List


Matrix = List[List[int]]


class Solution:
    def countSquares(self, matrix: Matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        result: int = 0 
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    continue
                if col > 0 and row > 0:
                    matrix[row][col] += (min(
                        matrix[row-1][col-1], matrix[row][col-1], matrix[row-1][col]
                    ))
                result += matrix[row][col]
        return result


