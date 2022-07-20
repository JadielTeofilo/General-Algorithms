"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
        _
_      | |  _
 |  _  | |_| |
 |_| |_|     |
0 1 2 3 4 5 6

2,0,1,0,2,1,2]


_
 _ _
  _  


2 1

In - bars: List[int]


map elemets on bigger equals equivalents 

have a pointer on left and right

start from the smaller one
    go until finding bigger equal
    keep track of blocks_to_remove
    update result when you find target block

stop when start == end

O(n) time complexity where n is the size of the inpt
O(1) space complexity


"""
from typing import List, Iterator, Callable


class Solution:
    def trap(self, height: List[int]) -> int:
        return find_trapped_area(height) + find_trapped_area(height, reverse=True)


def find_trapped_area(heights: List[int], reverse: bool = False) -> int:
    start: int = 0 if not reverse else len(heights) - 1
    minus_blocks: int = 0
    result: int = 0
    iteration: Iterator[int] = (range(1, len(heights)) 
                                if not reverse 
                                else range(len(heights) -2, -1, -1))
    comparison: Callable = (lambda x, y: x > y) if reverse else (lambda x, y: x >= y)
    for index in iteration:
        if comparison(heights[index], heights[start]):
            result += (abs(index - start) - 1) * heights[start] - minus_blocks
            minus_blocks = 0
            start = index
            continue
        minus_blocks += heights[index]
    return result


