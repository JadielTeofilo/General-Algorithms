"""

Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.

10111 = 11


11011 = 13
1010 = 10
1100 = 12

10110 = 22

10101
11010 = 26

11001

01001 = 9
00101 = 5
00110 = 6





0111
1110 vs 1101

10
100
001

0111

1011
111




Should I consider a 32 bit integer?
yes, but that should not matter
So, it is the imediatly smaller and the imediately bigger right?
yes
Only positives makes things a lot easier

What happens on places like 111

in - number: int

out - NextNums(smallest, largest)


100011000101010001

O(b) time complexity where b is the amount of bits
O(1) space complexity

"""
from typing import Iterable, Optional
import collections


NextNumber = collections.namedtuple('NextNumber', 'smallest largest')


def get_next_number(number: int) -> NextNumber:
	""" Finds the largest and smallest number 
		with the same amount of  1s bit """
	return NextNumber(_get_smallest(number), _get_largest(number))


def _get_smallest(number: int) -> int:
	""" Finds the imediatelly smaller number with 
		same amount of 1s bits """
	last_bit: Optional[int] = None
	ones: int = 0
	for index, bit in enumerate(_get_bits(number)):  # 1101
		if bit == 1:
			ones += 1
		if last_bit == 0 and bit == 1:
			number = update_bit(number, index, 0)
			break
		last_bit = bit
	else:
		return number  # Case this is the smallest possible

	number = clear_bits(number, 0, index)
	number = fill_bits(number, index - ones, (1 << ones) - 1)
	
	return number


def clear_bits(number: int, start: int, end: int) -> int:
	mask: int = ((1 << (end - start)) - 1) << start
	return number & ~mask


def fill_bits(number: int, start: int, bits: int) -> int:
	return number | (bits << start)


def _get_largest(number: int) -> int:  
	""" Finds the imediatelly bigger number with
		the same amount of 1s bits """
	last_bit: Optional[int] = None
	ones: int = 0
	for index, bit in enumerate(_get_bits(number)):
		if last_bit == 1 and bit == 0:
			number = update_bit(number, index, 1)
			ones -= 1
			break
		last_bit = bit
		if bit == 1:
			ones += 1
	number = clear_bits(number, 0, index)
	number = fill_bits(number, 0, (1 << ones) - 1)
	return number


def _get_bits(number: int) -> Iterable[int]:
	""" Finds the bits of a number from the 
		LSB to the MSB """
	while number:
		yield number & 1
		number >>= 1
		number &= ~(1 << 31)  # Clean the shifted bit
	yield 0


def update_bit(number: int, index: int, value: int) -> int:
	number &= ~(1 << index)  # Cleans the bit
	return number | (value << index)  # Inserts the value


print(get_next_number(9))
print([a for a in _get_bits(11)])
print(update_bit(3, 2, 1))

import pdb;pdb.set_trace()
