"""
Given an array A with non negative numbers, divide the array into two parts such that the average of both the parts is equal.

Return both parts (If exist). If there is no solution. return an empty list.

NOTE:
If a solution exists, you should return a list of exactly 2 lists of integers A and B which follow the following condition :
numElements in A <= numElements in B
If numElements in A = numElements in B, then A is lexicographically smaller than B ( https://en.wikipedia.org/wiki/Lexicographical_order )

If multiple solutions exist, return the solution where length(A) is minimum. If there is still a tie, return the one where A is lexicographically smallest.

Array will contain only non negative numbers.



2 6 7 3 2

We want to find a subset that the avg of remaining elements is same as curr avg
keep the full sum of the elements sum
subtract the elements on the current subset from the sum and divide by the remaining num of elements to get the avg of the other side

we want to build all subsets testing for the one with desired elements

numbers: List[int], start: int, curr_nums: List[int], curr_sum: int, curr_len: int, full_sum: int, cache: Cache




"""
import collections
from typing import List, Tuple, Set, Dict


Cache = Set[Tuple[int, int, int]]


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, numbers: List[int]) -> List[List[int]]:
        left_nums: List[int] = self._find_matching_avg(
            numbers, start=0, curr_nums=[], curr_sum=0, curr_len=0,
            full_sum=sum(numbers), cache=set()
        )
        counter: Dict[int, int] = collections.Counter(left_nums)
        right_nums: List[int] = self._find_right_nums(numbers, counter)
        return sorted([sorted(right_nums), sorted(left_nums)])

    def _find_right_nums(self, numbers: List[int], 
                         counter: Dict[int, int]) -> List[int]:
        right_nums: List[int] = []
        for num in numbers:
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                continue
            right_nums.append(num)
        return right_nums

    def _find_matching_avg(self, numbers: List[int], start: int, 
                           curr_nums: List[int], curr_sum: int, curr_len: int, 
                           full_sum: int, cache: Cache) -> List[int]:
        if start >= len(numbers):
            return (curr_nums 
                    if self.is_valid(curr_sum, curr_len, full_sum, len(numbers))
                    else [])
        if (start, curr_sum, curr_len) in cache:
            return []
        for i in range(start, len(numbers)):
            target_nums: List[int] = self._find_matching_avg(
                numbers, i + 1, curr_nums + [numbers[i]], 
                curr_sum + numbers[i], curr_len + 1, full_sum, cache
            )
            if target_nums:
                cache.add((start, curr_sum, curr_len))
                return target_nums
        return []

    def is_valid(self, curr_sum: int, curr_len: int, 
                 full_sum: int, full_len: int) -> bool:
        if curr_len == 0 or full_len == curr_len:
            return False
        return ((curr_sum / curr_len) == 
                (full_sum - curr_sum) / (full_len - curr_len))

