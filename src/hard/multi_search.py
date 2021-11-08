"""
17.17 Multi Search: Given a string b and an array of smaller strings T, design a method to search b for
each small string in T.

In - text: str, words: List[str]
Out - List[str]


lgget`s go to the party tonight?
['go', 'test', 'jump']

return ['go']

O(k^2 + n*t) time complexity, where k is the size of text, n is the size of words, and t is the size of the biggest word

O(k^2) space complexity

"""
from typing import Dict, Any, List


TrieNode = Dict[str, Any]


class Trie:

    def __init__(self) -> None:
        self.trie: TrieNode = {'children': {}}

    def insert(self, word: str) -> None:
        if not word:
            return
        self._insert_helper(word, self.trie)

    def _insert_helper(self, word: str, node: TrieNode) -> None:
        if not word:
            return
        target_char: str = word[0]
        if target_char not in node['children']:
            node['children'][target_char] = {'children': {}}
        return self._insert_helper(
            word[1:], 
            node['children'][target_char],
        )

    def search(self, word: str) -> bool:
        if not word: 
            raise ValueError('Empty input')
        return self._search_helper(word, self.trie)

    def _search_helper(self, word: str, node: TrieNode) -> bool:
        if not word:
            return True
        target_char: str = word[0]
        if target_char not in node['children']:
            return False
        return self._search_helper(
            word[1:],
            node['children'][target_char],
        )


def multi_search(text: str, words: List[str]) -> List[str]:
    # TODO validate input
    trie: Trie = build_trie(text)
    result: List[str] = []
    for word in words:
        if trie.search(word):
            result.append(word)
    return result


def build_trie(text: str) -> Trie:
    """
        Inserts all possible substrings on the trie
    """
    trie: Trie = Trie()
    for i in range(len(text)):
        trie.insert(text[i:])
    return trie


print(multi_search('lgget`s go to the party tonight?', ['go', 'test', 'jump']))
