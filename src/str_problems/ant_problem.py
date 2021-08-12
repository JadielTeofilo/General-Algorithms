"""
Langton's Ant: An ant is sitting on an infinite grid of white and black squares. It initially faces right.
At each step, it does the following:
(1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward
one unit.
(2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise). and move
forward one unit.
Write a program to simulate the first K moves that the ant makes and print the final board as a grid.
Note that you are not provided with the data structure to represent the grid. This is something you
must design yourself. The only input to your method is K. You should print the final grid and return
nothing. The method signature might be something like void printKMoves (int K).
Hints: #474, #487, #533, #540, #559, #570, #599, #676, #627

in: 

int k

out: 

none (prints result)


Is the initial grid supposed to have random white and black squares?
I can infere the size of the grid based on K, grid K*2+1 by K*2+1
What should be printed, only a square around what was visited?


[0, 0, 0, 1]
[1, 0, 0, 1]
[1, 1, 1, 0]
[0, 0, 0, 1]





"""
import dataclasses
import enum
import collections
import random
import unittest
from typing import List, Dict


class Direction(enum.Enum):
	right = 0
	left = 1
	up = 2
	down = 3

@dataclasses.dataclass
class Position:
	row: int
	column: int


@dataclasses.dataclass
class Ant:
	position: Position
	direction: Direction


def print_k_moves(k: int) -> None:

	grid: List[List[int]] = build_grid(k)
	ant = Ant(position=Position(row=k, column=k), direction=Direction.right)
	for row in grid:
		print(row)
	while k > 0:
		make_move(grid, ant)
		k -= 1
	print(ant)
	for row in grid:
		print(row) 
	

def build_grid(k: int) -> List[List[int]]: 
	size: int = k*2+1
	grid: List[List[int]] = [[0]*size]*size
	for row in range(size):
		for column in range(size):
			grid[row][column] = random.randrange(0, 2)
	return grid


def make_move(grid: List[List[int]], ant: Ant):
	current_position: Position = ant.position
	current_value: int = grid[current_position.row][current_position.column]
	# Flip grid value
	grid[current_position.row][current_position.column] += 1
	grid[current_position.row][current_position.column] %= 2 
	
	if current_value == 1:  # In case of black, turn 90 degrees left
		ant.direction = Direction((ant.direction.value - 1)%4)
	else:  # In case of white turn 90 to right
		ant.direction = Direction((ant.direction.value + 1)%4)

	go_foward(grid, ant)



def go_foward(grid: List[List[int]], ant: Ant):
	if ant.direction == Direction.left:
		ant.position.column -= 1
	elif ant.direction == Direction.right:
		ant.position.column += 1
	elif ant.direction == Direction.up:
		ant.position.row -= 1
	elif ant.direction == Direction.down:
		ant.position.row += 1


class Test(unittest.TestCase):

	def test(self):
		pass

if __name__ == '__main__':
	import pdb;pdb.set_trace()
