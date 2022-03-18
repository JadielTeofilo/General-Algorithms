"""
Maximize the Topmost Element After K Moves

You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

    If the pile is not empty, remove the topmost element of the pile.
    If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.

You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.



3 2 1 9 2 3

1

if 1 it will always be the second element

3

we can get n + 1 or we can get anyone from 1 to n - 1

the main point is to know that what matters are the different options that you can have, not how you are getting to it

max(max(nums[:n-1]), nums[n])


O(n) time complepxity where n is the size of the input
O(1) space
"""
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 1:
            return nums[1] if len(nums) > 1 else - 1
        if k == 0 or not nums:
            return nums[0] if nums else - 1
        if len(nums) == 1:
            return nums[0] if k % 2 == 0 else -1
        max_num: int = nums[k] if len(nums) > k else -1
        for index, num in enumerate(nums):
            if index == k - 1:
                break
            max_num = max(max_num, num)
        return max_num
