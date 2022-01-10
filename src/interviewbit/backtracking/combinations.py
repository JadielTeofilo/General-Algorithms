"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

    Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
    Entries should be sorted within themselves.

Example :

If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]


In - number: int, size: int 
Out - List[List[int]]

[1 2 3 4]

solve(size: int, current: List[int])
stops when the size is zero

                                                _
                        1                                               _
            2                       _                       2                       _
            X               3               _       3               _           3           _
                            X                       X       4               _
                                                            X





"""
from typing import List


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, number:int, size: int) -> List[List[int]]:
        self.result: List[List[int]] = []
        self.update_result(size, start=1, end=number+1,
                           current=[])
        self.result.sort()
        return self.result

    def update_result(self, size: int, start: int, end: int,
                      current: List[int]) -> None:
        if size == 0:
            current.sort()
            self.result.append(current)
        for num in range(start, end):
            self.update_result(size - 1, num + 1, end, current + [num])


