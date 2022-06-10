"""
You are given an m x n binary matrix grid.

In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.


0 0 0
1 1 1
0 0 0


if we go from the all zeros and experiment with what we can generate we can see that all the rows have to be the same pattern:
    row[i] == ~ row[j] or row[i] == row[j]

just go through the rows, if does not fit the pattern, return false

O(n*m) time where n =rows, m=cols
O(1) space
"""
from typing import List


def invert(bits: List[int]) -> List[int]:
    bits = bits.copy()
    for i, bit in enumerate(bits):
        bits[i] = bit ^ 1
    return bits


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return False
        patterns: List[List[int]] = [
            grid[0],
            invert(grid[0]),
        ]
        for row in range(len(grid)):
            if grid[row] not in patterns:
                return False
        return True

