"""
 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color.


In - image: List[List[int]], target: Point, color: int
Out - None

Can I fill in the diagonal?
yes



0 0 1 1 1 2 1
1 1 0 1 2 1 2 
1 0 1 1 2 2 1


O(n) time complexity where n is the number of pixels on the image
O(n) space complexity n being the number of pixels due to the recursion algo

"""
from typing import List, Set
import collections


Image = List[List[int]]
Point = collections.namedtuple('Point', 'row col')


def paint_fill(image: Image, target: Point, color: int) -> None:
	""" Changes target to color and do the same to the 
		surrounding until different color is found """
	if not image or not image[0]:
		raise ValueError('Empty image')
	visited: Set[Point] = set()
	paint_fill_helper(image, target, color, visited)


def paint_fill_helper(image: Image, current: Point, 
		  color: int, visited: Set[Point]) -> None:
	if current in visited:
		return
	sides: List[Point] = get_possible_sides(
		current, image, visited
	)
	image[current.row][current.col] = color
	visited.add(current)
	for side in sides: 
		paint_fill_helper(image, side, color, visited)


def get_possible_sides(point: Point, image: Image, 
					   visited: Set[Point]) -> List[Point]:
	current_color: int = image[point.row][point.col]
	sides: List[Point] = [
		Point(point.row+1, point.col),
		Point(point.row-1, point.col),
		Point(point.row, point.col-1),
		Point(point.row, point.col+1),
	]
	possible_sides: List[Point] = []
	for side in sides:
		if (outside_bounds(side, image) or
		    image[side.row][side.col] != current_color): 
			continue
		possible_sides.append(side)

	return possible_sides

def outside_bounds(point: Point, image: Image) -> bool:
	max_col: int = len(image[0]) - 1
	max_row: int = len(image) - 1
	return (point.col > max_col or point.col < 0 
 		    or point.row > max_row or point.row < 0)


image = [
[1, 0, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 1, 0],
[1, 1, 1, 0, 0],
]
paint_fill(image, Point(1,0), 2)
for row in image:
	print(row)
import pdb;pdb.set_trace()
