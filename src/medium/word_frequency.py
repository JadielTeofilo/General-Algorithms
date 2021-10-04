"""
Word Frequencies: Design a method to find the frequency of occurrences of any given word in a
book. What if we were running this algorithm multiple times?

In - book: str, word: str
Out - int

BCR = O(n*m) n being the number of words of the book m being the letters on a word

If running only once, go through the words on the book and count occurrences. 
.count() on python 

We are talking exact matches right?
yes, but what if it was till edit distance of 1

Is it just words or could it be sentences?
just words


If running more than once, build a trie for the book every node being a letter 
The first indexing will take O(n*m) n being the number of words and m the max amount of letters
The rest will be O(m)


'table'
'the book is on the table, and the table has turned.'



"""
from typing import Dict, Iterable, Union, Any
import re


TrieNode = Dict[str, Dict[str, Any]]


class Trie:
	
	def __init__(self) -> None:
		self.trie: TrieNode = {'': {'children': {}, 'count': 0}}

	def insert(self, word: str) -> None:
		self._insert_helper(self.trie[''], word)

	def _insert_helper(self, node: Any, 
					   word: str) -> None:
		if not word:
			node['count'] += 1
			return
		curr_char: str = word[0]
		if not node['children'].get(curr_char):
			# Initialize empty node
			node['children'][curr_char] = {'children': {}, 
											'count': 0}
		return self._insert_helper(
			node['children'][curr_char], word[1:]
		)
		
	def search(self, word: str) -> int:
		""" Finds the number of 
			occurencies of word 
		"""
		return self._search_helper(self.trie[''], word)

	def _search_helper(self, node: Any, word: str) -> int:
		if not word:
			return node['count']
		curr_char: str = word[0]
		if not node['children'].get(curr_char):
			raise ValueError('Word not present')
		return self._search_helper(
			node['children'][curr_char], word[1:]
		)



class FrequencyFinder:
	
	def __init__(self, book: str) -> None:
		self.book = book
		self.trie: Trie = Trie()
		self.build_trie()

	def build_trie(self) -> None:
		words: Iterable[str] = self._get_words_from_book()
		for word in words:
			self.trie.insert(word)

	def word_frequency(self, word: str) -> int:
		"""
			Finds the frequency of the requested word,
			It is case sensitive
		"""
		return self.trie.search(word)

	def _get_words_from_book(self) -> Iterable[str]:
		return re.findall('[a-zA-Z]+', self.book)



asdf = FrequencyFinder('the book is on the table, and the table has turned')

import pdb;pdb.set_trace()	




