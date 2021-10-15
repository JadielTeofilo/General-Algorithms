"""
 Pattern Matching: You are given two strings, pattern and value. 

The pattern string consists of just the letters a and b, describing a pattern within a string. 

For example, the string catcatgocatgo matches the pattern aabab (where cat is a and go is b). 

It also matches patterns like a, ab, and b.

Write a method to determine if value matches pattern


In - pattern: str, value: str
Out - bool


catca

aaa
			catc		catca			catcat

			

catca - aba
tca - ba
ca - a
aba
			c			ca
						t


translation: Dict[str, str], pattern: str, value: str


"""
from typing import Dict


def pattern_matching(pattern: str, value: str) -> bool:
	""" Identifies if the pattern can be used for the value """
	return match_helper(pattern, value, translation={})


def match_helper(
	pattern: str, value: str, translation: Dict[str, str]
) -> bool:
	if not pattern and not value:
		print(translation)
		return True
	if not pattern or not value:
		return False
	curr_pattern: str = pattern[0]
	if translation.get(curr_pattern):
		size: int = len(translation[curr_pattern])
		if translation[curr_pattern] != value[:size]:
			return False
		# Calls recursion for the rest if there is a match with 
		# pattern for current pattern
		return match_helper(pattern[1:], value[size:], translation.copy())
	else:
		# Generate all possibilities for the curr pattern
		for i in range(1, len(value) + 1):
			new_translation: Dict[str, str] = translation.copy()
			new_translation[curr_pattern] = value[:i]
			if match_helper(pattern[1:], value[i:], new_translation):
				return True
	return False


print(pattern_matching('ab', 'cat'))
import pdb;pdb.set_trace()

