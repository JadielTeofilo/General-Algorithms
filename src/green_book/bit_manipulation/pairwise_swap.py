"""
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

in - number: int
out - int

"""
import enum


class BitType(enum.Enum):
	even = 0
	odd = 1


def pairwise_swap(number: int) -> int:
	""" Swap even bits with odd bits """
	only_even: int = filter_bits(number, BitType.even)
	only_odd: int = filter_bits(number, BitType.odd)
	only_odd %= 0x100000000  # Makes right shift logical
	return only_odd >> 1 | only_even << 1


def filter_bits(number: int, bit_type: BitType) -> int:
	""" Removes bits different from bit type, 
		considering 32 bit integers """
	mask = 0x55555555 if bit_type == BitType.even else 0xaaaaaaaa
	return number & mask


print(pairwise_swap(10))
import pdb;pdb.set_trace()
