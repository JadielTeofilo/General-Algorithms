"""
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

Cant use dp as the square matrix cuz it does not have the same property

1 0 0 1 1 
1 1 1 0 0 
1 1 0 0 1
1 1 1 0 1

0 0 



Pattern matrix compression:
    iterate on the possible row combinations
    for a given start row initialize a cache that tells for a given col, starting from start row, if there are zeros yet
    with the cache up to that point run the algo that finds the number of subarrays with all ones


1 1 1 0 1 0 1 1


O(Cols * rows * rows) Time complexity
O(cols) space complexity

In - Matrix

"""
from typing import List


Matrix = List[List[int]]


class Solution:
    def numSubmat(self, mat: Matrix) -> int:
        result: int = 0
        if not mat or not mat[0]:
            return result
        for start_row in range(len(mat)):
            cache: List[int] = [1] * len(mat[0])
            for end_row in range(start_row, len(mat)):
                for col in range(len(mat[0])):
                    cache[col] &= mat[end_row][col]
                result += self.find_subarrays_with_ones(cache)
        return result

    def find_subarrays_with_ones(self, array: List[int]) -> int:
        result: int = 0
        ones_count: int = 0
        for num in array:
            if num == 1:
                ones_count += 1
            else:
                ones_count = 0
            result += ones_count
        return result




