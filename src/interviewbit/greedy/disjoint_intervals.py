"""
Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.

Return a integer denoting the length of maximal set of mutually disjoint intervals.


In - pairs: List[List[int]]
Out - int



1,3 - 1 relation
2,5 - 3 relations
3,4 - 1 
4,7 - 1


1,7 4,7 8,9

sort the intervals
if two intervals intersect keep the one with the smaller end
if they have the same end use the latest

O(nlogn) time where n is the size of numbers
O(n) space complexity

"""
from typing import List

START = 0
END = 1

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, intervals: List[List[int]]) -> int:
        # Can I change the input?
        intervals.sort()
        disjoint: List[List[int]] = intervals[0:1]
        for index, interval in enumerate(intervals):
            if index == 0:
                continue
            last: List[int] = disjoint[-1]
            if last[END] >= interval[START]:
                self.update_disjoint(disjoint, interval)
            else:
                disjoint.append(interval)
        return len(disjoint)

    def update_disjoint(self, disjoint: List[List[int]], 
                        interval: List[int]) -> None:
        # Returns when the last had smaller end
        if disjoint[-1][END] <= interval[END]:
            return
        # Replaces interval
        disjoint.pop(-1)
        disjoint.append(interval)



