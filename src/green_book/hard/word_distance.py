"""
Word Distance: You have a large text file containing words. Given any two words, find the shortest
distance (in terms of number of words) between them in the file. If the operation will be repeated
many times for the same file (but different pairs of words), can you optimize your solution?


In - words: List[str]
Out - int


"""
import collections
import math
from typing import Dict, List, Union


def word_distance(words: List[str], first: str, second: str) -> int:
	cache: Dict[str, List[int]] = build_cache(words) 
	return find_distance(cache, first, second) 


def find_distance(cache: Dict[str, List[int]], 
				  first: str, second: str) -> int:
	if first not in cache or second not in cache: 
		raise ValueError('Word not on text')
	first_hits: List[int] = cache[first]
	second_hits: List[int] = cache[second]
	i, j = 0, 0
	distance: Union[int, float] = math.inf
	while True:
		distance = min(abs(first_hits[i] - second_hits[j]), distance)
		# Case that both lists got to an end
		if i == len(first_hits) - 1 and j == len(second_hits) - 1:
			break
		if first_hits[i] < second_hits[j]:
			if i < len(first_hits) - 1:
				i += 1
			else:
				j += 1
		else:
			if j < len(second_hits) - 1:
				j += 1
			else:
				i += 1
	return int(distance) 
	

def build_cache(words: List[str]) -> Dict[str, List[int]]:
	cache: Dict[str, List[int]] = collections.defaultdict(list)
	for index, word in enumerate(words):
		cache[word].append(index)
	return cache



print(word_distance('a c b d a q q a'.split(' '), 'a', 'b'))
