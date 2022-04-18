"""
Problem Description

There is given an integer array A of size N denoting the heights of N trees.

Lumberjack Ojas needs to chop down B metres of wood. It is an easy job for him since he has a nifty new woodcutting machine that can take down forests like wildfire. However, Ojas is only allowed to cut a single row of trees.

Ojas's machine works as follows: Ojas sets a height parameter H (in metres), and the machine raises a giant sawblade to that height and cuts off all tree parts higher than H (of course, trees not higher than H meters remain intact). Ojas then takes the parts that were cut off. For example, if the tree row contains trees with heights of 20, 15, 10, and 17 metres, and Ojas raises his sawblade to 15 metres, the remaining tree heights after cutting will be 15, 15, 10, and 15 metres, respectively, while Ojas will take 5 metres off the first tree and 2 metres off the fourth tree (7 metres of wood in total).

Ojas is ecologically minded, so he doesn't want to cut off more wood than necessary. That's why he wants to set his sawblade as high as possible. Help Ojas find the maximum integer height of the sawblade that still allows him to cut off at least B metres of wood.

NOTE:

The sum of all heights will exceed B, thus Ojas will always be able to obtain the required amount of wood.

Problem Constraints
1 <= N <= 106
1 <= A[i] <= 106
1 <= B <= 2106

[20, 15, 10, 17]

start = 0
end = max(nums)

O(n*log(m)) time complexity where n is the size of the input and m the max number on the input
O(1) space

"""
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, nums: List[int], target: int) -> int:
        start, end = 0, max(nums)
        max_value: int = 0
        while start < end:
            mid = (start + end) // 2
            if self.is_enough(nums, mid, target):
                max_value = max(max_value, mid)
                start = mid + 1
            else:
                end = mid
        return max_value

    def is_enough(self, nums: List[int], cut: int, 
                  target: int) -> bool:
        wood_taken: int = 0
        for num in nums:
            # Cuts the top of each tree
            wood_taken += max(0, num - cut)
        return wood_taken >= target

