"""
Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

-2 _ 2

  -2  1 -2 3 -2
0 -2 -1 -3 0 -2


BIT

insert 0


Build running sum
iterate on running sum
    subract start and end from curr
    add to answer the followeing query(end) - query(start - 1)
    update BIT

with BIT (for num of elements smaller) one needs to normalize the input
    one way is to deduplicate, sort the values and build a equivalency hash from num to index
    another is to just have the deduplicate sorted list and search the index on the go with bin search
    another way is to not normalize at all, it will work if not negative. Downside is space complexity


O(n log n) time complexity where n is the size of the input numbers
O(n) space n=len(numbers)

"""
from typing import List, Dict

class BIT:

    def __init__(self, size: int) -> None:
        self.tree: List[int] = [0] * (size + 1)

    def update(self, index: int, value: int) -> None:
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        result: int = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        running_sums: List[int] = self.build_running_sums(nums)
        sums_sorted: List[int] = sorted(set(running_sums))
        rank: Dict[int, int] = {v: i for i, v in enumerate(sums_sorted)}
        tree: BIT = BIT(len(sums_sorted))
        result: int = 0
        for running_sum in running_sums:
            new_start: int = upper - running_sum
            new_end: int = lower - running_sum
            result += (tree.query(self.bisect_right(sums_sorted, new_end)) - 
                       tree.query(self.bisect_left(sums_sorted, new_start)))
            tree.update(rank[running_sum] + 1, 1)
        return result

    def bisect_left(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            mid: int = (start + end) // 2
            if nums[mid] < target: 
                start = mid + 1
            else:
                end = mid
        return start

    def bisect_right(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            mid: int = (start + end) // 2
            if nums[mid] > target: 
                end = mid - 1
            else:
                start = mid
        return start

    def build_running_sums(self, nums: List[int]) -> List[int]:
        running_sums: List[int] = [0] * (len(nums) + 1)
        for index, num in enumerate(nums):
            running_sums[index + 1] = running_sums[index] + num
        return running_sums




