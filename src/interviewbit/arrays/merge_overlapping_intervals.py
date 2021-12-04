"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

"""
from typing import List

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        return self.merge_intervals(intervals)

    def merge_intervals(
        self, intervals: List[Interval]
    ) -> List[Interval]:
        if len(intervals) < 2:
            return intervals
        result: List[Interval] = intervals[:1]
        for interval in intervals[1:]:
            if result[-1].end >= interval.start:
                self.merge_interval(result, interval)
                continue
            result.append(interval)
        return result

    def merge_interval(self, intervals: List[Interval], 
                       new_interval: Interval) -> None:
        """ Merges the last interval of intervals with new_inteval"""
        intervals[-1].end = max(intervals[-1].end, new_interval.end)


