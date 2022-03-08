"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



[
[9,9,4],
[6,6,8],
[2,1,1]]

[
[3,4,5],
[3,2,6],
[2,2,1]]



for each possible starting point we try going on all possible sides
get the side with the biggest value

we can cache a give position best result
keep track of a max


In - matrix: Matrix
Out - int


O(n*m) time complexity where n=rows, m=cols
O(n*m) space

"""
import collections
from typing import List, Dict, Iterable


Position = collections.namedtuple('Position', 'row col')
Matrix = List[List[int]]
Cache = Dict[Position, int] 


class Solution:
    def longestIncreasingPath(self, matrix: Matrix) -> int:
        longest_path: Dict[str, int] = {'val': 0}
        cache: Cache = {}
        for position in self.get_positions(matrix):
            self.update_longest_path(matrix, position, longest_path, cache)
        return longest_path['val']

    def update_longest_path(self, matrix: Matrix, curr: Position,
                            longest_path: Dict[str, int], 
                            cache: Cache) -> int:
        """
        [
            [3,4,5],
            [3,2,6],
            [2,2,1]
        ]
        """
        if curr in cache:
            return cache[curr]
        max_path: int = 0
        for position in self.possible_positions(matrix, curr):
            max_path = max(
                max_path, 
                self.update_longest_path(matrix, position, longest_path, cache)
            )
        cache[curr] = max_path + 1
        longest_path['val'] = max(longest_path['val'], cache[curr])
        return cache[curr]

    def possible_positions(self, matrix: Matrix, 
                           position: Position) -> Iterable[Position]:
        possibilities: List[Position] = [
            Position(position.row + 1, position.col),
            Position(position.row - 1, position.col),
            Position(position.row, position.col + 1),
            Position(position.row, position.col - 1),
        ]
        for possibility in possibilities:
            if self.is_valid(matrix, possibility, position):
                yield possibility

    def is_valid(self, matrix: Matrix, possibility: Position, 
                 position: Position) -> bool:
        if possibility.col < 0 or possibility.row < 0:
            return False
        if (possibility.row >= len(matrix) or 
            possibility.col >= len(matrix[0])):
            return False
        if (matrix[possibility.row][possibility.col] <= 
            matrix[position.row][position.col]):
            return False
        return True
    
    def get_positions(self, matrix: Matrix) -> Iterable[Position]:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                yield Position(row, col)
