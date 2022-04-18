"""
Given 2 integers A and B and an array of integars C of size N.

Element C[i] represents length of ith board.

You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board.

        2 painters cannot share a board to paint. That is to say, a board
        cannot be painted partially by one painter, and partially by another.
        A painter will only paint contiguous boards. Which means a
        configuration where painter 1 paints board 1 and 3 but not 2 is
        invalid.

Return the ans % 10000003

3 1

2 3 1 4
 |   | |
2 5 6 10

start = max(nums)
end = sum(nums)

check if partition is valid = number of partitions < painters
    if not, try with a bigger time
else,  try with a smaller time
update result

O(n*log(sum - max)) time where n is the size of list of boards
O(1) space

In - painters: int, cost: int, boards: List[int]
Out - int
"""
from typing import List


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, painters: int, cost: int, 
              boards: List[int]) -> int:
        """
        A : 2
        B : 5
        C : [ 1, 10 ]
        """
        start: int = max(boards)
        end: int = sum(boards) + 1
        result: int = end
        while start < end:
            time: int = (start + end) // 2
            partitions: int = self.get_partitions(time, boards)
            if partitions <= painters:
                result = min(result, time)
                end = time
            else:
                start = time + 1
        return (result * cost) % 10000003

    def get_partitions(self, size: int, boards: List[int]) -> int:
        partitions: int = 0
        curr_sum: int = 0
        for board in boards:
            if curr_sum + board > size:
                partitions += 1
                curr_sum = 0
            curr_sum += board
        if curr_sum > 0:
            partitions += 1
        return partitions

