"""
Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to
generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
this task.

In - file_name: str
Out - int



1GB fits how many ints?
1 int is 4 bytes
1GB is ~ 1000_000_000 bytes
meaning 250_000_000 integers

make files of sorted 200_000_000 elements and them do a sorted merge of them

O(n) time complexity where n is the number of ints since you might still 
O(1) space complexity since will always take the same amount of memory

1GB has 1000_000_000 bytes or 8000_000_000 bits, meaning we can map each value of the integer on a bit vector




32 bits 
valor maximo: 2^31
valores representados 2^32 - 1

FOLLOW UP
What if you have only 10MB of memory? Assume that all the values are distinct and we now have
no more than one billion non-negative integers.

"""
from typing import List, Iterable, Optional


def missing_int(file_name: str) -> Optional[int]:
	""" Finds an integer that is not on the file of file_name """
	# The size of bit_vector is such that will 
	# fit all possible integers
	bit_vector: List[int] = get_empty_bit_vector(size=2 ** 31 - 1)
	for integer in read_file_integers(file_name):
		update_bit_vector(bit_vector, integer)
	for index, bit in enumerate(get_bits(bit_vector)):
		if bit == 0:
			return index


def read_file_integers(file_name: str) -> Iterable[int]:
	with open(file_name) as fp:
		for line in fp:
			yield int(line)


def get_empty_bit_vector(size: int) -> List[int]:
	bit_vector: List[int] = []
	for _ in range(size//32 + 1):
		bit_vector.append(0x00000000)
	return bit_vector


def update_bit_vector(bit_vector: List[int], integer: int) -> None:
	index: int = integer // 32
	offset: int = integer % 32
	bit_vector[index] = set_bit(bit_vector[index], offset)


def set_bit(number: int, index: int) -> int:
	mask: int = 1 << (31 - index)
	return number | mask


def get_bits(bit_vector: List[int]) -> Iterable[int]:
	for integer in bit_vector:
		for i in range(31, -1, -1):
			yield (integer >> i) & 1


print(missing_int('missing_int.input'))
import pdb;pdb.set_trace()
