"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

    For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.


Input: words = 
"a","b","ba","bca","bda","bdca"
 4   4    3    2     2     1 

dca bca bda bdc -> 1
ba da bd -> 2
bc ba ca -> 2

b
d
c  a
a


O(n^2*m) m = string size, n=num strings

Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].


the size metters -> has to be smaller by one

sort by size

O(nlogn + n * m) where n is the num of strings, m is the max size of them

"""
from typing import Iterator, Dict, List


def build_variations(word: str) -> Iterator[str]:
    for i in range(len(word)):
        yield word[:i] + word[i + 1:]


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        dp: Dict[str, int] = {}
        result: int = 1
        for index, word in enumerate(words):
            curr: int = dp.get(word, 1)
            for variation in build_variations(word):
                dp[variation] = max(curr, dp.get(variation, 1))
                result = max(result, dp[variation])
        return result


            

