"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

3 closest
  _
1 3 5 6 8 9
    -
3 1
5 6 8 9

3 
5 6


bigger = bisect right to find the element imediatelly bigger then our target
keep two pointers, one at the bigger one smaller
keep getting from the one with the smallest distance
stop when k is zero or one of the two pointers is out of bounds

fill two results and join them after (one reversed)

O(k + logn) time complexity
O(k) space complexity

"""
import bisect
import collections
from typing import List, Dict, Deque


class Solution:
    def findClosestElements(self, nums: List[int], 
                            max_distance: int, target: int) -> List[int]:
        bigger: int = bisect.bisect_right(nums, target)
        start: int = bigger - 1
        closest: Deque[int] = collections.deque()
        for end in range(bigger, len(nums)):
            while (start >= 0 and 
                   target - nums[start] <= nums[end] - target and
                   max_distance > 0):
                closest.appendleft(nums[start])
                start -= 1
                max_distance -= 1
            if max_distance == 0:
                break
            closest.append(nums[end])
            max_distance -= 1
        while start >= 0 and max_distance > 0:
            closest.appendleft(nums[start])
            start -= 1
            max_distance -= 1
        return list(closest)




