"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

    Length of given string s will always equal to n - 1
    Your solution should run in linear time and space.


Have a max and min values from our target range (1 to n - 1)
we iterate backwards
if we see a D we get the min value, max value otherwise
At the end we just concatenate the last value
revert the result


O(n) time complexity where n is the input number

In - number: int, symbols: str
Out - List[int]


"""
import collections
from typing import List


Range = collections.namedtuple('Range', 'min max')


class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, number: int, symbols: str) -> List[int]:
        if not symbols or number == 0:
            return []
        if len(symbols) != number - 1:
            raise ValueError('Symbols len should be the same as number - 1')
        numbers: Range = Range(1, number - 1) 
        result: List[int] = []
        for char in reversed(symbols):
            if char == 'D':
                result.append(numbers.min)
                numbers = Range(numbers.min + 1, numbers.max)
            else:
                result.append(numbers.max)
                numbers = Range(numbers.min, numbers.max - 1)
        result.append(numbers.min)
        result.reverse()
        return result




