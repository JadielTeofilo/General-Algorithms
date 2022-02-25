"""
Given an array A of N non-negative numbers and you are also given non-negative number B.

You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow


_
5 3 2 1 2 1 3 4 
  -
5

amount of subarrays that can be formed by a array of size n is (n(n-1))//2 = 1 + 2 + 3 ... + n

iterate with end pointer until sum is invalid
at each iteration add end - start + 1
while invalid we move the start subtracting values


In - numbers: List[int], target: int
Out - int


O(n) time where n is the size of numbers
O(1) space



"""
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, numbers: List[int], target: int) -> int:
        start: int = 0 
        subarrays: int = 0
        curr_sum: int = 0
        for index, number in enumerate(numbers):
            curr_sum += number  # 3
            while curr_sum >= target:
                curr_sum -= numbers[start]
                start += 1
            subarrays += index - start + 1

        return subarrays
            
            
        

