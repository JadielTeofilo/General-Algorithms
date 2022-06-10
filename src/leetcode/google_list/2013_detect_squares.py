"""
You are given a stream of points on the X-Y plane. Design an algorithm that:

    Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
    Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

    DetectSquares() Initializes the object with an empty data structure.
    void add(int[] point) Adds a new point point = [x, y] to the data structure.
    int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.



1, 2


4

3     

2     -  -

1  -  -  -

0  1  2  3  4 



for the query point, find points that make a line of 45degree

abs(p1.x - p2.x) == abs(p1.y - p2.y)

if that is true we can check if the other two maching points exist

have a dict counter for the points, 

Check if 


O(P) time complexity for the count
O(1) time for the add
O(P) space complexity



"""
import collections
from typing import List, Dict


Point = collections.namedtuple('Point', 'x y')


class DetectSquares:

    def __init__(self):
        self.points: Dict[Point, int] = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[Point(*point)] += 1

    def count(self, point: List[int]) -> int:
        curr: Point = Point(*point)
        result: int = 0
        for x, y in self.points:
            if x == curr.x or abs(x - curr.x) != abs(y - curr.y):
                continue
            result += (
                self.points.get((x, y), 0) * 
                self.points.get((curr.x, y), 0) *
                self.points.get((x, curr.y), 0)
            )
        return result



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
