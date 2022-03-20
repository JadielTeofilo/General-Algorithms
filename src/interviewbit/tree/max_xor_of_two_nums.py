"""
Given two integer array A and B, you have to pick one element from each array such that their xor is maximum.

Return this maximum xor value.


2 1
5 3

build a trie for one of the list of nums, bit by bit
iterate on the second list and try to match with the trie using fliped bits
    try to get the oposit bit, if so add one to the local answer else add zero (bitwise)
    update result = max(result, answer)

O(n) time where n is the size of the biggest list (considering 32 bits)
O(n) space

"""
from typing import List, Any, Dict


TrieNode = Dict[str, Any]


def get_bit(number: int, bit: int) -> int:
    return int((1 << bit) & number != 0)


class Trie:

    def __init__(self) -> None:
        self.root: TrieNode = {'children': {}}
    
    def insert(self, number: int) -> None:
        self._insert_helper(number, self.root, 31)

    def _insert_helper(self, number: int, node: TrieNode, bit: int) -> None:
        if bit < 0:
            return
        curr: str = str(get_bit(number, bit))
        if curr not in node['children']:
            node['children'][curr] = {'children': {}}
        self._insert_helper(number, node['children'][curr], bit - 1)


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, first: List[int], second: List[int]) -> int:
        trie: Trie = self.build_trie(first)
        result: int = 0
        for num in second:
            result = max(result, self.get_max_xor(num, trie))
        return result

    def build_trie(self, numbers: List[int]) -> Trie:
        trie: Trie = Trie()
        for number in numbers:
            trie.insert(number)
        return trie

    def get_max_xor(self, num: int, trie: Trie) -> int:
        curr_num: int = 0
        node: TrieNode = trie.root
        for bit in range(31, -1, -1):
            curr_bit: str = str(get_bit(num, bit))
            expected: str = str(int(curr_bit) ^ 1)
            curr_num <<= 1
            if expected in node['children']:
                curr_num += 1
                node = node['children'][expected]
                continue
            node = node['children'][curr_bit]                
        return curr_num

