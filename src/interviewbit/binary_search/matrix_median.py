"""
Given a matrix of integers A of size N x M in which each row is sorted.
Find an return the overall median of the matrix A.
Note: No extra memory is allowed.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.

Input Format
The first and only argument given is the integer matrix A.
Output Format
Return the overall median of the matrix A.

Constraints
1 <= N, M <= 10^5
1 <= N*M  <= 10^6
1 <= A[i] <= 10^9
N*M is odd

For Example

Input 1:
    A = [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]
Output 1:
    5
Explanation 1:
    A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
    Median is 5. So, we return 5.


start = min(first_col) = 1
end = max(last_col)

O(log(max-min)*rows*log(cols)) time complexity
O(1) space complexity

In - matrix: Matrix
Out - int

The duplicates makes it that we have to use the bisect idea to find the closest element on the right that would work.

"""
from typing import List, Optional


Matrix = List[List[int]]


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, matrix: Matrix) -> int:
        if not matrix or not matrix[0]:
            return -1
        start, end = self.get_min(matrix), self.get_max(matrix)
        matrix_size: int = len(matrix) * len(matrix[0])
        while start < end:
            mid: int = (start + end) // 2
            position: int = self.find_position(mid, matrix)
            if position < (matrix_size + 1) // 2:
                start = mid + 1
            else:
                end = mid
        return start

    def find_position(self, target: int, matrix: Matrix) -> int:
        result: int = 0
        for row in matrix:
            result += self.bisect_right(row, target)
        return result

    def bisect_right(self, numbers: List[int], target: int) -> int:
        start, end = 0, len(numbers)
        while start < end:
            mid = (start + end) // 2
            if numbers[mid] > target:
                end = mid
            else:
                start = mid + 1
        return start

    def get_max(self, matrix: Matrix) -> int:
        max_number: int = 0
        for row in matrix:
            max_number = max(max_number, row[-1])
        return max_number

    def get_min(self, matrix: Matrix) -> int:
        min_number: Optional[int] = None
        for row in matrix:
            if not min_number: 
                min_number = row[0]
            min_number = min(min_number, row[0])
        return min_number or 0
            

