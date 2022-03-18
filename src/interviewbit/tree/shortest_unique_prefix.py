"""
Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov

    NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.


Build a trie where we keep a count of the number of words that use each node

keep a children ordered list so we know the order of the children to traverse

Iterate on it on the right order keeping the current word formed
    yield and return whenever ynu see a 1 on the counter


O(n*m) time and space where m is the size of the biggest string and n the num of strings
O(m*n) space

In - words: List[str]
Out - List[str]

"""
from typing import Dict, Any, List, Iterable, Optional


TrieNode = Dict[str, Any]


class Trie:
    
    def __init__(self) -> None:
        self.root: TrieNode = {'children': {}, 'full_word': '', 
                               'count': 0, 'root': True}
    
    def insert(self, word: str) -> None:
        if not word:
            return
        self._insert_helper(word, self.root, original=word)
    
    def _insert_helper(self, word: str, node: TrieNode, 
                       original: str) -> None:
        node['count'] += 1
        node['full_word'] = original
        if not word:
            return
        curr: str = word[:1]
        if curr not in node['children']:
            node['children'][curr] = {'children': {}, 'ordered': {}, 
                                      'count': 0}
        self._insert_helper(word[1:], node['children'][curr], original)

    def get_shortest_unique(self) -> Dict[str, str]:
        equivalency: Dict[str, str] = {}
        self._shortest_unique_helper(self.root, curr='', eq=equivalency)
        return equivalency

    def _shortest_unique_helper(
        self, node: Optional[TrieNode], 
        curr: str, eq: Dict[str, str],
    ) -> None:
        if not node:
            return
        if node['count'] == 1 and not node.get('root'):
            eq[node['full_word']] = curr
            return
        for char in node['children']:
            self._shortest_unique_helper(
                node['children'][char], curr + char, eq
            )


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, words: List[str]) -> Iterable[str]:
        trie: Trie = self.build_trie(words)
        equivalency: Dict[str, str] = trie.get_shortest_unique()
        for word in words:
            yield equivalency[word]
    
    def build_trie(self, words: List[str]) -> Trie:
        trie: Trie = Trie()
        for word in words:
            trie.insert(word)
        return trie
