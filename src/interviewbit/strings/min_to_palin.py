"""
Given an string A. The only operation allowed is to insert  characters in the beginning of the string.
Find how many minimum characters are needed to be inserted to make the string a palindrome string.

Input Format

The only argument given is string A.

Output Format

Return the minimum characters that are needed to be inserted to make the string a palindrome string.

In - word: str
Out - int

a
aba
abba

0 - n
cdbc
cbdc
0001

reverse the word
search the original string in the reversed
KMP
LPS
if there is a full match, return 0
when the the reversed word ends, return the remaining on the original

O(n) time complexity where n is the size of the word
O(n) space complexity where n is the size of the word
"""
from typing import List


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, word: str) -> int:
        inverted: str = word[::-1]
        lps: List[int] = self.get_lps(word) 
        left, right = 0, 0
        while right < len(inverted) and left < len(word):
            if word[left] == inverted[right]:
                left += 1
                right += 1
            elif left == 0:
                right += 1
            else:
                left = max(0, lps[left] - 1)
        return len(word) - left

    def get_lps(self, word: str) -> List[int]:
        lps: List[int] = [0] * len(word)
        left, right = 0, 1
        while right < len(word):
            if word[left] == word[right]:
                lps[right] = lps[right - 1] + 1
                left += 1
            else:
                while word[left] != word[right] and left > 0:
                    left -= 1
            right += 1
        return lps
                


