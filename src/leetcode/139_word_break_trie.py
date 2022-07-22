"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



 abookhaspages


has have page pages book a


iterate on the string looking to the substrings build from start to curr, if in the dictionary, call the recursion with start as the next position

Memoize on the start



O(n^2) time complexity where n is the size of the input n^2 from memoization 1 from the code inside the function
O(n) space complexity for the recursion stack


"""
import collections
import dataclasses
from typing import Any, List, Dict, Set, Tuple
import uuid


Cache = Dict[Tuple[str, int], bool]


@dataclasses.dataclass
class TrieNode:

    child: Dict[str, 'TrieNode'] = dataclasses.field(
        default_factory=lambda: collections.defaultdict(TrieNode)
    )
    key: str = dataclasses.field(default_factory=lambda: uuid.uuid4().hex)
    is_word: bool = False

    def insert(self, word: str) -> None:
        if not word:
            return
        curr: TrieNode = self
        for char in word:
            curr = curr.child[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr: TrieNode = self
        for char in word:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return curr.is_word


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        cache: Cache = dict()
        trie: TrieNode = build_trie(words)
        return self.can_break(s, trie, cache, 0, trie)

    def can_break(self, text: str, node: TrieNode, 
            cache: Cache, start: int, trie_root: TrieNode) -> bool:
        if (node.key, start) in cache:
            return cache[(node.key, start)]
        if node.is_word and (start >= len(text) or 
            self.can_break(text, trie_root, cache, start, trie_root)):
            return True
        if start >= len(text):
            return False
        curr: str = text[start]
        if curr not in node.child:
            cache[(node.key, start)] = False
            return False
        cache[(node.key, start)] = self.can_break(
            text, node.child[curr], 
            cache, start+1, trie_root
        )
        return cache[(node.key, start)]


def build_trie(words: List[str]) -> TrieNode:
    trie: TrieNode = TrieNode()
    for word in words:
        trie.insert(word)
    return trie
