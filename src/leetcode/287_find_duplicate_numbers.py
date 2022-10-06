"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



1,3,4,2,2

we can binary search to find the answer

we pick a number from 1 to n (lets say x)

we see how many elements smaller then it there is (and equal)
if equals > 1 we return it
if there are x - 1 elements we try a bigger number


O(nlogn) time complexity where n is the size of the input
O(1) space complexity

"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start: int = 1
        end: int = len(nums)
        while start < end:
            pivot: int = (start + end) // 2
            equal: int = 0
            smaller: int = 0
            for num in nums:
                equal += int(num == pivot)
                smaller += int(num < pivot)
            if equal > 1:
                return pivot
            if smaller >= pivot:
                end = pivot
            else:
                start = pivot + 1
        

