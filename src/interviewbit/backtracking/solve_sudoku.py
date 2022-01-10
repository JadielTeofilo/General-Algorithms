"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'

You may assume that there will be only one unique solution.

and its solution numbers marked in red.

Example :

For the above given diagrams, the corresponding input to your program will be

[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]

and we would expect your program to modify the above array of array of characters to

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]


In - board: List[List[str]]
Out - List[List[str]]

Iterate on empty spots 
for curr spot, find valid numbers
iterate on valid numbers
recurse with that option selected


"""
import collections
from typing import List, Iterable, Set


Spot = collections.namedtuple('Spot', 'row col')
Board = List[List[str]]
POSSIBLE_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, board: List[List[str]]) -> List[List[str]]:
        spot = self.find_empty_spot(board)
        for number in self.valid_numbers(board, spot):
            new_board: List[List[str]] = [row.copy() for row in board]
            new_board[spot.row][spot.col] = number
            new_board = self.solveSudoku(new_board)
            if new_board:
                return new_board
        return []

    def find_empty_spot(self, board: Board) -> Spot:
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '.':
                    return Spot(row, col)
        raise ValueError('empty board')

    def valid_numbers(self, board: Board, 
                      spot: Spot) -> Iterable[str]:
        possible: Set[str] = set(POSSIBLE_NUMBERS)
        self.remove_same_column_or_row(possible, spot, board)
        self.remove_same_group(possible, spot, board)
        return list(possible)

    def remove_same_column_or_row(self, result: Set[str], 
                           spot: Spot, board: Board) -> None:
        for row in range(len(board)):
            result.discard(board[row][spot.col])
        for col in range(len(board[0])):
            result.discard(board[spot.row][col])

    def remove_same_group(self, result: Set[str], spot: Spot, 
                          board: Board) -> None:
        start: Spot = self.find_start_spot(spot)
        end: Spot = self.find_end_spot(spot)
        for row in range(start.row, end.row + 1):
            for col in range(start.col, end.col + 1):
                # Removes O(1) no exception if missing
                result.discard(board[row][col])
    
    def find_start_spot(self, spot: Spot) -> Spot:
        return Spot((spot.row // 3)*3, (spot.col // 3)*3)

    def find_end_spot(self, spot: Spot) -> Spot:
        return Spot((spot.row // 3)*3+2, (spot.col // 3)*3+2)





