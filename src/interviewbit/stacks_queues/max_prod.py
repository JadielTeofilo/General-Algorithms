"""
Problem Description

You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:

    LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (i>j). If multiple A[j]'s are present in multiple positions, the LeftSpecialValue is the maximum value of j.
    RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (j>i). If multiple A[j]'s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

NOTE:  As the answer can be large, output your answer modulo 109 + 7.



Problem Constraints

1 <= N <= 105

1 <= A[i] <= 109


Input Format

First and only argument is an integer array A.


Output Format

Return an integer denoting the maximum special product of any integer.


[1, 4, 3, 4]
 -

4
4

0 1
2 3

2 1

We want to find the closest bigger element on the right and left
If we know those values for each i, we can just iterate and get the max

O(n) space and time where n is the size of the input

"""
import collections
from typing import List, Iterable


StackValue = collections.namedtuple('StackValue', 'value index')


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, numbers: List[int]) -> int:
        right_specials: List[int] = self.build_cache(numbers)
        left_specials: List[int] = self.build_cache(numbers, reverse=True)
        result: int = 0
        for right_special, left_special in zip(right_specials, left_specials):
            result = max(right_special * left_special, result)
        return result

    def build_cache(self, numbers: List[int], 
                    reverse: bool = False) -> List[int]:
        cache: List[int] = [0] * len(numbers)
        stack: List[StackValue] = []
        indices: Iterable[int] = (range(len(numbers)) if not reverse 
                                  else range(len(numbers) -1, -1, -1))
        for index in indices:
            num = numbers[index]
            while stack and stack[-1].value < num:
                curr: StackValue = stack.pop()
                cache[curr.index] = index
            stack.append(StackValue(num, index))
        return cache


 
