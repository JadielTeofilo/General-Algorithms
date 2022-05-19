"""
1293. Shortest Path in a Grid with Obstacles Elimination

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



0 1 0 0 
0 0 1 0
0 1 0 0
0 0 0 1
1 0 1 0

k = 2

[((0,0), 2, 0) ]

use the position and k as visited

have a deque, pop and add all neighbors
if neighbor == 1, make it be k - 1, if k < 0, dont use it

position, k, distance

((0,1), 1, 1) -> (0,2, 1, 2) (1,1, 1, 2)

O(m*n*k) time and space complexity
O(m*n*k) space complexity


"""
import collections
from typing import List, Set, Iterator, Tuple, Deque


Position = collections.namedtuple('Position', 'row col')
QueueValue = collections.namedtuple('QueueValue', 'pos k distance')


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        last_position: Position = Position(len(grid) - 1, len(grid[0]) - 1)
        visited: Set[Tuple[Position, int]] = set()
        deque: Deque[QueueValue] = collections.deque(
            [QueueValue(Position(0, 0), k - grid[0][0], 0)]
        )
        while deque:
            curr: QueueValue = deque.popleft()
            if (curr.pos, curr.k) in visited or curr.k < 0:
                continue
            visited.add((curr.pos, curr.k))
            if curr.pos == last_position:
                return curr.distance
            for neighbor in self.get_neighbors(grid, curr.pos):
                deque.append(
                    QueueValue(
                        neighbor, curr.k - grid[curr.pos.row][curr.pos.col],
                        curr.distance + 1,
                    )
                )

        return -1
    
    def get_neighbors(self, grid: List[List[int]], 
                      curr: Position) -> Iterator[Position]:
        options: List[Position] = [
            Position(-1, 0), Position(1, 0), Position(0, -1), Position(0, 1),
        ]
        for option in options:
            new: Position = Position(option.row + curr.row, 
                                     option.col + curr.col)
            if 0 <= new.row < len(grid) and 0 <= new.col < len(grid[0]):
                yield new

