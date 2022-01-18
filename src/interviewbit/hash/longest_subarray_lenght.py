"""
Problem Description
Given an integer array A of size N containing 0's and 1's only. 
You need to find the length of the longest subarray having count of 1’s one more than count of 0’s.

Problem Constraints
1 <= N <= 105

nput Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the longest length of the subarray.

Example Input
Input 1:
-1  0 1 1 0  0 1 1
 0 -1 0 1 0 -1 0 1

we can build a cache array keeping a running sum
we start the dict with a zero
cache: Dict[int, int]  # From the running sum to the min index
result: int  # Starts at 0
we add 1 when seeing 1 and we subtract 1 when seeing a 0

we look for previous values like the current in the cache
    if found we check for a 1 before and after the curr subarray
        update the result

Input 2:
1  0  0 1  0 1  0
1  0 -1 0 -1 0 -1
Example Output
Output 1:
 5
Output 2:
 1


xample Explanation
Explanation 1:
 Subarray of length 5, index 1 to 5 i.e 1, 1, 0, 0, 1. Count of 1 = 3, Count of 0 = 2.
Explanation 2:
 Subarray of length 1 will be only subarray that follow the above condition.

O(n) Time and space complexity where n is the size of the input

In - numbers: List[int]
Out - int

"""
import collections
from typing import List, Dict


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, numbers: List[int]) -> int:
        result: int = 0
        cache: Dict[int, int] = {}
        cache[0] = -1
        last: int = 0
        for index, number in enumerate(numbers):
            curr: int = last + (1 if number == 1 else -1)
            if curr not in cache:
                cache[curr] = index
            if curr - 1 in cache:
                result = max(
                    result, index - cache[curr - 1]
                )
            last = curr
        return result

