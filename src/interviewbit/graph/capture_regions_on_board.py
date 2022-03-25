"""
Given a 2D character matrix A of size N x M, containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.


Input 1:

 A = [  [X, X, X, X],
        [X, O, O, X],
        [X, X, O, X],
        [X, O, X, X]
     ]



Example Output

Output 1:

 A = [  [X, X, X, X],
        [X, X, X, X],
        [X, X, X, X],
        [X, O, X, X]
     ]


[ 
"XOXXXXOOXX", 
"XOOOOXOOXX", 
"OXXOOXXXOO", 
"OXOXOOOXXO", 
"OXOOXXOOXX", 
"OXXXOXXOXO", 
"OOXXXXOXOO" ]


Build two matrices, one that tells if you can reach top or left from current
the other tells if you can reach bottom or right from current

Iterate on them both, if cant reach neigther, make it X


The better option is to came from the outside, save on a set the spots that can be reached from the outside. 

BFS, add to queue all the elements from the border that are O

pop from queue
if visited continue
add to list of outsiders
add to visited
add all neighbors

iterate on all, if not visited, put X

O(N) time where N is the number of nodes
O(N) space cuz of queue

"""
import collections
from typing import List, Deque, Set, Iterable


Matrix = List[List[str]]
Place = collections.namedtuple('Place', 'row col')


class Solution:
    # @param A : list of list of chars
    def solve(self, matrix: Matrix) -> None:
        border: Iterable[Place] = self.get_border(matrix, match='O')
        deque: Deque[Place] = collections.deque(border)
        visited: Set[Place] = set()
        while deque:
            curr: Place = deque.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in self.get_neighbors(curr, matrix, match='O'): 
                deque.append(neighbor)
        self.update_matrix(matrix, visited)

    def update_matrix(self, matrix: Matrix, visited: Set[Place]) -> None:
        for row, col in self.get_places(matrix): 
            if (row, col) not in visited:
                matrix[row][col] = 'X'

    def get_places(self, matrix: Matrix) -> Iterable[Place]:
        if not matrix or not matrix[0]:
            return []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                yield Place(row, col)

    def get_border(self, matrix: Matrix, match: str) -> Iterable[Place]:
        for row, col in self.get_places(matrix):
            if ((row == 0 or col == 0 or 
                 col == len(matrix[0]) - 1 or 
                 row == len(matrix) - 1) and 
                matrix[row][col] == match):
                yield Place(row, col)

    def get_neighbors(self, place: Place, matrix: Matrix, 
                      match: str) -> Iterable[Place]:
        spots: List[Place] = [
            Place(place.row + 1, place.col),
            Place(place.row - 1, place.col),
            Place(place.row, place.col + 1),
            Place(place.row, place.col - 1),
        ]
        for spot in spots:
            if (self.is_valid(spot, matrix) and 
                matrix[spot.row][spot.col] == match):
                yield spot

    def is_valid(self, place: Place, matrix: Matrix) -> bool:
        return (not (place.row < 0 or place.col < 0 
                     or place.row > len(matrix) - 1 
                     or place.col > len(matrix[0]) - 1))

        




