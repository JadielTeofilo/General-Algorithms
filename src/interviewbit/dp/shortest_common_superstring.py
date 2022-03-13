"""
Given a set of strings, A of length N.

Return the length of smallest string which has all the strings in the set as substring.


Input Format:

The first and the only argument has an array of strings, A.

Output Format:

Return an integer representing the minimum possible length of the resulting string.



"abcd" "cdef" "fgh" "de"

"abcdefgh"

"abc" "zea" "bcz"

abc
eabc
_
abc
zc
-

abc
zc


we need to test all the different ordering for merging
iterate from start to len
    merge to curr
    update min size as len_curr + solve(curr)
return min size

O(n^2*m*2^n) time complexity


"""
from typing import List


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, words: List[str]) -> int:
        cache: Dict[Tuple[str, str], int] = {}
        return find_min_size(words, start, cache, '', '1' * len(words))

    def find_min_size(self, words: List[str], cache: Dict[Tuple[str, str], int], 
                      curr: str, bitmap: str) -> int:
        if '1' not in bitmap:
            return 0
        if (curr, bitmap) in cache:
            return cache[bitmap]
        min_: int = 0
        for i in range(len(words)):
            if bitmap[i] == 0:
                continue
            aux_currs: List[str] = self.merge(curr, words[i])
            aux_bitmap: str = bitmap[:i] + '0' + bitmap[i+1:]
            for aux_curr in aux_currs:
                min_ = min(
                    min_, 
                    len(aux_curr) + self.find_min_size(words, cache, 
                                                       aux_curr, aux_bitmap)
                )
        cache[(curr, bitmap)] = min_
        return min_

    def merge(self, word: str, target: str) -> Iterable[str]:
        if target in word:
            yield word
        #TODO Two ways, merge beggining or end



