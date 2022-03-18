"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].


Merge sort keeping swaps
merge_sort()
    merge(divice_n_conquer(s, m), divide_n_conquer(m + 1, end))
List[Dict[int, int]]
dict with position of each number
Dict[int, List[int]]
build result


O(n log n) time
O(n log n) space

"""
import collections
import dataclasses
from typing import List, Tuple, Dict


@dataclasses.dataclass
class Count:
    number: int
    right_smallers: int
    original_index: int


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts: List[Count] = self.merge_sort(nums)
        result: List[int] = [0] * len(nums)
        for count in counts:
            result[count.original_index] = count.right_smallers
        return result

    def merge_sort(self, nums: List[int]) -> List[Count]:
        counts: List[Count] = [Count(num, 0, i) for i, num in enumerate(nums)]
        return self.divide_n_conquer(counts, 0, len(counts) - 1)

    def divide_n_conquer(self, nums: List[Count], start: int, 
                         end: int) -> List[Count]:
        if start == end:
            return [nums[start]]
        pivot: int = (start + end) // 2
        return self.merge(self.divide_n_conquer(nums, start, pivot),
                          self.divide_n_conquer(nums, pivot + 1, end))

    def merge(self, first: List[Count], second: List[Count]) -> List[Count]:
        if not first or not second:
            return first or second
        inserted_from_second: int = 0
        index_sec: int = 0
        result: List[Count] = []
        for count in first:
            while index_sec < len(second) and count.number > second[index_sec].number:
                result.append(second[index_sec])
                index_sec += 1
                inserted_from_second += 1
            count.right_smallers += inserted_from_second
            result.append(count)
        if index_sec < len(second):
            result.extend(second[index_sec:])
        return result


