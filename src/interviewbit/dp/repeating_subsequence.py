"""
Given a string A, find length of the longest repeating sub-sequence such that the two subsequence don’t have same string character at same position,

i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

NOTE: Sub-sequence length should be greater than or equal to 2.

abba
false

aabsb
ab ab
 
  aabsb 
  
a001000
a0111
b00 0 
s0   0  
b0    0

  abab
 11111
a01122
b00113
a00011
b00001

  abbab
 000000
a000011
b000112
b001112
a011111
b002222


case equal - we add one to the 
dp[row][col] = dp[row-1][col-1] + 1
case diff - we just keep the size from the last element 
dp[row][col] = dp[row][col-1]

when row equals col, consider it different

we can keep only the last two rows to make it O(n) space

first: List[int] = [0] * len(word)
second: 

In - word: str
Out - int


O(n^2) time complexity where n is the size of word

"""
from typing import List


class Solution:
	# @param A : string
	# @return an integer
	def anytwo(self, word: str) -> int:
		first: List[int] = [0] * (len(word) + 1)
		second: List[int] = [0] * (len(word) + 1)

		max_subsequence: int = 0
		for row in range(len(word)):
			for col in range(len(word)):
				if word[col] == word[row] and col != row:
					second[col + 1] = first[col] + 1
				else:
					second[col + 1] = second[col]
				max_subsequence = max(max_subsequence, second[col + 1])
			first = second
			second = [0] * (len(word) + 1)

		return 1 if max_subsequence > 1 else 0
		


