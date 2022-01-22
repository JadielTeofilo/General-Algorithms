"""
Best Line: Given a two-dimensional graph with points on it, find a line which passes the most
number of points.

In - List[Point]
Out - Line


Try all points as a starting point, keep track of visited so no repeated work is done

O(n^3) time complexity where n is the amount of points

"""
import collections
import dataclasses
import math
from typing import List, Optional, Union, Dict


PRECISION = 2  # All float values will be rounded by it


Point = collections.namedtuple('Point', 'x y')
Cache = collections.namedtuple('Cache', 'slope point')
Line = collections.namedtuple('Line', 'slope yintercept xintercept')


def best_line(points: List[Point]) -> Optional[Line]:
    """ Finds the line that crosses the most points """
    if len(points) < 2:
        raise ValueError('There has to be at least two points')
    lines: Dict[Line, int] = build_lines(points)
    best_line: Optional[Line] = None
    max_points: int = 0
    for line, count in lines.items():
        if count > max_points:
            max_points = count
            best_line = line
    return best_line


def build_lines(points: List[Point]) -> Dict[Line, int]:
    """ Builds all possible lines using given points """
    lines: Dict[Line, int] = collections.defaultdict(int)
    for index, starting_point in enumerate(points[:-1]):
        for ending_point in points[index + 1:]:
            if starting_point == ending_point:
                continue
            line: Line = build_line(starting_point, ending_point)
            lines[line] += 1
    return lines


def build_line(starting_point: Point, ending_point: Point) -> Line:
    slope: float = find_slope(starting_point, ending_point)
    yintercept: Optional[float] = find_yintercept(starting_point, slope)
    xintercept: Optional[float] = find_xintercept(starting_point, slope, yintercept)
    return Line(slope, yintercept, xintercept)


def find_slope(first_point: Point, second_point: Point) -> float:
    if first_point.x == second_point.x:
        return math.inf if first_point.y < second_point.y else -math.inf
    return round((second_point.y - first_point.y)/
                 (second_point.x - first_point.x), PRECISION)


def find_yintercept(point: Point, slope: float) -> Optional[float]:
    if abs(slope) == math.inf:
        return 
    return round(point.y - point.x * slope, PRECISION)


def find_xintercept(point: Point, slope: float, 
                    yintercept: Optional[float]) -> Optional[float]:
    if slope == 0:
        return
    # Returns x of point if it is a vertical line
    if yintercept is None:
        return point.x
    return round(-(yintercept/slope), PRECISION)


points = [
    Point(1, 5), 
    Point(3, 2), 
    Point(6, 3), 
    Point(2, 5), 
    Point(-1, 3), 
    Point(-3, 9), 
    Point(7, 3), 
    Point(5, 6), 
]
print(best_line(points))
