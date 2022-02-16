"""
Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).


abba
ba

In - word: str, target: str
Out - int


Brute force

Generate all subsequences, that match the desired string

Keep a target_index
Keep a start

if target_index == len(target) - 1 we return 1

when start >= len(word) we return 0

iterate from start to len(word)
	skip if element is diff from target[target_index]
	solve(target_index + 1, start + 1)


if we memoize on start and target_index we get 

O(m*n^2) time complexity where n is the size of word and m the size of target
O(m) space complexity



							abba [ab]
			(a)bba [b]								bba
	(ab)ba []			(a)ba
					(ab)a []

"""
from typing import Dict, Tuple


Cache = Dict[Tuple[int, int], int]


class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def numDistinct(self, word: str, target: str)-> int:
		cache: Cache = {}
		return self.find_subsequences(word, target, cache, start=0, 
						 			  target_index=0)

	def find_subsequences(self, word: str, target: str, cache: Cache, 
						  start: int, target_index: int) -> int:
		if (start, target_index) in cache:
			return cache[(start, target_index)]
		if target_index >= len(target):
			return 1
		if start >= len(word):
			return 0
		subsequences: int = 0
		for i in range(start, len(word)):
			if word[i] != target[target_index]:
				continue
			subsequences += self.find_subsequences(
				word, target, cache, 
				i + 1, target_index + 1
			)
		cache[(start, target_index)] = subsequences
		return subsequences
		

