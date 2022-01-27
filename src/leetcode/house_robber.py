"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


In - houses: List[int]
Out - int

2    3   1  2  2 9 3 0
14  14  11  11 9 9 3 0

dp[i] = max(dp[i]+dp[i+2], dp[i + 1])

find a subsequence that has no adjencent elements

O(n) time and space complexity where n is the size of the input
possible to do O(1) space by only keeping last three elements

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # Adds one more dummy element at the end
        dp: List[int] = [0] * (len(nums) + 1)
        # Fills the original last element
        dp[-2] = nums[-1]
        for i in range(len(nums) - 2, - 1, - 1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]

        
