"""
Re-Space: Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a
lengthy document. A sentence like "I reset the computer. It still didn`t boot!"
became"iresetthecomputeritstilldidntboot': You'll deal with the punctuation and capi-
talization later; right now you need to re-insert the spaces. Most of the words are in a 
dictionary but a few are not. Given a dictionary (a list of strings) and the 
document (a string), design an algorithm to unconcatenate the 
document in a way that minimizes the number of unrecognized characters.

In - document: str, dictionary: List[str]

iresetthecomputeritstilldidntboot

reset it still boot 

i reset thecomputer it still didnt boot


A trie does the trick 

fill a trie with the dictionary

find the start and end indexes of the words

"""
import collections
from typing import Dict, Any, List, Optional


TrieNode = Dict[str, Any]
WordHit = collections.namedtuple('WordHit', 'start end word')


class Trie:

	def __init__(self) -> None:
		self.trie: TrieNode = {'children': {}, 'is_word': False}
	
	def insert(self, word: str) -> None:
		# TODO


def re_space(document: str, dictionary: List[str]) -> str:
	""" Re inserts space on the document 
		using the dictionary 
	"""
	#TODO validate input
	trie: Trie = build_trie(dictionary)  # TODO
	split_words: List[str] = find_words(document, trie)  #TODO
	return ' '.join(split_words)


def find_words(document: str, trie: Trie) -> List[str]:
	""" 
		Iterates through the document findind 
		words according to the trie dictionary 
	"""
	words: List[str] = []
	word_start: int = 0
	last_start: int = 0
	index: int = 0
	while index < len(document):
		hit: Optional[WordHit] = find_word(
			document, trie, index
		)  # TODO
		if hit:
			# TODO
		index += 1

	# TODO handle the unmatched rest of the string
		
	


	
