"""
Langton's Ant: An ant is sitting on an infinite grid of white and black squares. It initially faces right.
At each step, it does the following:
(1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward
one unit.
(2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise), and move
forward one unit.
Write a program to simulate the first K moves that the ant makes and print the final board as a grid.
Note that you are not provided with the data structure to represent the grid. This is something you
must design yourself. The only input to your method is K. You should print the final grid and return
nothing. The method signature might be something like void printKMoves (int K) .




"""
import dataclasses
import enum
from typing import List, Set, Optional
import math
import unittest


class Direction(enum.Enum):
    right = 0
    down = 1
    left = 2
    up = 3


class Color(enum.Enum):
	white = 0
	black = 1
	

@dataclasses.dataclass
class Position:
    row: int = 0
    column: int = 0

    def move(self, direction: Direction) -> None:
        if direction == Direction.right:
            self.column += 1
        elif direction == Direction.left:
            self.column -= 1
        elif direction == Direction.down:
            self.row += 1 
        elif direction == Direction.up:
            self.row -= 1


@dataclasses.dataclass
class Ant:
    position: Position = Position()
    direction: Direction = Direction.right

    def move(self) -> None:
        self.position.move(self.direction)
            

    def flip(self, side: int) -> None:
        """ Flips direction 90 degree to right (side=1) or left (side=-1) """
        self.direction = Direction((self.direction.value + side) % 4)


Coordinate = collections.namedtuple('Coordinate', ['row', 'column'])
Limits = collections.namedtuple('Limits', ['max', 'min'])


@dataclasses.dataclass
class Grid:

	blacks: Set[Coordinate] = dataclasses.field(default_factory=set)
	row_limits: Limits = Limits(-math.inf, math.inf)
	column_limits: Limits = Limits(-math.inf, math.inf)

	def update_limits(self, position: Position) -> None: 
		self.row_limits = Limits(max(row_limits.max, position.row), 
 								 min(row_limits.min, position.row))
		self.column_limits = Limits(max(column_limits.max, position.column), 
				      			    min(column_limits.min, position.column))

	def flip(self, position: Position) -> None:
		coordinate: Coordinate = Coordinate(position.row, position.column)
		if coordinate in self.blacks:
			self.blacks.remove(coordinate)
		else:
			self.blacks.add(coordinate)

	def get_color(self, position: Position) -> Color:
		coordinate: Coordinate = Coordinate(position.row, position.column)
		return Color.black if coordinate in blacks else Color.white

	def build_matrix(self) -> List[List[int]]:
		row_size: int = self.row_limits.max - self.row_limits.min
		column_size: int = self.column_limits.max - self.column_limits.min
		matrix: List[List[int]] = [[0] * row_size for _ in range(column_size)]
		row_offset: int = self.row_limits.min 
		column_offset: int = self.column_limits.min
		for row in range(self.row_limits.min, self.row_limits.max + 1):
			for column in range(self.column_limits.min, self.column_limits.max + 1):
				matrix[row+row_offset][column+column_offset] = 0 if 
				

		return matix

	
def print_k_moves(k: int) -> List[List[int]]:
	ant: Ant = Ant()
	grid: Grid = Grid()
	
	while k > 0:
		k -= 1
		make_movement(ant, grid)

	return grid.build_matrix()  # TODO implement this


def make_movement(ant: Ant, grid: Grid) -> None:
	
	
	current_color: Color = grid.get_color(ant.position)  # TODO implement
	grid.flip(ant.position)
	grid.update_limits(ant.position)
	if current_color == Color.white:
		ant.flip(1)
	else:
		ant.flip(-1)
	ant.move()
		

	




