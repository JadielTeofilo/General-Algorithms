"""

Chess Game


Two players
    
    A player can move a piece on its turn
    Each turn has a max time of 1 min then player is forced to make a move
    A player can get the piece from the adversary
    A player can win the game by getting the king


INITIAL_POSITIONS = {} #TODO


ChessGame (singleton)
    - board
    - turn

    + run()


Player
    WhitePicesPlayer
    BlackPiecesPlayer


Board
    - grid: List[List[Optional[Piece]]]

    + reset_board()

Piece
    +move(position: Position): Optional[Piece]

    QueenPiece
    KingPiece
    PawnPiece

Turn (singleton)
    - player: Player
    - start_time: int


Position
    - row
    - col

"""
import abc
import collections
import dataclasses
import threading
from typing import List, Optional



Position = collections.namedtuple('Position', 'row col')


class ChessGame:
    _intance: Optional['ChessGame'] = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls, *args, **kargs) -> 'ChessGame':
        if cls._instance:
            return cls._instance
        with cls._lock:
            if cls._instance:
                return cls._instance
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> 
        self._board: Board = Board()
        self._turn: Turn = Turn()




@dataclasses.dataclass
class Player(abc.ABC):
    @property
    @abc.abstractmethod
    def priority(self):
        pass


@dataclasses.dataclass
class BlackPiecePlayer(Player):
    _priority: int
    @property
    def priority(self):
        return self._priority









