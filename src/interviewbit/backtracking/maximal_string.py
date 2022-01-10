"""
Problem Description

Given a string A and integer B, what is maximal lexicographical string that can be made from A if you do atmost B swaps.

In - word: str, swaps: int
out - word


abcd

dcba
3210

dabc

dcab

dcba


sort in reversed order, keeping track of original indexes
iterate on the reversed string, until `swap` elements, keeping a `deleted indexes` set
iterate on the string adding elements not in the deleted set

O(nlogn) time complexity n being the size of the string
O(n) space complexity 


"""
import collections
from typing import List, Set


WordValue = collections.namedtuple('WordValue', 'char original_index')


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, word: str, swaps: int) -> str:
        inverted: List[WordValue] = sorted(self.get_values(word), 
                                           reverse=True)
        result: List[str] = []
        deleted_indexes: Set[int] = set()
        for index in range(swaps):
            result.append(inverted[index].char)
            deleted_indexes.add(inverted[index].original_index)
        for index, char in enumerate(word):
            if index in deleted_indexes:
                continue
            result.append(char)
        return ''.join(result)

    def get_values(self, word: str) -> List[WordValue]:
        return [WordValue(char, index) 
                for index, char in enumerate(word)]



