"""
Given a sorted array A consisting of duplicate elements.

 Your task is to remove all the duplicates and return a sorted array of distinct elements consisting of all distinct elements present in A.

But, instead of returning an answer array, you have to rearrange the given array in-place such that it resembles what has been described above.
Hence, return a single integer, the index(1-based) till which the answer array would reside in the given array A.

Note: This integer is the same as the number of integers remaining inside A had we removed all the duplicates.
Look at the example explanations for better understanding.

      _
123623668
    -

O(n) time complexity
O(1) space

"""
from typing import List, Optional


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, numbers: List[int]) -> int:
        left: int = 0
        last: Optional[int] = None
        for right in range(len(numbers)):
            if numbers[right] == last:
                continue
            numbers[left] = numbers[right]
            last = numbers[right]
            left += 1
        
        return left 

