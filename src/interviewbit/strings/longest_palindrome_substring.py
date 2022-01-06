"""
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:

A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).


The main palindrome aspect for this problem is that, from the middle of it, both sides are the same
you can pick a mid spot and expand on both sides while valid


if smaller then two, return the string it self
iterate on the valid ranges
a range can be defined as an non inclusive interval (0,1) (0,2)

expand on valid spots
keep track of max size and max range


In - word: str
Out - str
"""
import dataclasses
from typing import List, Iterable


@dataclasses.dataclass
class Range:
    start: int
    end: int

    def get_size(self) -> int:
        return self.end - self.start - 1


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, word: str) -> str:
        if len(word) < 2:
            return word
        ranges: Iterable[Range] = self.find_mid_points(word)
        max_size: int = 1
        max_range: Range = Range(-1, 1)
        for interval in ranges:
            self.expand_interval(interval, word)
            if interval.get_size() > max_size:
                max_size = interval.get_size()
                max_range = interval
        return word[max_range.start + 1:max_range.end]

    def find_mid_points(self, word: str) -> Iterable[Range]:
        for i in range(len(word)-1):
            yield Range(i, i+1)
            # Restrict on the string size
            if i + 2 < len(word):
                yield Range(i, i+2)

    def expand_interval(self, interval: Range, word: str) -> None:
        while (interval.start >= 0 and interval.end < len(word)
               and word[interval.start] == word[interval.end]):
            interval.start -= 1
            interval.end += 1


