"""
Given a N * 2 array A where (A[i][0], A[i][1]) represents the ith pair.

In every pair, the first number is always smaller than the second number.

A pair (c, d) can follow another pair (a, b) if b < c , similarly in this way a chain of pairs can be formed.

Find the length of the longest chain subsequence which can be formed from a given set of pairs.



[5, 24]
[39, 60]
[15, 28]
[27, 40]
[50, 90]


pairs, start, constraint

use backtracking to build the valid subsequences
stop when start >= len(pairs)
[], 0, 0
iterate from start to len(pairs)
getting the max from recursion




"""
import math
from typing import List, Tuple, Dict
import sys


sys.setrecursionlimit(5000)
Cache = Dict[Tuple[int, int], int]

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, pairs: List[List[int]]) -> int:
        cache: Cache = dict()
        return self._solve_helper(pairs, start=0, 
                                  constraint=0, cache=cache)

    def _solve_helper(self, pairs: List[List[int]], start: int, 
                      constraint: int, cache: Cache) -> int:
        if start >= len(pairs):
            return 0
        if (start, constraint) in cache:
            return cache[(start, constraint)]
        max_size: int = 0
        for i in range(start, len(pairs)):
            if pairs[i][0] > constraint:
                max_size = max(
                    max_size, 
                    1 + self._solve_helper(pairs, i + 1, 
                                           pairs[i][1], cache)
                )
        cache[(start, constraint)] = max_size
        return cache[(start, constraint)]

