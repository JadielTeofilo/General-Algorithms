"""
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

    The first n elements belonging to the first part and their sum is sumfirst.
    The next n elements belonging to the second part and their sum is sumsecond.

The difference in sums of the two parts is denoted as sumfirst - sumsecond.

    For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
    Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.

Return the minimum difference possible between the sums of the two parts after the removal of n elements.

Answer:

Its easier to see it as find a subsequence of size len//3 * 2 that the first half minus the second half is minimal
when the problem asks to minimize the difference of the sum, we must get the min possible first half and the max possible second half

since we're talking subsequences, the way to do it is to have a pprefix and suffix array with the sums (of n//3 max and min elements). Then iterate on the possible midpoints of the subsequence just look at the cache arrays

1 8 7 1 2 8 
   |
prefix - non inclusive (has to be minimized):
    keep a maxheap (start with nums[:n])
    iterate on nums from n to the len()-n + 1  # +1 cuz its non inclusive
    add to curr sum
    add to heap and remove the biggest element
    remove biggest from curr sum

suffix - inclusive (has to be maximized)
    keep minHeap

7,9,5,8,1,3

O(nlogn) time complexity
O(n) space

"""
import collections
import heapq
import sys
from typing import List


HeapValue = collections.namedtuple('HeapValue', 'index value')


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        prefix: List[int] = self.build_prefix(nums)
        suffix: List[int] = self.build_suffix(nums) 
        min_diff: int = sys.maxsize
        group_size: int = len(nums)//3
        # Iterates on the possible mid points
        for i in range(group_size, len(nums) - group_size + 1): 
            min_diff = min(min_diff, prefix[i] - suffix[i])
        return min_diff

    def build_prefix(self, nums: List[int]) -> List[int]:
        prefix: List[int] = [0] * len(nums)
        group_size: int = len(nums)//3
        max_heap: List[HeapValue] = [HeapValue(-n, n) 
                                     for n in nums[:group_size]]
        heapq.heapify(max_heap)
        prefix[group_size] = sum(nums[:group_size])
        for i in range(group_size + 1, len(nums) - group_size + 1):
            heapq.heappush(max_heap, HeapValue(-nums[i-1], nums[i-1]))
            prefix[i] = (prefix[i-1] - heapq.heappop(max_heap).value +
                         nums[i-1])
        return prefix

    def build_suffix(self, nums: List[int]) -> List[int]:
        suffix: List[int] = [0] * len(nums)
        group_size: int = len(nums)//3
        min_heap: List[int] = nums[-group_size:]
        heapq.heapify(min_heap)
        suffix[-group_size]: int = sum(min_heap)
        for i in range(len(nums) - group_size - 1, group_size - 1, -1):
            heapq.heappush(min_heap, nums[i])
            suffix[i] = suffix[i+1] - heapq.heappop(min_heap) + nums[i]
        return suffix


