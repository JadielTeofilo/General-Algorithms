"""
Given an array A of positive integers,call a (contiguous,not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly B.

(For example: [1, 2, 3, 1, 2] has 3 different integers 1, 2 and 3)

Return the number of good subarrays of A.


2
1 2 1 3 1 2


have two pointers, move the second until the condition is not meet
    while that, keep adding end - start + 1 to answer, adding so, the num of subarrays with at most k diff nums
if not meet, move the start until its meet
    

answer will be at_most(k) - at_most(k-1)
handle case of 0, return 0

In - numbers: List[int], size: int
Out - int


O(n) time complexity where n is the size of numbers
O(1) space where s is size

"""
import collections
from typing import Dict, List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, numbers: List[int], size: int) -> int:
        return (self.get_at_most(numbers, size) - 
                self.get_at_most(numbers, size - 1))

    def get_at_most(self, numbers: List[int], size: int) -> int:
        if size <= 0:
            return 0
        counter: Dict[int, int] = collections.defaultdict(int)
        start: int = 0
        result: int = 0
        for end in range(len(numbers)):
            counter[numbers[end]] += 1
            while len(counter) > size:
                counter[numbers[start]] -= 1
                if counter[numbers[start]] == 0:
                    counter.pop(numbers[start])
                start += 1
            result += end - start + 1
        return result
