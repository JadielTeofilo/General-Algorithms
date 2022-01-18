"""
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

1 5 2 1 7 6 2 2 4

n^2 combinations

6: [(0, 1), (1, 9), (7, 1)]


In - numbers: List[int]
Out - List[int]

Iterate on the pairs building the sum_cache
    defaultdict(list)

find the sum_cache with more than one tuple that has the smallest first tuple
    iterate on sum cache, keeping a min_position and a result_tuples
return the first two concatenated

Note:

1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)

If no solution is possible, return an empty list.

O(n^2) time and space complexity where n is the size of the input

"""
import collections
import math
from typing import Optional, List, Dict


Duo = collections.namedtuple('Duo', 'left right')
Cache = Dict[int, List[Duo]]


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, numbers: List[int]) -> List[int]:
        sum_cache: Cache = collections.defaultdict(list)
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] in sum_cache:
                    for duo in sum_cache[numbers[i] + numbers[j]]:
                        if self.is_valid(i, j, duo):
                            return [duo.left, duo.right, i, j]
                sum_cache[numbers[i] + numbers[j]].append(
                    Duo(i, j)
                )
        return []

    def is_valid(self, i: int, j: int, duo: Duo) -> bool:
        # Returns true if they are all distinct
        return len({i, j, duo.left, duo.right}) == 4

