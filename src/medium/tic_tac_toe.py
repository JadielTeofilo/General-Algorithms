"""
Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.


In - board: TicTacToeBoard
Out - Optional[Symbol]




board = [
[ , , ],
[ , , ],
[ , , ],
]

O(n) time complexity n being the amount of spots on the board


"""
import enum
import dataclasses
from typing import List, Optional


class Symbol(enum.Enum):
    empty = 0
    square = 1
    circle = 2


@dataclasses.dataclass
class TicTacToeBoard:
    size: int 

    def __post_init__(self) -> None:
        self.matrix: List[List[Symbol]] = [[Symbol.empty] * self.size 
                                           for _ in self.size]

def win_finder(board: TicTacToeBoard) -> Optional[Symbol]:
    # TODO check for empty input
    return (check_columns(board) or
            check_lines(board) or
            check_diagonals(board))


def check_columns(board: TicTacToeBoard) -> Optional[Symbol]:
    """ Goes on every column of matrix and check if 
        all values are the same, if so, returns it """
    for col in range(len(board[0])):
        current_value: Optional[Symbol] = None
        for row in range(len(board)):
            if current_value is None: 
                current_value = board[row][col]
            if current_value != board[row][col]:
                break
        else:
            if current_value != Symbol.empty:
                return current_value 
    return None


def check_diagonals(board: TicTacToeBoard) -> Optional[Symbol]:
    """ Check both diagonals to see if there is 
        only one symbol """
    return left_diagonal(board) or right_diagonal(board)


def left_diagonal(board: TicTacToeBoard) -> Optional[Symbol]:
    current_value: Optional[Symbol] = None
    for row in range(len(board)):
        current_value = board[row][row] if not current_value 
                        else current_value
        if current_value != board[row][row]:
            break
    else:
        return current_value 
               if current_value != Symbol.empty else None
    return None


def right_diagonal(board: TicTacToeBoard) -> Optional[Symbol]:
    """ Checks the diagonal starting from the 
        right side of the matrix """
    current_value: Optional[Symbol] = None
    last_column: int = len(board[0]) - 1
    for row in range(len(board)):
        if current_value is None:
            current_value = board[row][last_column - row]
        if current_value != board[row][last_column - row]:
            break
    else:
        return current_value 
               if current_value != Symbol.empty else None
    return None


def check_lines(board: TicTacToeBoard) -> Optional[Symbol]:
    """ Checks if any row has all the same symbols, 
        if so, returns it """
    for row in range(len(board)):
        current_value: Optional[Symbol] = None
        for col in range(len(board[0])):
            if current_value is None:
                current_value = board[row][col]
            if current_value != board[row][col]:
                break
        else:
            if current_value != Symbol.empty:
                return current_value
    return None
    

    

