"""
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

    During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
    During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
    It may be the case that for some index i, there are no legal jumps.

A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.




we have higher and lower jumps
you start on a higher jump and must follow with lower jump and keep inverting
We can use DP bottom up
we start backwards


Reach:
    with_higher: bool
    with_lower: bool

dp: List[Reach]

2 1 5 1 4
T T T T T
T T T F T

We need a way to find the smallest bigger element on the right
same for biggest smaller element

we can do that by sorting the elements keeping the index, then use a monotonic stack to map the closest indices
To get the lower we have to sort the negative numbers so the indices of duplicates dont get swapped
2 1 5 1 4
0 1 2 3 4

1 1 2 4 5
1 3 0 4 2


O(nlogn) time complexity n = len(nums)
O(n) space

In - nums: List[int]
Out - int

"""
import dataclasses
from typing import List, Dict, Optional, Tuple, Iterable


@dataclasses.dataclass
class Reach:
    with_higher: bool
    with_lower: bool


class Solution:
    def oddEvenJumps(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Finds the sorted list of (num, index)
        sorted_nums: List[Tuple[int, int]] = sorted(
            [(num, i) for i, num in enumerate(nums)]
        )
        higher: List[Optional[int]] = self.map_nums(sorted_nums)
        sorted_nums: List[Tuple[int, int]] = sorted(
            [(-num, i) for i, num in enumerate(nums)]
        )
        lower: List[Optional[int]] = self.map_nums(sorted_nums)
        dp: List[Reach] = [Reach(False, False) for _ in range(len(nums))]
        dp[-1] = Reach(True, True)
        counter: int = 0
        for index in range(len(nums) - 2, -1, -1):
            if higher[index] is not None:
                dp[index].with_higher = dp[higher[index]].with_lower
            if lower[index] is not None:
                dp[index].with_lower = dp[lower[index]].with_higher
            # Adds one if with higher is set (could be inited here)
            counter += int(dp[index].with_higher)
        return counter + 1

    def map_nums(self, sorted_nums: List[Tuple[int, int]]) -> List[Optional[int]]:
        mapped: List[Optional[int]] = [None] * len(sorted_nums)
        stack: List[int] = []
        for _, num_index in sorted_nums:
            while stack and stack[-1] < num_index:
                stack_index: int = stack.pop()
                mapped[stack_index] = num_index
            stack.append(num_index)
        return mapped

        


