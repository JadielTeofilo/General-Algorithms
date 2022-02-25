"""
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,

Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].



         _
112355666N
        -
_

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
        moves: int = 0
        last: Optional[int] = None
        #     _
        # 111122334
        # -
        for number in numbers:
            if number == last:
                moves += 1
                continue
            skip: int = 1 if moves < 2 else 2
            left += skip
            numbers[left] = number
            numbers[left - 1] = last
            moves = 0
            last = number
        return left
            
