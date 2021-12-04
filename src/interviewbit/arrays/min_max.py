"""
Problem Description

Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

NOTE: You should make minimum number of comparisons.


In - numbers: List[int]
Out - Sum

[2, 1 , 4 , 6, 2 , 9 ]

We could use two heaps, one max, other min 
Or just iterate on the array keeping track of min and max
	The comparison num here is 2*n
Or use divide and conquer approach 

T(n) = 2 + 2*T(n/2)
...
T(2) = 1  # There will be n/2 elements like these, above it we have n/2+n/4+n/8 ...n/n comparisons
T(1) = 0

This will be a bit over n comparisons, which is better than 2*n
The whole point is to save comparisons by doing only one to check the min and max



Problem Constraints

1 <= N <= 105

-109 <= A[i] <= 109



Input Format

First and only argument is an integer array A of size N.


Output Format

Return an integer denoting the sum Maximum and Minimum element in the given array.



"""
import collections
import math
from typing import Union, List


Edges = collections.namedtuple('Edges', 'min max')


class Solution:
	# @param A : list of integers
	# @return an integer
        def solve(self, numbers: List[int]) -> int:
            edges: Edges = self.get_max_min(
                numbers, start=0, end=len(numbers) - 1
            )
            return edges.max + edges.min

        def get_max_min(self, numbers: List[int], start: int, 
                        end: int) -> Edges:
            if start >= end:
                return Edges(numbers[start], numbers[start])
            # Case list has size 2
            if end - start == 1:
                if numbers[start] > numbers[end]:
                    return Edges(numbers[end], numbers[start])
                else:
                    return Edges(numbers[start], numbers[end])
            pivot: int = (start + end) // 2
            left_edges: Edges = self.get_max_min(numbers, start, pivot)
            right_edges: Edges = self.get_max_min(numbers, pivot + 1, end)
            return Edges(min(left_edges.min, right_edges.min),
                         max(left_edges.max, right_edges.max))


