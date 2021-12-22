"""
Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9


What is the possible input? digits, space, non digit chars


Iterate on the digits until finding non digit number
no digit found, return 0
for each digit multiply the curr by 10 and add the digit (curr starts at zero)

if num > max int 

return sys.maxsize

In - number: str
Out - int


O(n) where n is the size of numbers string

"""
from typing import Dict
import sys

EQUIVALENCY: Dict[str, int] = {num: index for index, num 
							  in enumerate('0123456789')}


class Solution:
	# @param A : string
	# @return an integer
	def atoi(self, number: str) -> int:
		if not number:
			return 0
		sign = 1
		if number[0] in {'-', '+'}:
			sign = -1 if number[0] == '-' else 1
			number = number[1:]
		curr: int = 0
		for char in number:
			if not char.isdigit():
				break
			curr *= 10
			curr += EQUIVALENCY[char]
			if curr > sys.maxsize:
				curr = sys.maxsize
				break
		curr *= sign
		return curr
