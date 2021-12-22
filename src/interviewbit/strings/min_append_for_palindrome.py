"""
Problem Description

Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.


acdcdc
cdcdca

Reverse the string and try to find the matching substring
Use a pointer for each string, when the first string gets to an end stop
the pointer to the second string will tell us what we need to add to make a palindrome


O(n^2) time complexity where n is the size of the string
O(1) space 

In - word: str
Out - int

Use LPS (longest prefix that is also a suffix) array with the KMP algorighm

"""
from typing import List

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, word: str) -> int:
		reversed_word: str = word[::-1]
		lps: List[int] = self.build_lps(reversed_word)
		i, j = 0, 0
		while i < len(word):
			if word[i] == reversed_word[j]:
				i += 1
				j += 1
			elif j == 0:
				i += 1
			else:
				j = lps[j] - 1
		return len(word) - j

	def build_lps(self, word: str) -> List[int]:
		lps: List[int] = [0] * len(word)
		left, right = 0, 1
		while right < len(word):
			if word[left] == word[right]:
				lps[right] = lps[right - 1] + 1
				right += 1
				left += 1
				continue
			elif left == 0:
				right += 1
				continue
			while left > 0 and word[left] != word[right]:
				left -= 1
		return lps
			
