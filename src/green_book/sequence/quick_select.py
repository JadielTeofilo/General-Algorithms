from typing import List


def quick_select(nums: List[int], k: int) -> int:
    """ Finds the k th largest element """
    return quick_select_helper(nums, target_elements_on_the_left=len(nums) - k)


def  quick_select_helper(nums: List[int], target_elements_on_the_left: int) -> int:
    if not nums:
        return -1
    mid:  int = (len(nums) - 1) // 2
    smaller_elements: List[int] = [num for i, num in enumerate(nums) 
                                            if num <= nums[mid] and i != mid]
    bigger_elements: List[int] = [num for num in nums if num > nums[mid]]
    if len(smaller_elements) == target_elements_on_the_left:
        return nums[mid]
    if len(smaller_elements) > target_elements_on_the_left:
        return quick_select_helper(smaller_elements, target_elements_on_the_left)
    else:
        target_elements_on_the_left -= len(smaller_elements) + 1
        return quick_select_helper(bigger_elements, target_elements_on_the_left)
