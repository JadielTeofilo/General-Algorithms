"""
T9: On old cell phones, users typed on a numeric keypad and the phone would provide a list of words
that matched these numbers. 

Each digit mapped to a set of 0 - 4 letters. Implement an algorithm to return a list of matching words, given a sequence of digits. 

You are provided a list of valid words (provided in whatever data structure you'd like). The mapping is shown in the diagram below


In - valid_words: Trie, digits: str
Out- List[str]



						w
		a						h
		t					a
		e					t	
		r					


92837



O(4^n) time complexity where n is the size of the digits string
O(n) space, for the recursion where n is the size of digits




"""
from typing import List, Dict, Any, Iterable


TrieNode = Dict[str, Dict[str, Any]]


class Trie:

	def __init__(self) -> None:
		self.trie: TrieNode = {'': {'children': {}, 'is_word': False}}

	def insert(self, word: str) -> None:
		if not word:
			raise ValueError('Empty word')
		self._insert_helper(self.trie[''], word)
	
	def _insert_helper(self, node: Any, word: str) -> None:
		if not word:
			node['is_word'] = True
			return
		char: str = word[0]
		if not node['children'].get(char):
			node['children'][char] = {'children': {}, 'is_word': False}
		self._insert_helper(
			node['children'][char], word[1:]
		)
	

translation: Dict[str, List[str]] = {
	'1': [], 
	'2': ['a', 'b', 'c'],
	'3': ['d', 'e', 'f'],
	'4': ['g', 'h', 'i'],
	'5': ['j', 'k', 'l'],
	'6': ['m', 'n', 'o'],
	'7': ['p', 'q', 'r', 's'],
	'8': ['t', 'u', 'v'],
	'9': ['w', 'x', 'y', 'z'],
}


def find_possible_words(valid_words: Trie, 
						digits: str) -> Iterable[str]:
	""" From cellphone digit number, finds all valid 
		words that could be formed """
	return find_words_helper(valid_words.trie[''], digits, current=[])


def find_words_helper(valid_words: Any, digits: str,
					  current: List[str]) -> Iterable[str]:
	if not digits:
		if valid_words['is_word']:		
			yield ''.join(current)  # Turns the list into string
		return
	curr_digit: str = digits[0]
	for char in translation[curr_digit]:
		if not valid_words['children'].get(char):
			continue
		yield from find_words_helper(
			valid_words['children'][char], 
			digits[1:], 
			current + [char]
		)

asdf = Trie()
asdf.insert('water')
asdf.insert('will')
asdf.insert('weather')
asdf.insert('what')
asdf.insert('wimp')
print([a for a in find_possible_words(asdf, '9455')])
import pdb;pdb.set_trace()
