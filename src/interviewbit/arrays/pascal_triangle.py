"""
Problem Description
Given an index k, return the kth row of the Pascal's triangle.

Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3
                    1
                1       1
            1       2       1
        1       3       3       1


Return : [1,3,3,1]

Note: k is 0 based. k = 0, corresponds to the row [1].

Note: Could you optimize your algorithm to use only O(k) extra space?


have a last and a curr as lists 
generate curr based on last
    use a get_value(last) to ignore out of bounds
stop iteration when len(curr) == k + 1
return curr

O(k^2) time complexity 
O(k) space complexity where k is the inputed number

"""
from typing import List


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, k: int) -> List[int]:
        last: List[int] = [1]
        curr: List[int] = [1]
        while len(curr) < k + 1:
            curr = self.generate_current(last)
            last = curr
        return curr

    def generate_current(self, last: List[int]) -> List[int]:
        result: List[int] = []
        for i in range(len(last) + 1):
            result.append(
                self.get_value(last, i) + self.get_value(last, i - 1)
            )
        return result

    def get_value(self, numbers: List[int], index: int) -> int:
        if index >= len(numbers) or index < 0:
            return 0 
        return numbers[index]


    
