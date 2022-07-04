"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

    For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).


1 3

0 1 1 1



1 2 3 1


0 1 1 2 2 2 3

randint(0, sum(w) - 1)

1 2 3 1


have a prefix sum

1 3 6 7

randint(0, 6)  # 2



brute force - get the random integer and iterate on w subtracting by the curr, when negative, stop

with the prefix sum we can just bisect the increasing list to find the first element bigger the the target


O(n) time complexity where n is the size of w for the initialization
O(logn) time complexity for the pick index function
O(n) space complexity

"""
import bisect
import itertools
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        """
        1 2 3 1
        1 3 6 7
        """
        self.numbers: List[int] = w
        self.prefix_sum: List[int] = list(
            itertools.accumulate(self.numbers)
        )

    def pickIndex(self) -> int:
        random_index: int = random.randint(0, sum(self.numbers) - 1)
        return bisect.bisect_right(self.prefix_sum, random_index)       



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
