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
Remember to ask if can reuse words

"""
import collections
from typing import Dict, Any, List, Optional


TrieNode = Dict[str, Any]
WordHit = collections.namedtuple('WordHit', 'start end word')


class Trie:

	def __init__(self) -> None:
		self.trie: TrieNode = {'children': {}, 'is_word': False}
	
	def insert(self, word: str) -> None:
		self._insert_helper(word, self.trie)

	def _insert_helper(self, word: str, node: TrieNode) -> None:
		if not word:
			node['is_word'] = True
			return
		target_char: str = word[0]
		if target_char not in node['children']:
			node['children'][target_char] = {'children': {}, 
											 'is_word': False}
		self._insert_helper(
			word[1:], node['children'][target_char]
		)


def re_space(document: str, dictionary: List[str]) -> str:
	""" Re inserts space on the document 
		using the dictionary 
	"""
	#TODO validate input
	trie: Trie = build_trie(dictionary) 
	split_words: List[str] = find_words(document, trie)
	return ' '.join(split_words)


def build_trie(words: List[str]) -> Trie:
	trie: Trie = Trie()
	for word in words:
		trie.insert(word)
	return trie


def find_words(document: str, trie: Trie) -> List[str]:
	""" 
		Iterates through the document findind 
		words according to the trie dictionary 
	"""
	doc_size: int = len(document)
	words: List[str] = []
	last_hit: WordHit = WordHit(start=-1, end=-1, word='')
	index: int = 0
	while index < len(document):
		hit: Optional[WordHit] = find_word(
			document, trie.trie, index
		)
		if hit:
			# fills misses in between hits
			fill_missing_word(document, hit, last_hit, words)
			words.append(hit.word)
			last_hit = hit
			index = hit.end + 1
			continue
		index += 1
	# Gets any missing word at the end
	empty_hit_at_end: WordHit = WordHit(doc_size, doc_size, '')
	fill_missing_word(document, empty_hit_at_end, last_hit, words)
	return words


def find_word(document: str, node: TrieNode, 
			  start: int) -> Optional[WordHit]:
	end: int = start
	# Finds if from 'start' its possible to find a valid 
	# word on the trie
	while end < len(document):
		if node['is_word']:
			return WordHit(start, end-1, document[start:end])
		target_char: str = document[end]
		if target_char in node['children']:
			node = node['children'][target_char]
			end += 1
		else:
			return
	if node['is_word']:
		return WordHit(start, end-1, document[start:end])

		
def fill_missing_word(document: str, curr_hit: WordHit, 
					  last_hit: WordHit, words: List[str]) -> None:
	# Case the last hit was not next to the start of the curr hit
	# adds the missing word in between
	if last_hit.end + 1 != curr_hit.start:
		words.append(document[last_hit.end + 1:curr_hit.start])


print(re_space('iresetthecomputeritstilldidntboot', ['reset', 'it', 'still', 'boot']))
