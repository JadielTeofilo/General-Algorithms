"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right. 


In - rows: int, columns: int, grid: List[List[bool]]

Out - List[Position]


1	1	1	0	0
0	1	0	1	1
0	1	1	0	1
1	0	1	1	1


O(m * n) space
O(m * n) time complexity



"""
from typing import List, Dict
import collections


Position = collections.namedtuple('Position', 'row column')


_Grid = List[List[bool]]
_Cache = Dict[Position, List[Position]]


def find_path(rows: int, columns: int, 
			  grid: _Grid) -> List[Position]:
	
	positions: List[Position] = [Position(0, 0)]
	limit: Position = Position(rows - 1, columns - 1)
	return find_helper(positions, {}, limit, grid)


def find_helper(positions: List[Position], cache: _Cache,
				limit: Position, grid: _Grid) -> List[Position]:
	"""
		Does recursion to find possible path
	"""
	curr: Position = positions[-1]
	if cache.get(curr):
		return cache[curr]
	if is_invalid_position(curr, limit, grid):
		return []
	if curr == limit:
		return positions
	path: List[Position] = find_helper(
		positions + [Position(curr.row + 1, curr.column)], 
		cache, limit, grid
	)  # Tries going down
	if path:
		cache[curr] = path
		return cache[curr]
	path = find_helper(
		positions + [Position(curr.row, curr.column + 1)], 
		cache, limit, grid
	)  # Tries going right
	
	cache[curr] = path
	return cache[curr]
	

def is_invalid_position(position: Position, 
						limit: Position, grid: _Grid) -> bool:
	"""
		Position is invalid if it is out of limit or on 
		invalid grid position
	"""
	if (position.row > limit.row or 
		position.column > limit.column):
		return True
	return grid[position.row][position.column] == 0
	

grid = [
[1, 1, 0, 1, 0],
[1, 0, 0, 1, 0],
[1, 1, 0, 1, 0],
[0, 1, 1, 1, 1],
]
find_path(4, 5, grid)
import pdb;pdb.set_trace()	
