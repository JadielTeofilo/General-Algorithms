"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
     _
                   _
        _   
 _           
   __   
  _   _    _
________________________



two pointer approach

start, end = 0, len(n) - 1
while start < end

update max_size


O(n) time complexity where n is the size of the input
O(1) space complexity 


"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area: int = 0
        start, end = 0, len(height) - 1
        while start < end:
            max_area = max(max_area, 
                           get_area(height, start, end))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area


def get_area(height: List[int], start: int, end: int) -> int:
    return (end - start) * min(height[start], height[end])

