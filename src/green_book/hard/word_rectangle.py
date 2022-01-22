"""
Word Rectangle: Given a list of mill ions of words, design an
 algorithm to create the largest possible
rectangle of letters such that every row forms a word (reading left to right) and every column forms
a word (reading top to bottom). The words need not be chosen consecutively from the list, but all
rows must be the same length and all columns must be the same height.


In - words: List[str]
Out - matrix: List[str]

gouping by size will allow us to start from the bigger words

Put the group of same sized words on a trie

use recursion to build a tree of possibilities attempting different orders of same sized words
at each level we add a row. The row is chosen among the same size input words that keep valid all columns. Each element of the matrix will have a pointer to the place in the trie that it is at



"""
import collections
from typing import List, Dict, Any


CharData = collections.namedtuple('CharData', 'char trie_node')
Matrix = List[List[CharData]]
TrieNode = Dict[str, Any]


class Trie:
	
	def __init__(self) -> None:
		self.trie: TrieNode = {'children': {}, 'is_word': False}
	
	def insert(self, word: str) -> None:
		if not word: 
			raise ValueError('Empty input')
		self._insert(word, self.trie)

	def _insert(self, word: str, node: TrieNode) -> None:
		if not word: 
			node['is_word'] = True
			return
		curr_char: str = word[0]
		if curr_char not in node['children']: 
			node['children'][curr_char] = {'children': {}, 
										   'is_word': False}
		return self._insert(word[1:], node['children'][curr_char])



def word_rectangle(words: List[str]) -> List[str]:
	# TODO validate input
	grouped_words: Dict[int, List[str]] = group_by_size(words)
	keys_sorted_desc: List[int] = sorted(list(grouped_words.keys()), 
										 reverse=True)
	# TODO make it so that for each row size, try all possible column sizes
	for word_size in keys_sorted_desc:
		same_size_words: List[str] = grouped_words[word_size]
		trie: Trie = build_trie(same_size_words)
		rectangle: List[str] = build_rectangle(same_size_words, trie)
		if rectangle:
			return rectangle
	raise ValueError('Not possible to make rectangle with given words')


def group_by_size(words: List[str]) -> Dict[int, List[str]]:
	result: Dict[int, List[str]] = collections.defaultdict(list)
	for word in words:
		result[len(word)].append(word)
	return result


def build_trie(words: List[str]) -> Trie:
	trie: Trie = Trie()
	for word in words:
		trie.insert(word)
	return trie


def build_rectangle(words: List[str], trie: Trie) -> List[str]:
	size: int = len(words[0])
	matrix: Matrix = [[CharData(None, None)] * size	for _ in range(size)]
	return build_rectangle_helper(words, matrix, trie.trie)


def build_rectangle_helper(words: List[str], matrix: Matrix, 
						   trie_root: TrieNode, row=0) -> List[str]:
	if not words:
		return []
	if row + 1 == len(matrix):
		if not are_valid_columns(matrix):
			return []
		return [''.join([data.char for data in row]) for row in matrix]
	
	for index, word in enumerate(words):
		if not check_for_valid_word(word, matrix, row):
			continue
		new_matrix: Matrix = copy_matrix(matrix)
		add_to_row(new_matrix, row, word, trie_root)
		rectangle: List[str] = build_rectangle_helper(
			words[:index] + words[index + 1:], 
   		    new_matrix, trie_root, row + 1
		)
		if rectangle:
			return rectangle
	return []


def are_valid_columns(matrix: Matrix) -> bool:
	"""
		Checks to see if at every column the last 
		item makes up a word
	"""
	for char_data in matrix[-1]:
		if not char_data.trie_node or not char_data.trie_node['is_word']:
			return False
	return True


def check_for_valid_word(word: str, matrix: Matrix, row: int) -> bool:
	if row == 0:
		return True  # If empty matrix any word is valid
	last_row: int = row - 1
	for word_char, last_char_data in zip(word, matrix[last_row]):
		if (last_char_data.trie_node and 
			word_char not in last_char_data.trie_node['children']):
			return False
	return True
	
	
def copy_matrix(matrix: Matrix) -> Matrix:
	return [row.copy() for row in matrix]
	

def add_to_row(matrix: Matrix, row: int, word: str, 
			   trie_root: TrieNode) -> None:
	for i, (char, last_data) in enumerate(zip(word, matrix[row - 1])):
		if row == 0:
			node: TrieNode = trie_root['children'].get(char)
		else:
			node: TrieNode = last_data.trie_node['children'].get(char)
		matrix[row][i] = CharData(char, node)

print(word_rectangle([
'bo',
'al',
'ba',
'ab',
'ay',
'ol',
'aa',]
))
import pdb;pdb.set_trace()
