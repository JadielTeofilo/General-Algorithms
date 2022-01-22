"""
Longest Word: Given a list of words, write a program to find the longest word made of other words
in the list.

In - words: List[str]
Out - str


"""
from typing import List, Dict, Any, Optional


TrieNode = Dict[str, Any]


class Trie:

    def __init__(self) -> None: 
        self.trie: TrieNode = {'children': {}, 'count': 0}

    def insert(self, word: str) -> None:
        if not word:
            return
        self._insert_helper(word, self.trie)

    def _insert_helper(self, word: str, trie_node: TrieNode) -> None:
        if not word:
            trie_node['count'] += 1
            return
        target_char: str = word[0]
        if target_char not in trie_node['children']:
            trie_node['children'][target_char] = {'children': {}, 'count': 0}
        return self._insert_helper(
            word[1:], 
            trie_node['children'][target_char]
        )

    def remove(self, word: str) -> None:
        if not word: 
            return
        self._remove_helper(word, self.trie)

    def _remove_helper(self, word, trie_node: TrieNode) -> None:
        if not word:
            trie_node['count'] -= 1
            return
        target_char: str = word[0]
        if target_char not in trie_node['children']:
            return
        self._remove_helper(word[1:], trie_node['children'][target_char])


def longest_word(words: List[str]) -> Optional[str]:
    # TODO check input
    # Sorts by size and revert to have bigger 
    # str at beginning
    words.sort(key=lambda x: len(x))
    words.reverse()
    trie: Trie = build_trie(words)
    for word in words:
        trie.remove(word)
        if is_made_of_other_words(word, trie.trie, trie.trie):
            return word
        trie.insert(word)
    return None


def build_trie(words: List[str]) -> Trie:
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)
    return trie


def is_made_of_other_words(word: str, trie_node: TrieNode, 
                           root: TrieNode) -> bool:
    if not word:
        return trie_node['count'] >= 1
    if (trie_node['count'] >= 1 and
        is_made_of_other_words(word, root, root)):
        return True
    target_char: str = word[0]
    if target_char not in trie_node['children']:
        return False
    return is_made_of_other_words(
        word[1:], 
        trie_node['children'][target_char], 
        root
    )


import pdb;pdb.set_trace()
print(longest_word(['a', 'b', 'abca', 'aba', 'ab', 'bc', 'xmajqa']))
