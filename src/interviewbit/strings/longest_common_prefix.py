"""
Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".

In - words: List[str]
Out - str


Get the len of min sized word
iterate on that
keep a result 
add to result if all are the same

O(m*n) time where m is the len of the smallest string and n is the len of words
"""
from typing import Optional, List


class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, words: List[str]) -> str:
        if not words:
            return ''
        min_len: int = self.get_min_len(words)
        result: List[str] = []
        for index in range(min_len):
            if not self.all_equal(words, index):
                break
            # Takes the tested char and add to result
            result.append(words[0][index])
        return ''.join(result)

    def get_min_len(self, words: List[str]) -> int:
        min_len: Optional[int] = None
        for word in words:
            if min_len is None:
                min_len = len(word)
            min_len = min(min_len, len(word))
        if not words:
            raise ValueError('Empty words')
        return int(min_len)

    def all_equal(self, words: List[str], index: int) -> bool:
        target_char: str = words[0][index]
        for word in words:
            if target_char != word[index]:
                return False
        return True

