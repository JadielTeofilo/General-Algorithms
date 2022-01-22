##################### QuickSort ###################
from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    """ Does recursive sorting using quick sort """
    if len(nums) < 2:
        return nums
    mid: int = (len(nums) - 1)//2
    smaller_values: List[int] = [num for i, num in enumerate(nums) 
                                          if num <= nums[mid] and i != mid]
    bigger_values: List[int] = [num for num in nums
                                          if num > nums[mid]]
    return quick_sort(smaller_values) + [nums[mid]] + quick_sort(bigger_values)

