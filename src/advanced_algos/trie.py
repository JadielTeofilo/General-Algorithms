"""

Trie implementation


"""
import collections
import uuid


class TrieNode:

    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = collections.defaultdict(
            TrieNode
        )
        self.key: str = uuid.uuid4().hex
        self.is_word: bool = False


    def insert(self, word: str) -> None:
        if not word: 
            return
        curr: 'TrieNode' = self
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr: 'TrieNode' = self
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word



