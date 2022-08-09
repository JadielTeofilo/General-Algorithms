"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


-1 3 -2 4 -2

-1 -2 -2 3 4


sort input
iterate on the input
    skip if equal


Use two sum


"""
from typing import List, Iterator


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            # Breaks because all numbers infront are positive
            if num > 0:
                break
            for triplet in twosum(
                nums, start=index + 1, end=len(nums) - 1, target=num
            ):
                result.append(triplet)
        return result


def twosum(nums: List[int], start: int, end: int, 
           target: int) -> Iterator[List[int]]:
    while start < end:
        if nums[start] + nums[end] == -target:
            yield [target, nums[start], nums[end]]
            start += 1
            end -= 1
        elif nums[start] + nums[end] > -target:
            end -= 1
        else:
            start += 1
        while start > 0 and nums[start] == nums[start - 1]:
            start += 1


