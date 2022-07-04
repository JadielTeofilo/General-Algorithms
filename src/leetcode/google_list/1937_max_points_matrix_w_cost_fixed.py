"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.


we can think of a bottom up dp from the top where dp[i][j] tells us the max value we get from picking that point
we can use the input matrix to save space

dp[i][j] = max(points[i-1][k] - abs(j - k) for k in range(len(points[0])))

make prev be the first row
iterate on the rows from the second row
generate preffix and suffix max from the prev row
iterate on the columns on the curr row
update the row with the max between the prefix and suffix array




"""
from typing import List


def build_prefix(numbers: List[int]) -> List[int]:
    prefix: List[int] = [0] * len(numbers)
    for i, number in enumerate(numbers):
        if i == 0:
            prefix[i] = numbers[i]
            continue
        prefix[i] = max(prefix[i - 1] - 1, numbers[i])
    return prefix


def build_suffix(numbers: List[int]) -> List[int]:
    suffix: List[int] = [0] * len(numbers)
    suffix[-1] = numbers[-1]
    for i in range(len(numbers) - 2, -1, -1):
        suffix[i] = max(suffix[i + 1] - 1, numbers[i])
    return suffix


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        prev: List[int] = points[0]
        for row in range(1, len(points)):
            preffix: List[int] = build_prefix(prev)
            suffix: List[int] = build_suffix(prev)
            for col in range(len(prev)):
                prev[col] = max(suffix[col], preffix[col]) + points[row][col]

        return max(prev)
            

