"""
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "baroothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].

(order does not matter).

trie

        f           b
        o           a
        o           r

In - words: List[str], text: str
Out - List[int]

build trie
itearte on text
    when first match is found call the recursion to see if it is a match
        if match, continue from curr + len(sum(words)) else
    matched_words: Dict[str, count]
    look for match
    if word is not fully matched go back to root and reset matched_words and counter_matched
    after a full word match, mark it as matched, and add one to counter of matched words
    if counter equals len(words) add start position to result

"""
import collections
from typing import Any, Dict, List


TrieNode = Dict[str, Any]

class Trie:

    def __init__(self) -> None:
        self.root: TrieNode = {'children': {}, 'count': 0}

    def insert(self, word: str) -> None:
        if not word:
            return
        self.root = self._insert_helper(self.root, word)

    def _insert_helper(self, node: TrieNode, 
                       word: str) -> TrieNode:
        if not word:
            node['count'] += 1
            return node
        curr_char: str = word[0]
        if not curr_char in node['children']:
            node['children'][curr_char] = {'children': {}, 'count': 0}
        self._insert_helper(node['children'][curr_char],
                            word[1:])
        return node


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, text: str, words: List[str]) -> List[int]:
        trie: Trie = self.build_trie(words)
        words_full_size: int = len(''.join(words))
        trie_root: TrieNode = trie.root
        result: List[int] = []
        for index, char in enumerate(text):
            if char not in trie_root['children']:
                continue
            matched_words: Dict[str, int] = collections.defaultdict(int)
            match: bool = self.look_for_words(
                text[index:words_full_size],
                len(words), trie_root, trie_root,
                matched_words, count_matched={'val': 0},
                curr_word='',
            )
            if match:
                result.append(index)
        return result

    def look_for_words(self, text: str, words_len: int, node: TrieNode, 
            trie_root: TrieNode, matched_words: Dict[str, int],
            count_matched: Dict[str, int], curr_word: str) -> bool:
        if words_len == count_matched['val']:
            return True
        if node['count'] > 0:
            # Case we matched more of the same word then 
            # there is on the words list
            if matched_words[curr_word] >= node['count']:
                return False
            count_matched['val'] += 1
            matched_words[curr_word] += 1
            return self.look_for_words(
                text, words_len, trie_root, trie_root,
                matched_words, count_matched, ''
            ) 
        if not text:
            return False
        if text[0] not in node['children']:
            return False
        return self.look_for_words(
            text[1:], words_len, node['children'][text[0]],
            trie_root, matched_words, count_matched, 
            curr_word + text[0],
        )

    def build_trie(self, words: List[str]) -> Trie:
        trie: Trie = Trie()
        for word in words: 
            trie.insert(word)
        return trie








