"""
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.


Input Format:

The first and the only argument contains the string A.

Output Format:

Return an integer, representing the answer as described in the problem statement.


In - word: str
Out - int


build all valid subarrays
iterate i from start
validate start:i+1
min (1 + solve(i+1), min_)1


ab

O(n^3) time where n is the size of the input
O(n^2) space depth n with n usage inside


"""
import math
from typing import Dict, Union


class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, word: str) -> Union[int, float]:
        cache: Dict[int, Union[int, float]] = {}
        return self.find_min(start=0, word=word, cache=cache)

    def find_min(self, word: str, start: int, 
                 cache: Dict[int, Union[float, int]]) -> Union[int, float]:
        if start >= len(word) - 1:
            return 0
        if start in cache: 
            return cache[start]
        min_: Union[int, float] = math.inf
        for i in range(start, len(word)):
            if not self.is_palindrome(word[start:i + 1]):
                continue
            split: int = 1 if i + 1 < len(word) else 0 
            min_ = min(min_, split + self.find_min(word, i + 1, cache))
        cache[start] = min_
        return cache[start]

    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

