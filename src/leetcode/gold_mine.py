"""

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position, you can walk one step to the left, right, up, or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.


"""


import collections
from typing import List, Dict, Iterable, Set, Tuple

Node = collections.namedtuple('Node', 'row col')
Cache = Dict[Tuple[Node, Node], int]
"""


[
[0, 0, 19,5,8],
[11,20,14,1,0],
[0, 0, 1, 1,1],
[0, 2, 0, 2,0]]

"""

class Solution:
    def getMaximumGold(self, mine: List[List[int]]) -> int:
        cache: Dict[Node, int] = {}
        max_: int = 0
        if not mine:
            return 0
        for node in self.get_positions(mine):
            visited: Set[Node] = set()
            max_ = max(max_, self.find_max(mine, node, visited))
        return max_

    def find_max(self, mine: List[List[int]], node: Node, visited: Set[Node]) -> int:
        if mine[node.row][node.col] == 0:
            return 0
        if node in visited:
            return cache[(start, node)]
        visited.add(node)
        max_: int = 0
        for neighbor in self.get_neighbors(mine, node):
            max_ = max(self.find_max(mine, neighbor, visited), max_)
        visited.discard(node)
        return max_ + mine[node.row][node.col]

    def get_positions(self, mine: List[List[int]]) -> Iterable[Node]:
        for row in range(len(mine)):
            for col in range(len(mine[0])):
                yield Node(row, col)
                
    def get_neighbors(self, mine: List[List[int]], node: Node) -> Iterable[Node]:
        positions: List[Node] = [
            Node(node.row + 1, node.col),
            Node(node.row, node.col + 1),
            Node(node.row - 1, node.col),
            Node(node.row, node.col - 1),
        ]
        for position in positions:
            if self.is_valid(mine, position):
                yield position
    
    def is_valid(self, mine: List[List[int]], position: Node) -> bool:
        if (position.row < 0 or position.col < 0 or
            position.row >= len(mine) or position.col >= len(mine[0])):
            return False
        return True

asdf = Solution()
qwer = [
[0, 0, 19,5,8],
[11,20,14,1,0],
[0, 0, 1, 1,1],
[0, 2, 0, 2,0]]
qwer = [
[0, 0, 20,4,8],
[ 5,20,20,1,0],
[0, 0, 1, 1,1],
[0, 2, 0, 2,0]]
asdf.getMaximumGold(qwer)
