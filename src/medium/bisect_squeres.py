"""
Bisect Squares: Given two squares on a two-dimensional plane, find a line that would cut these two
squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis.
Hints: #468, #479, #528, #560


.         .


.         .  
                



                .       .
                                
                                
                .       .

In - first: Square, second: Squere
Out - line: Line 


A line that cuts in half a square goes through the middle point of it

"""
import collections
import dataclasses
from typing import List, Optional, Tuple
import math


Point = collections.namedtuple('Point', 'x y')


@dataclasses.dataclass
class Line: 
    start: Point
    end: Point

    def slope(self) -> float:
        if self.start.x == self.end.x:
            return math.inf if self.start.y < self.end.y else -math.inf
        return abs((self.end.y - self.start.y)/
                   (self.end.x - self.start.x))

    def yintercept(self) -> float:
        if abs(self.slope()) == math.inf:
            raise ValueError('Vertical lines have no yintercept')
        return self.start.y - self.slope() * self.start.x


@dataclasses.dataclass
class Square:
    top_left: Point
    top_right: Point
    bottom_left: Point
    bottom_right: Point

    def lines(self) -> List[Line]:
        return [
            Line(self.top_left, self.top_right), 
            Line(self.bottom_left, self.bottom_right), 
            Line(self.top_left, self.bottom_left),
            Line(self.top_right, self.bottom_right),
        ]


def find_middle_line(
    first: Square, 
    second: Square
) -> Tuple[List[Point], List[Point]]:
    """ Finds line that cuts both squares in half """
    if first.top_left.x > second.top_left.x:
        return find_middle_line(second, first)
    crossing_line: Line = Line(find_mid_point(first), find_mid_point(second))
    if crossing_line.start == crossing_line.end:
        raise ValueError('Both squares have the same center')
    if crossing_line.slope() == 0:  # If they are next to each other
        return  ([], []) # TODO the mid point of the square
    if abs(crossing_line.slope()) == math.inf: # Above each other
        return  ([], [])# TODO the mid point of the square
    return (find_intersection_points(crossing_line, first),
            find_intersection_points(crossing_line, second))


def find_mid_point(square: Square) -> Point:
    return Point((square.top_right.x + square.top_left.x)//2,
                 (square.top_right.y + square.bottom_right.y)//2)


def find_intersection_points(line: Line, square: Square) -> List[Point]:
    """ Finds the intersection points of a line with a square"""
    result: List[Point] = []
    for square_line in square.lines():
        intersection: Optional[Point] = find_intersection(
            line, square_line
        )
        if intersection:
            result.append(intersection)
    return result


def find_intersection(line: Line, 
                      square_line: Line) -> Optional[Point]:
    if abs(line.slope()) in [0, math.inf]:
        raise ValueError('Method only calculates the intersection of non vertical or horizontal lines')
    if square_line.slope() == 0:
        y: float = square_line.start.y
        x: float = (y - line.slope()) / line.yintercept()
    if abs(square_line.slope()) == math.inf:
        x: float = square_line.start.x
        y: float = line.slope() * x + line.yintercept()
    intersection: Point = Point(x, y)
    # Checks to see if the point is 
    # actually inside the lines, since the 
    # intersection was found considering infinite lines
    if is_inside(intersection, square_line):
        return intersection


def is_inside(point: Point, line: Line) -> bool:
    
    return ((min(line.start.x, line.end.x) <= point.x) and
            (max(line.start.x, line.end.x) >= point.x) and
            (min(line.start.y, line.end.y) <= point.y) and
            (max(line.start.y, line.end.y) >= point.y))


a = Square(Point(2,4), Point(4,4), Point(2,2), Point(4,2))
b = Square(Point(8,6), Point(10,6), Point(8,4), Point(10,4))
print(find_middle_line(a, b))

