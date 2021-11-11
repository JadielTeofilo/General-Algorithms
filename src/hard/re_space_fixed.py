"""
Re-Space: Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a
lengthy document. A sentence like "I reset the computer. It still didn`t boot!"
became"iresetthecomputeritstilldidntboot': You'll deal with the punctuation and capi-
talization later; right now you need to re-insert the spaces. Most of the words are in a 
dictionary but a few are not. Given a dictionary (a list of strings) and the 
document (a string), design an algorithm to unconcatenate the 
document in a way that minimizes the number of unrecognized characters.

In - document: str, dictionary: List[str]

string: iresetthecomputeritstilldidntboot

dictionary: reset it still boot thec computer

i reset thec [omputer] it still didnt boot
or
i reset [the] computer it still didnt boot


receive a string and test the different positions that a space can fit

loop i in string
	if substring not in words:
		invalid = len(substring)
	min_ = min(min_, invalid + solve(string[i+2:]))


Uses memoization to keep the time complexity at O(n^3) where n is the size of the document

"""
import collections
import math
from typing import List, Set, Union, Dict


SplitResult = collections.namedtuple('SplitResult', 'words invalid')
Cache = Dict[str, SplitResult]


def re_space(document: str, dictionary: List[str]) -> str:
	cache: Cache = {}
	split: SplitResult = split_words(document, set(dictionary), cache)
	return ' '.join(split.words)


def split_words(document: str, dictionary: Set[str], 
				cache: Cache) -> SplitResult:
	if not document:
		return SplitResult([], 0)
	if document in cache:
		return cache[document]
	min_invalids: Union[int, float] = math.inf
	words: List[str] = []
	for i in range(len(document)):
		curr_word: str = document[0:i+1]
		curr_splits: SplitResult = split_words(document[i+1:], dictionary, cache)
		curr_invalids: int = curr_splits.invalid
		if curr_word not in dictionary:
			curr_invalids += len(curr_word)
		if curr_invalids <= min_invalids:
			min_invalids = curr_invalids
			words = [curr_word] + curr_splits.words
	cache[document] = SplitResult(words, min_invalids)
	return cache[document]


print(re_space('ires', ['r', 're']))	
print(re_space('iresetthecomputeritstilldidntboot', ['reset', 'it', 'still', 'thec', 'computer', 'boot']))	
