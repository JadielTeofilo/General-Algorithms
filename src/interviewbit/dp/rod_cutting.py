"""
There is a rod of length N lying on x-axis with its left end at x = 0 and right end at x = N. Now, there are M weak points on this rod denoted by positive integer values(all less than N) A1, A2, …, AM. You have to cut rod at all these weak points. You can perform these cuts in any order. After a cut, rod gets divided into two smaller sub-rods. Cost of making a cut is the length of the sub-rod in which you are making a cut.

Your aim is to minimise this cost. Return an array denoting the sequence in which you will make cuts. If two different sequences of cuts give same cost, return the lexicographically smallest.


1 | 2 | 3 4 5 | 6

1 2 5

Brute force

try cutting on every position from start to end and call the recursion on it
    we sort the cuts so we know which cuts can be done 

stop when start > end return 0

iterate on cut positions, and call solve on the new start, end
left_max = solve(start=cut + 1, end=end, curr_cuts=curr_cuts + [cut])
right_max = solve(start=start, end=cut - 1, curr_cuts=curr_cuts + [cut])
min_cost = min(min_cost, left_max + right_max)

memoize the start, end position

O(m^3) time complexity where m is the size of cuts
O(m^2) space complexity 


In - cuts: List[int], size: int
Out - int

"""
import math
from typing import List, Dict, Iterable, Tuple, Union


Cache = Dict[Tuple[int, int], int]


class Solution:
    def minCost(self, size: int, cuts: List[int]) -> int:
        cuts.sort()
        return self.find_min_cost(cuts, size, start=0, 
                                  end=size, cache={})

    def find_min_cost(self, cuts: List[int], size: int, start: int, 
                      end: int, cache: Cache) -> int:
        # n = 7, cuts = [1,3,4,5]
        """
        0 1 2 3 4 5 6 7

        7 + solve(0, 1) -> 0
            solve(1, 7) 
                6 + solve(1,3) -> 0
                    solve(3,7)
                        4 + solve(3,4) -> 0
                            solve(4,7)
        """
        if start >= end:  # 0 7 
            return 0
        if (start, end) in cache:
            return cache[(start, end)]
        min_cost: Union[int, float] = math.inf
        for cut in self.get_possible_cuts(start, end, cuts):
            left_min: int = self.find_min_cost(
                cuts, size, start=start, end=cut, cache=cache
            )
            right_min: int = self.find_min_cost(
                cuts, size, start=cut, end=end, cache=cache
            )
            min_cost = min(min_cost, end - start + left_min + right_min)
        # Handles the case with no cuts
        if min_cost == math.inf:
            min_cost = 0
        cache[(start, end)] = min_cost
        return min_cost

    def get_possible_cuts(self, start: int, end: int, 
                          cuts: List[int]) -> Iterable[int]:
        for cut in cuts:
            if cut <= start:
                continue
            if cut >= end:
                break
            yield cut
