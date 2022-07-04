"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1



manhatan distance


1 0 0
0 1 0
1 1 1

1 0 0
0 1 0
1 2 1


build two dp matrices one dp[row][col] = 1 + max(dp[row+1][col], dp[row][col + 1])
and one for row - 1 col, row col -1

iterate on the matrices getting the smallest value between the two



O(m*n) time complexity where m=rows, n=cols
O(1) space cuz the output does not count as space complexity



################

BFS approach 

0 1 0
0 0 1
1 1 1

Start from all zeros, add new elements to queue when they are 1 and have a smaller distance then what is recorded


"""
from typing import List


Matrix = List[List[int]]
INF = 10001


class Solution:
    def updateMatrix(self, mat: Matrix) -> List[List[int]]:
        dp: Matrix = [[INF] * len(mat[0]) for _ in range(len(mat))]
        get_bellow_dp(mat, dp)
        get_above_dp(mat, dp)
        return dp


def get_bellow_dp(mat: Matrix, bellow: Matrix) -> None:
    for row in range(len(mat) - 1, -1, -1):
        for col in range(len(mat[0]) -1, -1, -1):
            if mat[row][col] == 0:
                bellow[row][col] = 0
                continue
            bellow[row][col] = min(1 + get_bellow(bellow, row, col), bellow[row][col])


def get_bellow(mat: Matrix, row: int, col: int) -> int:
    down: int = mat[row + 1][col] if row + 1 < len(mat) else INF
    right: int = mat[row][col + 1] if col + 1 < len(mat[0]) else INF
    return min(down, right)


def get_above_dp(mat: Matrix, above: Matrix) -> None:
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                above[row][col] = 0
                continue
            above[row][col] = min(1 + get_above(above, row, col), above[row][col])


def get_above(mat: Matrix, row: int, col: int) -> int:
    up: int = mat[row - 1][col] if row - 1 >= 0 else INF
    left: int = mat[row][col - 1] if col -1 >= 0 else INF
    return min(up, left)

