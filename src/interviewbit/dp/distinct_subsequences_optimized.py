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

Better approach 

Build a matrix that for a given row gives the answer for word[:col], target[:row]
recurrence is dp[row][col] = dp[row][col - 1] + dp[row - 1][col - 1]


 
	abbab
   111111
  a011122
  b001224

we keep two lists of size len(word) + 1
[011111]
[000000]
we iterate on range(len(words)) * range(len(target))
if word[col] == target[row]
dp[1][col+1] = dp[1][col] + dp[0][col]
else
dp[1][col+1] = dp[1][col]

case 1). if T[i] != S[j], then the solution would be to ignore the character S[j] and align substring T[0..i] with S[0..(j-1)]. Therefore, dp[i][j] = dp[i][j-1].

case 2). if T[i] == S[j], then first we could adopt the solution in case 1), but also we could match the characters T[i] and S[j] and align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)]. As a result, dp[i][j] = dp[i][j-1] + d[i-1][j-1]


we can keep only the curr and last row to solve it in:

O(m*n) time complexity where n = len(word) m = len(target)
O(m) space complexity 

"""
from typing import Dict, Tuple, List, Iterable


Matrix = List[List[int]]


class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def numDistinct(self, word: str, target: str)-> int:
		dp: List[List[int]] = [[1] * (len(word) + 1), 
							   [0] * (len(word) + 1)]

		for row in range(len(target)):
			for col in range(len(word)):
				if word[col] == target[row]:
					dp[1][col+1] = dp[1][col] + dp[0][col]
				else:
					dp[1][col+1] = dp[1][col]
			dp[0] = dp[1].copy()
			dp[1] = [0] * (len(word) + 1)
		return dp[1][-1]

