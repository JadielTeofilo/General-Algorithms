"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

00:00, 23:59

sort the input, for each pair test the min distance:

either the subtraction between the two (subract hour, add the minutes of the bigger, sub the min of smaller)

or the subtraction between the bigger and 24:00 + the smaller (hour * 60 + minutes)

04:20 10:24

06:04


O(HlogH) time complexity
O(1) space complexity

"""
from typing import collections


Time = collections.namedtuple('Time', 'hour minute')
MIDNIGHT = Time('24', '00')


class Solution:
    def findMinDifference(self, timepoints: List[str]) -> int:
        timepoints.sort()
        return min(
            self.find_helper(timepoints), 
            self.find_helper([timepoints[0], timepoints[-1]]) if len(timepoints) > 2 else sys.maxsize
        )

    def find_helper(self, timepoints: List[str]) -> int:
        result: int = sys.maxsize
        for i in range(len(timepoints) - 1):
            smaller: Time = Time(*timepoints[i].split(':'))
            bigger: Time = Time(*timepoints[i + 1].split(':'))
            curr_diff: int = min(
                get_distance(bigger, smaller),
                get_distance(MIDNIGHT, bigger) + to_minutes(smaller),
            )
            result = min(curr_diff, result)        
        return result

def get_distance(first: Time, second: Time) -> int:
    hours_diff: int = (int(first.hour) - int(second.hour)) * 60
    total_diff: int = hours_diff + int(first.minute) - int(second.minute)
    return total_diff

def to_minutes(target: Time) -> int:
    return int(target.hour) * 60 + int(target.minute)



