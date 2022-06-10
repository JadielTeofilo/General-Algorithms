"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).


1 3 2
3 5 1
2 4 2

we keep a heap of all the available paths at a given cost
we get the element with the least cost and add its neighbors to the heap the cost is max(curr, neighbor_cost)
keep a visited set

return when the element poped from the heap is the last element


O(n*m*log(n*m)) time complexity where n = rows, m = cols
O(n*m) space complexity



"""
import collections
import heapq
from typing import List, Set, Iterator


Matrix = List[List[int]]
Position = collections.namedtuple('Position', 'row col')
HeapValue = collections.namedtuple('HeapValue', 'cost position')


class Solution:
    def swimInWater(self, matrix: Matrix) -> int:
        if not matrix or not matrix[0]:
            raise ValueError('Can not handle empty matrix')
        heap: List[HeapValue] = [HeapValue(matrix[0][0], Position(0, 0))]
        visited: Set[Position] = set()
        while heap:
            cost, position = heapq.heappop(heap)
            if position in visited:
                continue
            visited.add(position)
            if self.is_last_position(matrix, position):
                return cost
            for row, col in self.get_neighbors(position, matrix):
                heapq.heappush(
                    heap, 
                    HeapValue(max(matrix[row][col], cost), 
                              Position(row, col)),
                )

    def is_last_position(self, matrix: Matrix, position: Position) -> bool:
        return (position.row == len(matrix) - 1 and 
                position.col == len(matrix[0]) - 1)

    def get_neighbors(self, position: Position, 
                      matrix: Matrix) -> Iterator[Position]:
        options: List[Position] = [
            Position(position.row, position.col + 1),
            Position(position.row, position.col - 1),
            Position(position.row + 1, position.col),
            Position(position.row - 1, position.col),
        ]
        for option in options:
            if self.is_valid(option, matrix):
                yield option

    def is_valid(self, position: Position, matrix: Matrix) -> bool:
        return (position.row >= 0 and position.col >= 0 and 
                position.row < len(matrix) and 
                position.col < len(matrix[0]))


