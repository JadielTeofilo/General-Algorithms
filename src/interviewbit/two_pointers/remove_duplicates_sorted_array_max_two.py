"""
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,

Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].



    _
1111235566N
  -
11235566

-

3 >= 2
move `left` two to the right

keep count



 
O(n) time where n is the size of input
O(1) space

"""
from typing import List, Optional


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, numbers: List[Optional[int]]) -> int:
        left: int = 0
        last: Optional[int] = None
        prev: Optional[int] = None
        #       _
        # 0 0 1 1 1 2 2 3
        #     -
        for i, number in enumerate(numbers):
            if number == last and number == prev:
                continue
            numbers[left] = number
            prev = last  # 0
            last = number  # 0
            left += 1
        return left
            
