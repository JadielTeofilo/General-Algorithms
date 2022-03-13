"""
Given an integer A, how many structurally unique BST’s (binary search trees) exist that can store values 1…A?

Input Format:

The first and the only argument of input contains the integer, A.

Output Format:

Return an integer, representing the answer asked in problem statement.


In - number: int
Out - int

At a given node when you change from one value to another, the structure will always be different


3

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

                      first level [1,3]
    pick (0 left) 1 (2 right)

stops when end - start == 1 return 1
The recursion returns the num of ways given a list
solve(1, j-1)*solve(j+1, n)


"""
from typing import Dict, Tuple


class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, number: int) -> int:
        if number < 1:
            return 0
        cache: Dict[Tuple[int, int], int] = dict()
        return self.find_ways(start=1, end=number+1, cache=cache)
    
    def find_ways(self, start: int, end: int, 
                  cache: Dict[Tuple[int, int], int]) -> int:
        if end - start <= 1:  # Has size one
            return 1
        if (start, end) in cache:
            return cache[(start, end)]
        ways: int = 0
        for i in range(start, end):
            ways += (self.find_ways(start, i, cache) * 
                     self.find_ways(i+1, end, cache))
        cache[(start, end)] = ways
        return ways

