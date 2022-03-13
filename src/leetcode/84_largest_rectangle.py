"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


   23241
      _
    _  
   _ _  
       ______
______________

= 10

2 goes until 4
3 goes 3
4 goes to 4
2 goes util 4

0 3
3 2
2 1
1 0

while stack and curr is smaller pop from the stack updating the result
    (curr.index - stack[-1].index) * stack.number
    change curr index to the index of the popped so we keep track of how big to the left it could go
add to the stack (num, index) when empty, bigger or equal

Add zero to the end of the list to get the remaining elements on the stack


In - bars: List[int]
Out - int

O(n) time where n it the size of bars
O(n) space where n is the size of bars

"""
import collections
from typing import List


StackData = collections.namedtuple('StackData', 'index number')


class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
        bars.append(0)
        max_area = 0
        stack: List[StackData] = []
        for i, bar in enumerate(bars):
            new_index: int = i
            while stack and bar < stack[-1].number:
                max_area = max(
                    max_area,
                    (i - stack[-1].index) * stack[-1].number
                )
                new_index = stack[-1].index
                stack.pop()
            stack.append(StackData(new_index, bar))
        return max_area
