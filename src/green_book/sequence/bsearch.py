############ Binary Search ###############
""" Important to notice the usage of (start + end)//2 to find mid point """
from typing import List


def binary_search(nums: List[int], target: int) -> bool:
    if not nums:
        return False
    start: int = 0
    end: int = len(nums) - 1
    while start <= end:
        mid: int = (start + end)//2
        if target == nums[mid]:
            return True
        if target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


def bin_recursive(nums: List[int], target: int) -> bool:
    return bin_recursive_helper(nums, start=0, end=len(nums), target=target)


def bin_recursive_helper(nums: List[int], start: int, end: int, target: int) -> bool:
    if start > end:
        return False
    mid: int = (start + end)//2
    if target == nums[mid]: 
        return True
    elif target < nums[mid]:
        return bin_recursive_helper(nums, start, mid - 1, target)
    else:
        return bin_recursive_helper(nums, mid + 1,end, target)
