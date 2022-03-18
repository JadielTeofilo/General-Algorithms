"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.


1 0 0 1
0 1 0 0
1 1 0 0
1 1 1 0 

0 1 2 3
  _ 

while stack and bar < stack[-1].number
    max_area updated to (i - stack[-1].index) * stack[-1].number
    update curr index to the popped index
    pop
insert in the stack


add zero at the end of input

build cache matrix with num of ones uppwards


1 0 0 1
0 1 0 0
1 2 0 0 
2 3 1 0

O(n*m) time complexity where n = rows m = cols
O(n*m) space complexity where n = rows m = cols 

"""
import collections
from typing import List


Matrix = List[List[str]]
Cache = List[List[int]]
StackData = collections.namedtuple('StackData', 'index number')


class Solution:
    def maximalRectangle(self, matrix: Matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        cache: Cache = self.build_cache(matrix)
        max_area: int = 0
        for row in cache:
            max_area = max(max_area, self.get_max_area(row + [0]))
        return max_area

    def build_cache(self, matrix: Matrix) -> Cache:
        cache: Cache = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or matrix[row][col] == '0':
                    cache[row][col] = int(matrix[row][col])
                    continue
                cache[row][col] = 1 + cache[row - 1][col]
        return cache

    def get_max_area(self, numbers: List[int]) -> int:
        max_area: int = 0
        stack: List[StackData] = []
        for i, number in enumerate(numbers):
            new_index: int = i
            while stack and number < stack[-1].number:
                max_area = max(
                    max_area, 
                    (i - stack[-1].index) * stack[-1].number
                )
                new_index = stack[-1].index
                stack.pop()
            stack.append(StackData(new_index, number))
        return max_area


