"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

    x for x >= 0.
    -x for x < 0.


1 2 3
4 1 2
3 1 1

O(c^2*r) time complexity

If we can cache the result for a given row, given a column
    _
4 1 1 3
-
0 0 0 3
0 3 3 3


O(c*r) time
O(c*r) space


build a cache[row][col] that tells us if an element on the previous row was chosen in this column, which would be the best number in this row to use


"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cache: List[List[int]] = build_cache(points)
        result: int = 0
        for fixed_col in range(len(points[0])):
            last_col: int = fixed_col
            curr_sum: int = points[0][fixed_col]
            for row in range(1, len(points)):
                curr_sum += points[row][cache[row][last_col]]
                last_col = cache[row][last_col]
            result = max(result, curr_sum)
        return result


def build_cache(points: List[List[int]]) -> List[List[int]]:
    cache: List[List[int]] = [[0] * len(points[0]) for _ in range(len(points))]
    for row in range(len(points)):
        curr_max: int = points[row][0]
        max_index: int = 0
        for col in range(1, len(points[0])):
            if points[row][col] > curr_max - 1:
                cache[row][col] = col
                max_index = col
                curr_max = points[row][col]
            else:
                cache[row][col] = max_index
                curr_max -= 1
        curr_max: int = points[row][-1]
        max_index: int = len(points[0]) - 1
        for col in range(len(points[0] - 2, -1, -1)):
            if points[row][col] > curr_max - 1:
                cache[row][col] = col if points[row][cache[row][col]] < points[row][col] else cache[row][col]
                max_index = col
                curr_max = points[row][col]
            else:
                cache[row][col] = max_index if points[row][cache[row][col]] < points[row][max_index] else cache[row][col]
                curr_max -= 1
    return cache
