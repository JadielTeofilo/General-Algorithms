"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


we are looking for the closest bigger temperature in the right

10 50 20 10 10 20 

1  0  0  2  1  0


initialize output as list of 0s

have a stack
iterate on the input, adding the index to the stack
    we pop from the stack while we have a smaller element on it
        update the result of those indices



O(n) time complexity
O(1) space complexity

"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: List[int] = [0] * len(temperatures)
        stack: List[int] = []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                popped_index: int = stack.pop()
                result[popped_index] = index - popped_index
            stack.append(index)
        return result


