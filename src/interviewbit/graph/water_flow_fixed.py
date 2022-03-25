"""
Given an N x M matrix A of non-negative integers representing the height of each unit cell in a continent, the "Blue lake" touches the left and top edges of the matrix and the "Red lake" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the number of cells from where water can flow to both the Blue and Red lake.

 Blue Lake ~   ~   ~   ~   ~ 
        ~  1   2   2   3  (5) *
        ~  3   2   3  (4) (4) *
        ~  2   4  (5)  3   1  *
        ~ (6) (7)  1   4   5  *
        ~ (5)  1   1   2   4  *
           *   *   *   *   * Red Lake

 Water can flow to both lakes from the cells denoted in parentheses.



The goal is to find nodes that have edges that reach both sides
brute force is to do bfs from every node and check if it reaches both the sides

Think of flood from the ocean = bidirectional search
w do the inverse, start from borders and mark the matrix with blues and reds, keeping track of visited

add first row and col to queue
add last row and col to queue_2

call the following once with the queue1, other=visited_2 and then queue_2, other=visited1
insidewhile
    pop from queue
    if visited, skip
    add to visited
    check if in the other visited, add one to result
    add to queue the neighbors


have one visited for each
do a bidirectional search
adding one when visited of one is on the other




O(n*m) time complexity where row= n col=m
O(n*m) space

"""
import dataclasses
from typing import List, Tuple

Matrix = List[List[int]]


@dataclasses.dataclass
class Reach:
    blue: bool = False
    red: bool = False


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, matrix: Matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
