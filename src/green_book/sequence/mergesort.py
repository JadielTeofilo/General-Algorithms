######################## Merge Sort ########################
""" Main point to remember is the recursion call merge(divide_and_conquer(nums, start, mid), divide_and_conquer(nums, mid+1, end)) """
from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if not nums:
        return nums
    return divide_and_conquer(nums, start=0, end=len(nums) - 1)


def divide_and_conquer(nums: List[int], start: int, end: int) -> List[int]:
    if start == end:
        return [nums[start]]
    else:
        mid: int = (start+end)//2
        return merge(divide_and_conquer(nums, start, mid), 
                           divide_and_conquer(nums, mid+1, end))


def merge(nums_a: List[int], nums_b: List[int]) -> List[int]:
    index_a: int = 0
    index_b: int = 0
    result: List[int] = []
    while index_a < len(nums_a) and index_b < len(nums_b):
        if nums_a[index_a] < nums_b[index_b]:
            result.append(nums_a[index_a])
            index_a += 1
        else:
            result.append(nums_b[index_b])
            index_b += 1
    if index_a < len(nums_a):
        result.extend(nums_a[index_a:])
    if index_b < len(nums_b):
        result.extend(nums_b[index_b:])
    return result


def iter_merge_sort(nums: List[int]) -> List[int]: 
    nums = [[num] for num in nums]
    while len(nums) > 1:
        nums = do_list_merge(nums)
    return nums[0]


def do_list_merge(nums: List[List[int]]) -> List[List[int]]: 
    result: List[List[int]] = []
    for i in range(0, len(nums) - 1, 2):
        result.append(merge(nums[i], nums[i+1]))
    if len(nums) % 2 == 1:
        result.append(nums[-1])
    return result

