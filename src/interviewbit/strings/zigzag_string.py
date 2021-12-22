"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R

And then read line by line: PAHNAPLSIIGYIR

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"

**Example 2 : **

ABCD, 2 can be written as

A....C
...B....D

and hence the answer would be ACBD.


The idea is to iterate on the string iterating the cycle 0 1 2 1 0 1 2 0 1 2 1 0 until the end of the string 
Add result to three lists
concatenate the lists as string

In - word: str, size: int
Out - str


"""
from typing import List, Union


class Solution:
	# @param A : string
	# @param B : integer
	# @return a strings
	def convert(self, word: str, size: int) -> str:
		if size <= 1:
			return word
		zig_zag: List[List[str]] = [[] for _ in range(size)]
		i: int = 0
		jump: int = 1
		for char in word:
			zig_zag[i].append(char)
			i += jump
			# Inverts when getting to the corners
			if i >= size - 1 or i <= 0:
				jump *= -1
		result: List[str] = [''] * size
		for index, line in enumerate(zig_zag.copy()):
			result[index] = ''.join(line)
		return ''.join(result)
			
			
