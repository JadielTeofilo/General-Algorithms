"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.


Just have the distance to midnight in minutes already

24 120 167

midnight is 24*60

we add on item to the list: the first as being the midnight - last + first w

we compare each pair and return the min

O(nlogn) time
O(n) space


"""
import sys
from typing import List


def to_minutes(time: str) -> int:
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute) 


class Solution:
    def findMinDifference(self, time_points: List[str]) -> int:
        minutes: List[int] = list(map(to_minutes, time_points))
        minutes.sort()
        if len(minutes) > 1:
            minutes.append(24*60 + minutes[0])
        result: int = sys.maxsize
        for i in range(len(minutes) - 1):
            result = min(result, minutes[i + 1] - minutes[i])
        return result
