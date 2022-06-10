"""
There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.



In - paint: List[Tuple[int, int]]
Out - List[int]


paint
3-4, 1-2, 5-9, 2-7

1    1    4    2

brute force is to just iterate on the intervals keeping track of the visited spots
just mind that the end is not inclusive

better approach

1 - - - 4  6 7

  1 2

2 5

keep the intervals sorted
when inserting, bisect right -1 on the start to find which interval the start matches
update the end of this interval
merge the intervals from that point



O(nlogn) time complexity cuz the merge is limited to n throughout the execution
O(n) space complexity

"""
import sortedcontainers
from typing import List, Tuple


START = 0
END = 1


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        merged_intervals: List[List[int]] = sortedcontainers.SortedList()
        result: List[int] = []
        for start, end in paint:
            if not merged_intervals:
                merged_intervals.add([start, end])
                result.append(end - start)
                continue
            target: int = merged_intervals.bisect_left([start, end])
            merged_intervals.add([start, end])
            result.append(self.merge(merged_intervals, max(0, target)))
        return result

    def merge(self, intervals: List[List[int]], target: int) -> int:
        """
        1-7 2-3 5-8
        [[1,5],[2,4]]
        1-5
        """
        free_spots: int = intervals[target][END] - intervals[target][START]
        start = sys.maxsize
        size = 0
        for i in range(target + 1, len(intervals)):
            if intervals[i][START] < intervals[target][END]:
                free_spots -= (min(intervals[i][END],
                                   intervals[target][END]) - intervals[i][START])
                intervals[target][END] = max(intervals[i][END],
                                             intervals[target][END])
                start = min(i, start)
                size += 1
                continue
            break
        if (target - 1 >= 0 and
             intervals[target - 1][END] > intervals[target][START]):
            free_spots -= (min(intervals[target - 1][END],
                   intervals[target][END]) - intervals[target][START])
            intervals[target - 1][END] = max(intervals[target][END],
                                             intervals[target-1][END])
            start = min(target, start)
            size += 1
        while size > 0:
            intervals.pop(start)
            size -= 1
        return free_spots



############### Other approach #############
"""
Keep a dict with all the intermediate steps

It allows us to see that a given start has been seen before, and back then it had that given end, make start = old_end and go from there to see if there is any new value to use.

1-7 2-3 5-8

1:7 2:7 3:7 4:7 5:7 6:7

while start < end
    if start in sequence: 
        start = sequence[start]
    else:
        sequence[start] = end
        work += 1
        start += 1


"""
