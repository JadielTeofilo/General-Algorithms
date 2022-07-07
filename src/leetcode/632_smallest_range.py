"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



1 3 5 6

9 10 11

20 21


for the start of the interval, 


6, 20

maybe binary search the interval

try starting from the min(alist[i][0])
end = max(alist[i][-1])

for every one of them you bisect the start to find if a given list works has a number bigger than it
if not try another number (bisect right)

Do the same for the end value with bisect left but making sure it is bigger than the start


5 8
4 9


start = 1
end = 21

start = 1
end = 10

start = 

O(k*log(n)*log(k)) time complexity
O(1) space complexity

"""
import bisect
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        start = find_start(nums) - 1
        end = find_end(nums, start)
        return [start, end]


def find_start(nums: List[List[int]]) -> int:
    start: int = min([num[0] for num in nums])
    end: int = max([num[-1] for num in nums])
    while start < end:
        mid: int = (start + end) // 2
        if not is_valid_start(nums, mid):
            end = mid
        else:
            start = mid + 1
    return start

def is_valid_start(nums: List[List[int]], mid: int) -> bool:
    for num in nums:
        if bisect.bisect_left(num, mid) >= len(num):
            return False
    return True


def find_end(nums: List[List[int]], start: int) -> int:
    start: int = min([num[0] for num in nums])
    end: int = max([num[-1] for num in nums])
    while start < end:
        mid: int = (start + end) // 2
        if not is_valid_end(nums, mid, start): 
            start = mid + 1
        else:
            end = mid
    return start


def is_valid_end(nums: List[List[int]], mid: int, start: int) -> bool:
    if mid < start:
        return False
    for num in nums:
        if bisect.bisect_right(num, mid) == 0:
            return False
    return True


