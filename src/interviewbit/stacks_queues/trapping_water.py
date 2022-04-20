"""
Given an integer array A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


We keep a left and right pointers and move the smaller, while you move you add to the final area the last_max - curr. With the two pointer we know that there is going to be a bigger bar on the other side

keep a left_max and right_max

move the pointer that has the smallest curr value
at each move, add the left/right_max - curr to the answer

stop when they both reach the same point


O(n) time complexity where n is the num of bars
O(1) space 

In - bars: List[int]
Out - int
"""
from typing import List


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, bars: List[int]) -> int:
        left, right = 0, len(bars) - 1
        left_max, right_max = 0, 0
        result: int = 0
        if not bars:
            return 0
        """
        1 0 3 2 0 5 0
              -   -

        """
        while left < right:
            if bars[left] < bars[right]:
                left_max = max(left_max, bars[left])
                result += left_max - bars[left]
                left += 1
            else:
                right_max = max(right_max, bars[right])
                result += right_max - bars[right]
                right -= 1
        return result
        

