"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]

Elements for which no smaller element exist, consider next smaller element as -1.

Input Format

The only argument given is integer array A.

Output Format

Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element occurs G[i] should be -1.


[4, 5, 2, 10, 8]


(2, -3)
(10 -2)
(8 -1)

Keep a monotonic stack (increasing)
When poping update the poped value index

O(n) time and space where n is the size of the inputed array 

In - numbers: List[int]
Out - List[int]

"""
import collections
from typing import List


StackValue = collections.namedtuple('StackValue', 'value index')


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, numbers: List[int]) -> List[int]:
        result: List[int] = [-1] * len(numbers)
        stack: List[StackValue] = []
        for index in range(len(numbers) - 1, -1, -1):
            while stack and stack[-1].value > numbers[index]:
                stack_item: StackValue = stack.pop()
                result[stack_item.index] = numbers[index]
            stack.append(StackValue(numbers[index], index))
        return result


