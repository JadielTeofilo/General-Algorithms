"""
Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence of one or more dictionary words.

Input Format:

The first argument is a string, A.
The second argument is an array of strings, B.

Output Format:

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

In - text: str, word: List[str]

A = "myinterviewtrainer",

B = ["trainer", "my", "m", "interview"]


build a trie on the words inputed


traverse the text matching against the trie
stop when node is null 
    return true if the text is also empty, false otherwise
if curr node marked as a word, try recursing with the remaining chars from text from the trie root, if true return true, if not continue
try to match against the node, 
    if no match, go back to the root, if already on the root, return False
    if match, return the recursion with the remaining chars from text and the next node

text: str, start: int, node: TrieNode, trie_root: TrieNode

"""
from typing import List, Any, Dict


TrieNode = Dict[str, Any]


class Trie:

    def __init__(self):
        self.root: TrieNode = {'children': {}, 'is_word': False}

    def insert(self, word: str) -> None:
        if not word:
            return
        self._insert_helper(word, self.root)

    def _insert_helper(self, word: str, node: TrieNode) -> None:
        if not word:
            node['is_word'] = True
            return 
        curr_char: str = word[0]
        if curr_char not in node['children']:
            node['children'][curr_char] = {'children': {}, 
                                           'is_word': False}
        self._insert_helper(word[1:], node['children'][curr_char])


def build_trie(words: List[str]) -> Trie:
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)
    return trie


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, text: str, words: List[str]) -> int:
        trie: Trie = build_trie(words)
        return int(self.can_break_words(text, start=0, 
                                        node=trie.root, 
                                        trie_root=trie.root))

    def can_break_words(self, text: str, start: int, 
                        node: TrieNode, trie_root: TrieNode) -> bool:
        # a   a c
        if not text and node['is_word']:
            return True
        if not text or not node:
            return False
        if node['is_word']:
            attempt: bool = self.can_break_words(text, start, 
                                                 trie_root, trie_root)
            if attempt:
                return True
        if text[start] in node['chidren']:
            return self.can_break_words(
                text, start + 1, 
                node['children'][text[start]],
                trie_root
            )
        return False
"""
import sys
import uuid
sys.setrecursionlimit(50000)

class Trie():

    def __init__(self):
        self.root = {'children': {}, 'is_word': False, 'id': uuid.uuid1().hex}

    def insert(self, word):
        if (not word):
            return
        self._insert_helper(word, self.root)

    def _insert_helper(self, word, node):
        if (not word):
            node['is_word'] = True
            return
        curr_char = word[0]
        if (curr_char not in node['children']):
            node['children'][curr_char] = {'children': {}, 'is_word': False,
                                           'id': uuid.uuid1().hex}
        self._insert_helper(word[1:], node['children'][curr_char])

def build_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

class Solution():

    def wordBreak(self, text, words):
        trie = build_trie(words)
        self.cache = {}
        return int(self.can_break_words(text, start=0, node=trie.root, trie_root=trie.root))

    def can_break_words(self, text, start, node, trie_root):
        if ((start >= len(text)) and node['is_word']):
            return True
        if ((start >= len(text)) or (not node)):
            return False
        if (start, node['id']) in self.cache:
            return self.cache[(start, node['id'])]
        if node['is_word']:
            attempt = self.can_break_words(text, start, trie_root, trie_root)
            if attempt:
                self.cache[(start, node['id'])] = True
                return True
        if (text[start] in node['children']):
            self.cache[(start, node['id'])] = self.can_break_words(text, (start + 1), node['children'][text[start]], trie_root)
            return self.cache[(start, node['id'])]
        self.cache[(start, node['id'])] = False
        return False
"""
