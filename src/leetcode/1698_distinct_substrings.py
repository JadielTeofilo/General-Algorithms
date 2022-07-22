"""
Given a string s, return the number of distinct substrings of s


iterate on the different substrings put them on a trie/hash (check if they already exist)

O(n^3) time complexity where n is the size of the input
O(n^3) worst case space complexity


iterate on the starting points
    iterate on the ending chars
        if not on trie, add it and add to answer

"""
import collections
import dataclasses
from typing import Dict


@dataclasses.dataclass
class TrieNode:

    child: Dict[str, 'TrieNode'] = dataclasses.field(
            default_factory=lambda: collections.defaultdict(TrieNode)
    )


class Solution:
    def countDistinct(self, s: str) -> int:
        trie: TrieNode = TrieNode()
        result: int = 0
        for start in range(len(s)):
            node: TrieNode = trie
            for end in range(start, len(s)):
                if s[end] not in node.child:
                    node = node.child[s[end]]
                    result += 1
        return result


