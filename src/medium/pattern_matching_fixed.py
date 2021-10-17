"""
Pattern Matching: You are given two strings, pattern and value. The pattern string consists of
just the letters a and b, describing a pattern within a string. 


For example, the string catcatgocatgo matches the pattern aabab (where cat is a and go is b). 

It also matches patterns like a, ab, and b.

Write a method to determine if value matches pattern.

"""
import collections
from typing import Tuple, Iterable, Optional


PatternMetadata = collections.namedtuple('PatternMetadata', 'count start')



def pattern_matching(pattern: str, value: str) -> bool:
	
	for a, b in find_ab_values(pattern, value): 
		if matches(pattern, a, b, value):
			return True
	return False


def find_ab_values(pattern, value) -> Iterable[Tuple[str, str]]:
	a_meta: PatternMetadata = PatternMetadata(
		pattern.count('a'),
		pattern.index('a'),
	)
	b_meta: PatternMetadata = PatternMetadata(
		pattern.count('b'),
		pattern.index('b'),
	)
	# Builds all possibilities of a, than finds the b
	for i in range(1, len(value) + 1):
		a: str = value[:i]
		b: Optional[str] = generate_b(pattern, value, a, b_meta, a_meta)
		if not b:
			continue
		yield a, str(b)


def generate_b(pattern: str, value: str, 
			  a: str, b_meta: PatternMetadata, 
			  a_meta: PatternMetadata) -> Optional[str]:
	b_size: float = (len(value) - (a_meta.count * len(a))) / b_meta.count
	if b_size < 1 or int(b_size) != b_size:
		return
	b_real_start: int = len(a) * b_meta.start
	return value[b_real_start:b_real_start+int(b_size)]


def matches(pattern: str, a: str, b: str, value: str) -> bool:
	index: int = 0
	for char in pattern:
		translation: str = a if char == 'a' else b
		size: int = len(translation)
		if translation != value[index:index+size]:
			return False
		index += size
	return True
		
print(pattern_matching(pattern='aba', value='catca'))
import pdb;pdb.set_trace()	
