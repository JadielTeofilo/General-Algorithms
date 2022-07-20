"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


1 2 3 4
1 2 4 3



4 2 1 3
4 2 3 1


4 1 3 2 0
4 1 3 2 0


stop on index 1
we go backwards trying to find an element on index i that nums[i - 1] is smaller
if nothing found, reverse the list and stop
now we go backards again to find the element immediatelly bigger 

O(n) time complexity
O(1) space complexity

"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        4 1 3 2 0
        
        """
        # Finds first decreasing position (backwards)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        else:
            # Stops in case it's already the biggest permutation
            # (there is no decreasing position)
            nums.reverse()
            return
        #  Finds the immediatelly bigger element and swap it
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > nums[i - 1]:
                nums[j], nums[i - 1] = nums[i - 1], nums[j]
                break
        reverse_partial(nums, i, len(nums) - 1)


def reverse_partial(nums: List[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


