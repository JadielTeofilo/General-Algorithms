"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

keep track of starting points and end points

sort them separatly 

iterate two pointers keeping track of know many rooms we need at a given time


2 10, 3 5, 8 12, 14 15
      _
2 3 8 14
   _
5 10 12 15

iterate on the starts
    increase end index (and -1 to answer) while smaller equal to start
    add one to answer


O(nlogn) time complexity where n is the size of the input
O(n) space complexity

"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts: List[int] = sorted([interval[0] for interval in intervals])
        ends: List[int] = sorted([interval[1] for interval in intervals])
        end_index: int = 0
        result: int = 0
        curr_rooms: int = 0
        for start in starts:
            while end_index < len(ends) and ends[end_index] <= start:
                end_index += 1
                curr_rooms -= 1
            curr_rooms += 1
            result = max(result, curr_rooms)
        return result
