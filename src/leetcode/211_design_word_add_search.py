"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


A trie feels like the best option
the . makes things a bit more expensive 

addition: normal trie insertion

search: if current char is a ., try all possible letters inserted on the trie


addition

O(n) time where n is the size of the word being inserted
O(n*m) space where n is size of word and m is the num of insertions

search 

O(26 ^ n) time complexity where n is the max size of word (you could have all dots)
O(n) space where n is the size of word (words case with recursion)


"""
from typing import Dict, Any


TrieNode = Dict[str, Any]


class WordDictionary:

    def __init__(self):
        self.trie: TrieNode = {'children': dict(), 
                               'is_word': False}

    def addWord(self, word: str) -> None:
        if not word:
            return
        self._add_word_helper(word, self.trie)

    def _add_word_helper(self, word: str, node: TrieNode) -> None:
        if not word:
            node['is_word'] = True
        curr: str = word[0]
        if curr not in node['children']:
            node['children'][curr] = {'children': dict(),
                                      'is_word': False}
        self._add_word_helper(word[1:], node['children'][curr])


    def search(self, word: str) -> bool:
        return self._search_helper(word, self.trie)

    def _search_helper(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node['is_word']
        curr: str = word[0]
        if curr == '.':
            for char in node['children']:
                if self._search_helper(
                    word[1:], node['children'][char]
                ):
                    return True
            return False
        if curr not in node['children']:
            return False
        return self._search_helper(word[1:], node['children'][curr])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

