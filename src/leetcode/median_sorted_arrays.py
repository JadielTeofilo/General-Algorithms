"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Answer:

Median is the point where len(left) == len(right), so when we pick a pivot in the first list, we can guess what is the pivot on the second

  x | x x x
y y | 


1 3 | 

2 | 4 5



pick a pivot from 0 to N inclusive (we are treating the split as being on the left of pivot)
check 
    first_left > second_right
        move to the left
    first_right < second_left
        move to the right

    if odd, answer will be the max between lefts
    if even max between lefts / min between rights


"""
from typing import List
import sys


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full: int = len(nums1) + len(nums2)
        half: int = (len(nums1) + len(nums2)) // 2
        start: int = 0
        end: int = len(nums1)
        while start <= end:
            # x | x x 
            # y | y
            pivot1: int = (start + end) // 2
            pivot2: int = half - pivot1
            if pivot2 < 0:
                end = pivot1 - 1
                continue
            if pivot2 > len(nums2):
                start = pivot1 + 1
                continue
            if pivot1 - 1 >= 0 and pivot2 < len(nums2) and nums1[pivot1 - 1] > nums2[pivot2]:
                end = pivot1 - 1
            elif pivot2 - 1 >= 0 and pivot1 < len(nums1) and nums1[pivot1] < nums2[pivot2 - 1]:
                start = pivot1 + 1
            else:
                break
        if full % 2 == 0:
            return (
                (min(self.get_right(nums1, pivot1),
                    self.get_right(nums2, pivot2)) +
                 max(self.get_left(nums1, pivot1), 
                    self.get_left(nums2, pivot2))) / 2
            )
        return min(self.get_right(nums1, pivot1), 
                   self.get_right(nums2, pivot2))
    
    def get_left(self, nums: List[int], pivot: int) -> int:
        if pivot == 0:
            return -sys.maxsize
        return nums[pivot - 1]

    def get_right(self, nums: List[int], pivot: int) -> int:
        if pivot == len(nums):
            return sys.maxsize
        return nums[pivot]

