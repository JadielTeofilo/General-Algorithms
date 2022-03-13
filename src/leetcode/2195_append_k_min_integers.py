"""
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.



The main point here is that k can be bigger then the array it self and O(n + k) is not an option
the idea is to find the first element that allows for k elements to be on its left

remove duplicates
sort input
for every element
check its value minus index: num - i
    if bigger than k get the sum minus the elements behind

if not possible, the answer is the sum from 1 to len(nums) + k - the sum(nums)


O(n log n) time complexity
O(n) space

"""
from typing import List, Optional


class Solution:
    def minimalKSum(self, nums: List[int], target: int) -> int:
        nums = sorted(list(set(nums)))
        result: int = 0
        min_index: Optional[int] = self.find_min_index(nums, target)
        if min_index is None:
            min_index = len(nums)
        target_nums: List[int] = nums[:min_index]
        return (((len(target_nums) + target) * (1 + len(target_nums) + target))//2 - 
                sum(target_nums))

    def find_min_index(self, nums: List[int], target:int) -> Optional[int]:
        for i, num in enumerate(nums):
            if num - i > target:
                return i

