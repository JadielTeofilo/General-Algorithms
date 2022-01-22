"""
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.


Use a XOR

"""
from typing import Iterable


def binary_edit_distance(left_number: int, right_number: int):
	""" Finds the amount of flipped bit to make 
		left equals right """

	# Xor gives the different bits between the two
	diff: int = left_number ^ right_number

	counter: int = 0
	for bit in get_bits(diff):
		counter += bit

	return counter


def get_bits(number) -> Iterable[int]:
	# Turns shift into logical right shift
	number %= 0x100000000
	while number != 0:
		yield number & 1
		number >>= 1
	return number


print(binary_edit_distance(29, 15))
print(len([a for a in get_bits(-1)]))
import pdb;pdb.set_trace()
