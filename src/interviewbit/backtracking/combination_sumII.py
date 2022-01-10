"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

    Note:

        All numbers (including target) will be positive integers.
        Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
        The solution set must not contain duplicate combinations.

Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

In - numbers: List[int], target: int
Out - List[List[int]]


Recursion

solve(numbers, start_index, target, answer)

"""
from typing import List

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, numbers: List[int], 
                       target: int) -> List[List[int]]:
        result: List[List[int]] = []
        numbers.sort()
        self.find_combinations(numbers, 0, target, result, [])
        return result

    def find_combinations(self, numbers: List[int], start_index: int, 
                          target: int, result: List[List[int]], 
                          curr: List[int]) -> None:
        if target < 0 or start_index > len(numbers):
            return
        if target == 0:
            curr.sort()
            result.append(curr)
        for index in range(start_index, len(numbers)):
            if (index > start_index and 
                numbers[index] == numbers[index - 1]):
                continue
            self.find_combinations(numbers, index + 1, 
                                  target - numbers[index], result,
                                  curr + [numbers[index]])




