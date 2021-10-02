"""
Intersection: Given two straight line segments (represented as a start point and an end point),
compute the point of intersection, if any.

In - first_line: Line, second_line: Line
Out - Optional[Point]


points are integers?
aye desu

O(1) time complexity 
O(1) space complexity
"""
import dataclasses
from typing import Optional


@dataclasses.dataclass
class Point:
    x: Optional[float] = None
    y: Optional[float] = None


@dataclasses.dataclass
class Line:
    start: Point  # Assumes start has the smallest x value
    end: Point

    def __post_init__(self):
        self.slope: float = self.build_slope()
        # Intercept is the y value where 
        # the line crosses the y axis
        self.intercept: float = self.build_intercept()

    def build_slope(self) -> float:
        return ((self.end.y - self.start.y) / 
                (self.end.x - self.start.x))

    def build_intercept(self) -> float:
        return self.start.y - self.slope * self.start.x


def find_intersection(first_line: Line, 
                      second_line: Line) -> Optional[Point]:
    # Case they are parallel
    if first_line.slope == second_line.slope:
        if first_line.intercept == second_line.intercept:
            if in_between(first_line.end, second_line.start,
                          second_line.end):
                return first_line.end
            if in_between(second_line.end, first_line.start,
                          first_line.end):
                return second_line.end
        else:
            return
    
    intersection: Point = Point()
    intersection.x = ((first_line.intercept - second_line.intercept) /
                      (second_line.slope - first_line.slope))
    intersection.y = first_line.slope * intersection.x + first_line.intercept
    if (in_between(intersection, first_line.start, first_line.end) and
        in_between(intersection, second_line.start, second_line.end)):
        return intersection
    return
    

def in_between(target: Point, start: Point, end: Point) -> bool:

    # No need to check x cause start.x is assumed to be 
    # always bigger equal than end.x
    in_between_x: bool = target.x >= start.x and target.x <= end.x
    if start.y <= end.y:
        in_between_y: bool = target.y >= start.y and target.y <= end.y
    else:
        in_between_y: bool = target.y >= end.y and target.y <= start.y
    return in_between_y and in_between_x


line1 = Line(Point(2, 11), Point(36, 34))
line2 = Line(Point(5, 18), Point(20, 7))

print(find_intersection(line1, line2))
line1 = Line(Point(14, 19), Point(26, 27))
line2 = Line(Point(20, 23), Point(36, 34))

print(find_intersection(line1, line2))
import pdb;pdb.set_trace()
