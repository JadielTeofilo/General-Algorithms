"""
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:

A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).



aobosjahshauaahshaajd

aahshaajd
djaahshaa

abcabacba
010001200


cabac
00012

caba


In - word: str
Out - str

consider all possible middle points for the palindrome
The main point is to find the mid point of the desired palindrome 
with the mid point it is possible to expand to both sides while valid



abac
0123






"""
import dataclasses
from typing import Dict, Any


TrieNode = Dict[str, Any]


class Trie:

	def __init__(self) -> None:
		self.root: TrieNode = {'children': {}}
		
	def insert(self, word: str) -> None:
		# TODO


class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, word: str) -> str:
		trie: Trie = self.build_trie(word[::-1])  # TODO
		max_size: int = 0
		for i in range(len(word)):
			



		
