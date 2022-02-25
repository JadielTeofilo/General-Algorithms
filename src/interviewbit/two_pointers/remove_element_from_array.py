"""
Given an array and a value, remove all the instances of that value in the array. 

Also return the number of elements left in the array after the operation.

It does not matter what is left beyond the expected length.

    Example:

    If array A is [4, 1, 1, 2, 1, 3]

    and value elem is 1, 

    then new length is 3, and A is now [4, 2, 3]

Try to do it in less than linear additional space complexity.


          _
4 2 3 2 1 3
      1-


same idea of the previous two pointer problems
iterate until you find a valid element,
copy to the left index


O(n) time
O(1) space

In - numbers: int, target: int
Out - int

"""
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, numbers: List[int], target: int) -> int:
        """
              _        
        4 2 1 2 1 3
            -
        
        """
        start: int = 0 
        for number in numbers:
            if number == target:
                continue
            numbers[start] = number
            start += 1
        return start

