"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


build a trie with the input words

try every starting position keeping track of visited 
when we find a word we remove it from the trie



O(N*(4*3^(W-1))) time complexity 4 branches in the first iteration, then 3 branches thought W (max size of a word)

Branches ^ depth

O(W*N) for the worst case on the trie


"""
import collections
from typing import List, Dict, Set


Position = collections.namedtuple('Position', 'row col')
Matrix = List[List[str]]


class TrieNode:

    def __init__(self) -> None:
        self.children: Dict[str, 'TrieNode'] = collections.defaultdict(
            TrieNode
        )
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        if not word:
            return
        curr: 'TrieNode' = self
        for char in word:
            curr = curr.children[char]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie: TrieNode = build_trie(words)
        result: List[str] = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited: Set[Position] = set()
                find_words(board, Position(row, col), trie, visited, result, [])
        return result


def build_trie(words: List[str]) -> TrieNode:
    trie: TrieNode = TrieNode()
    for word in words:
        trie.insert(word)
    return trie


def find_words(board: Matrix, start: Position, trie: TrieNode, visited: Set[Position],
              result: List[str], curr_word: List[str]) -> None:
    curr_char: str = board[start.row][start.col]
    if (start in visited or
            curr_char not in trie.children):
        return
    visited.add(start)
    curr_word.append(curr_char)
    next_node: TrieNode = trie.children[curr_char]
    if next_node.is_word:
        result.append(''.join(curr_word))
        next_node.is_word = False
        # Removes the node it its a leaf
        if not next_node.children:
            trie.children.pop(curr_char)
    for neighbor in get_valid_neighbors(start, board):
        find_words(board, neighbor, next_node, visited, result, curr_word)
    visited.remove(start)
    curr_word.pop()


def get_valid_neighbors(start: Position, board: Matrix) -> Iterator[Position]:
    for row, col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        curr_row: int = start.row + row
        curr_col: int = start.col + col
        if 0 <= curr_row < len(board) and 0 <= curr_col < len(board[0]):
            yield Position(curr_row, curr_col)


