"""


You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 

You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.

NOTE: This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.


    We need to go through the points meajuring the distance from current to last
"""
import collections


Point = collections.namedtuple('Point', 'x y')


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B) -> int:
        """
        """
        if not A or not B:
            return 0
        last: Point = Point(A[0], B[0])
        result: int = 0
        for x, y in zip(A[1:], B[1:]):
            result += self.distance_of(last, Point(x, y))
            last = Point(x, y)
        return result
            
    def distance_of(self, left: Point, right: Point) -> int:
        return max(abs(left.x - right.x), abs(left.y - right.y))

