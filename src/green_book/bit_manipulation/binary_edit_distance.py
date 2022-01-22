"""
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.


01010100
00011111

ans = 4

O(b) time complexity where b is the amount of bits of the bigger number
O(1) space complexity



"""
from typing import Iterable
import itertools as ite


def binary_edit_distance(left_number: int, right_number: int) -> int:
	""" Finds the number of flipped bits needed to 
		turn left into right """
	left_bits: Iterable[int] = get_bits(left_number)
	right_bits: Iterable[int] = get_bits(right_number)
	counter: int = 0
	for left_bit, right_bit in ite.zip_longest(left_bits, right_bits, 
								  			   fillvalue=0):
		if left_bit != right_bit:
			counter += 1
	return counter


def get_bits(number: int) -> Iterable[int]:
	""" Finds bits of number, considering a 32 bit integer """
	while number != 0:
		yield number & 1
		number >>= 1
		# Needed for negative numbers, it clears the MSB
		number &= ~(1 << 31)


print(binary_edit_distance(29, 15))
import pdb;pdb.set_trace()
