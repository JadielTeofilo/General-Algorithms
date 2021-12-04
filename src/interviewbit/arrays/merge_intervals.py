"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
1,2 - 3,10 - 11,19 - 12,16

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.


When you say non overlaping do you mean that the end will never be a start of other intervakl
yup


Find afected intervals (index of them)
    Use binary search to do so
        First look for the interval that covers start, and then end
If it is not inside anything, find its position
If is all inside one interval, just return
___ ____  ___ ___     _
  ___  _ __ __    __ ___
start is inside one interval, end is in another
start is outside, end is inside
start is inside and end is outside

In - intervals: List[Interval], new: Interval
Out - List[Interavals]



"""
from typing import List


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals: Interval, 
               new_interval: Interval) -> List[Interval]:
        self.insert_interval(
            intervals, new_interval
        )   
        return self.merge_intervals(intervals)

    def insert_interval(self, intervals: List[Interval], 
                         new_interval: Interval) -> None:
        for i in range(len(intervals)):
            if intervals[i].start > new_interval.start:
                intervals.insert(i, new_interval)
                return 
        intervals.append(new_interval)

    def merge_intervals(self, intervals: List[Interval]) -> List[Interval]:
        result: List[int] = []
        i: int = 0
        j: int = 1
        deleted: Set[int] = set()
        while j < len(intervals):
            # Case they ovelap
            if intervals[i].end >= intervals[j].start:
                intervals[i].end = max(intervals[i].end, intervals[j].end)
                deleted.add(j)
                j += 1
                continue
            i = j
            j += 1
        for i, interval in enumerate(intervals):
            if i in deleted:
                continue
            result.append(interval)
        return result
