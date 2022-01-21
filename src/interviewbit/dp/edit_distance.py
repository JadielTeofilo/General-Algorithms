"""
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character



In - left: str, right: str
Out - int
 

O(m * (m - n)!) where m is the size of right and n of left. This is so, cuz these are the diff ways that we can permutate starting from the string left 

aab

                            tg
1            ag              g           atg





if one of them ended, return the len diff
Just compare the first element, if equal, recurse on remaining
if diff 
try adding the right char
try removing the curr char
try replacing the curr char
cache the result



"""
from typing import Dict, Tuple
import math


Visited = Dict[Tuple[str, str], int]


class Solution:
    # @param A : string
    # @param B : string
    
    # @return an integer
    def minDistance(self, left: str, right: str) -> int:
        visited: Visited = dict()
        return self.get_min_distance(left, right, visited)

    def get_min_distance(self, left: str, right: str, 
                         visited: Visited) -> int:
        if (left, right) in visited:
            return visited[(left, right)]
        if not left or not right:
            return abs(len(left) - len(right))
        if left[0] == right[0]:
            visited[(left, right)] = self.get_min_distance(
                left[1:], right[1:], visited
            )
        else:
            visited[(left, right)] = min(
                1 + self.get_min_distance(left, right[1:], visited),
                1 + self.get_min_distance(left[1:], right, visited),
                1 + self.get_min_distance(left[1:], right[1:], visited),
            )
        return visited[(left, right)]
