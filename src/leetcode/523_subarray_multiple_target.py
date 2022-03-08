"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


 [23,2,6,4,7], k = 6
0 5  1 1 5 0 

The goal is to find the num that (x + y + z) % target == 0
ever growing bars does the trick


keep a running sum
keep a cache dict of the running sum that tells the smallest index that a given value was found
initialize it with zero


O(n) time complexity
O(n) space where n is the size of nums
"""
from typing import List, Dict


class Solution:
    def checkSubarraySum(self, nums: List[int], target: int) -> bool:
        cache: Dict[int, int] = {0: -1}
        running_sum: int = 0

        for index, num in enumerate(nums):
            running_sum = (running_sum + num) % target
            if running_sum in cache:
                if cache[running_sum] < index - 1:
                    return True
            else:
                cache[running_sum] = index
        return False

