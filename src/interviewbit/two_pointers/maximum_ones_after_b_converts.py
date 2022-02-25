"""
Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.

2
        -
001110110
012345678
     _

=7
 
we want to find the max subarray with at most size zeros

two pointer

move end until its invalid
    calculate max end - start
move start until its valid


O(n) time where n is the size of numbers
O(1) space

In - numbers: List[int], size: int
Out - int

"""
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, numbers: List[int], size: int) -> int:
        if size < 0:
            raise ValueError('Incorrect size, must be positive')
        start: int = 0
        zeros: int = 0
        max_size: int = 0
        for index, bit in enumerate(numbers):
            if bit == 0:
                zeros += 1
            max_size = max(max_size, index - start)
            while zeros > size:
                if numbers[start] == 0:
                    zeros -= 1
                start += 1
        # Handles the edge case where iteration ends with zeros <= size
        index += 1
        max_size = max(max_size, index - start)
        return max_size


