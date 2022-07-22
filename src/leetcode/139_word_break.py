"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



abookhaspages


has have page pages book a


iterate on the string looking to the substrings build from start to curr, if in the dictionary, call the recursion with start as the next position

Memoize on the start



O(n^3) time complexity where n is the size of the input n from memoization n^2 from the code inside the function
O(n) space complexityt for the recursion stack


"""
from typing import List, Dict, Set


Cache = Dict[int, bool]


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        cache: Cache = dict()
        return self.can_break(s, set(words), cache, 0)

    def can_break(self, text: str, words: Set[str], 
            cache: Cache, start: int) -> bool:
        if start >= len(text):
            return True
        if start in cache:
            return cache[start]
        for curr in range(start, len(text)):
            if (text[start:curr + 1] in words 
                and self.can_break(text, words, cache, curr + 1)):
                cache[start] = True
                return True
        cache[start] = False
        return False


