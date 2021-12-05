"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5

Return 0 if the array contains less than 2 elements.

    You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
    You may also assume that the difference will not overflow.


5 1 8  9  10 12  2
5 6 14 23 33 45 47

1 2 5 8 9 10 12

get max and min elements
iterate from min to max
skip elements outside of set(numbers)
keep track of max distance


O(m) time cmplxt where m is the range of numbers
O(n) space where n is the size of numbers

In - numbers: List[int]
Out - int


"""
from typing import List, Set


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, numbers: List[int]) -> int:
        if len(numbers) < 2:
            return 0
        min_number: int = min(numbers)
        max_number: int = max(numbers)
        numbers_hash: Set[int] = set(numbers)
        max_gap: int = 0
        last: int = min_number
        for number in range(min_number + 1, max_number + 1):
            if number not in numbers_hash:
                continue
            max_gap = max(max_gap, number - last)
            last = number
        return max_gap
            
