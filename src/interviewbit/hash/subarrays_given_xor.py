"""
Problem Description

Given an array of integers A and an integer B.

Find the total number of subarrays having bitwise XOR of all elements equals to B.



Problem Constraints

1 <= length of the array <= 105

1 <= A[i], B <= 109



Input Format

The first argument given is the integer array A.

The second argument given is integer B.


Output Format

Return the total number of subarrays having bitwise XOR equals to B.

In - numbers: List[int]
Out - int


A = [4, 2, 2, 6, 4]
B = 6




running xor

100 010 010 110 100
100 110 100 010 110

4,2
2,2,6
6

cache  dict int int 
add 0 to cache as -1
keep result as the sum of working values
iterate on numbers 
keep a running xor
each number make the xor, store on cache
O(n) time and space, n the size of numbers
"""
import collections
from typing import Dict, List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, numbers: List[int], target: int) -> int:
        cache: Dict[int, int] = collections.defaultdict(int)
        cache[0] += 1
        result: int = 0
        running_xor: int = 0
        for number in numbers:
            running_xor ^= number
            cache[running_xor] += 1
            if running_xor ^ target in cache:
                result += cache[running_xor ^ target]
        return result




