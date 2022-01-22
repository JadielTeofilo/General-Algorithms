"""
Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.

in - number: int
out - int

      i
1001010001101110
   j


O(n) time

O(n) space

"""
from typing import Union, List
import math


def	flip_to_win(number: int) -> int:
	""" Finds the size of max subsequence of ones 
		after adding 1 on any place """
	bits: str = bit_to_str(number)
	fast: int = 0
	slow: int = 0
	zero_count: int = 0
	result: Union[float, int] = -math.inf
	last_zero_index: int = 0
	while fast < len(bits):
		if bits[fast] == 1:
			fast += 1
			continue
		zero_count += 1
		if zero_count == 1:
			last_zero_index = fast
		elif zero_count == 2:
			zero_count -= 1
			result = update_result(result, fast, slow)
			slow = last_zero_index + 1
			last_zero_index = fast
		fast += 1
	return int(result)
	

def bit_to_str(number: int) -> str:
	result: List[str] = []
	def get_last_bit(number: int) -> str:
		mask: int = 1
		return str(mask & number)
	while number:
		last_bit: str = get_last_bit(number)
		result.append(last_bit)
		number >>= 1
	return ''.join(reversed(result))


def update_result(result: Union[float, int], 
				  fast: int, slow: int) -> int:
	return max(result, fast - slow)


import pdb;pdb.set_trace()
