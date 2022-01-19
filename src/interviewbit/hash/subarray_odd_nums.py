"""
Problem Description
Given an array of integers A and an integer B.
Find the total number of subarrays having exactly B odd numbers.

  2 1 8 7 3 3 2 1 2 8
0 0 1 1 2 3 4 4 5 5 5

brute force is to start from every position and stop when finding B odds, add one to result
    after that, keep going, until a new even is found
    while you go, keep adding to result



1 2 1

Problem Constraints
1 <= length of the array <= 105
1 <= A[i] <= 109
0 <= B <= A

Input Format
The first argument given is the integer array A.
The second argument given is integer B.


Output Format
Return the total number of subarrays having exactly B odd numbers.

In - numbers: List[int]
Out - int


"""
import collections
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, numbers: List[int], target: int) -> int:
        cache: Dict[int, int] = collections.defaultdict(int)
        cache[0] += 1
        odds_count: int = 0
        result: int = 0
        for number in numbers:
            odds_count += 1 if number % 2 != 0 else 0
            if odds_count - target in cache:
                result += 1
            cache[odds_count] += 1
        return result


