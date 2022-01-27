"""
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:

    You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50

2^n
memoization on the capacity, start
O(n*c)

building diff subsets (valid ones)

                            60 100 120
            60                                          _
    100             _                       100                     _
                120     _

use a cache on start, capacity
we stop when capacity is zero or start is at the end of the list
iterate from start to len of values
    if capcity minus weight is smaller then zero we continue
    max_ = max(curr_value + solve(data, start, capaticy - curr_weight), max_)

"""
from typing import List, Dict, Tuple

Cache = Dict[Tuple[int, int], int]


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, values: List[int], weights: List[int], 
              capacity: int) -> int:
        cache: Cache = dict()
        start: int = 0
        return self.find_max(values, weights, start, capacity, cache)

    def find_max(self, values: List[int], weights: List[int], 
                 start: int, capacity: int, cache: Cache) -> int:
        if capacity == 0 or start >= len(values):
            return 0
        if (start, capacity) in cache:
            return cache[(start, capacity)]
        max_: int = 0
        for i in range(start, len(values)):
            if capacity - weights[i] < 0:
                continue
            max_ = max(
                values[i] + 
                self.find_max(
                    values, weights, i + 1, 
                    capacity - weights[i], cache
                ), 
                max_
            )
        cache[(start, capacity)] = max_
        return cache[(start, capacity)]

