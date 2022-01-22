"""
FOLLOW UP
What if you have only 10MB of memory? Assume that all the values are distinct and we now have
no more than one billion non-negative integers.


there are 2^31 - 1 non negative integers wich is around 2 billion

10MB is 1_000_000 bytes or 8_000_000 bits

we can use a bit vector of size 4_000_000 to store the visited elements

But first we have to group every 1_000_000 elements to find which group has a missing elements, 
that is possible cuz we know *there are no duplicates*. 

To do that we can create an array of integers of size 1_000_000, which takes 4MB, from that we can find the group of thousands that have missing element.
The bit vector will then be of size 1_000


O(n) time complexity where n is the amount of integers
O(1) space since always will be using 4MB


"""
from typing import List, Iterable


def missing_int(file_name: str) -> int:
	""" Finds a missing integer on the file """
	target_group: int = find_target_group_start(file_name)
	bit_vector: List[bool] = [False] * 1000
	for integer in read_integers(file_name):
		if not is_in_range(integer, target_group):
			continue
		bit_vector[integer % 1000] = True
	return target_group + find_unset_bit(bit_vector)


def find_target_group_start(file_name: str) -> int:
	""" Finds the start of the range that has a missing integer """

	# Every item represents one group of 1000 elements
	integer_groups: List[int] = [0] * 1000
	for integer in read_integers(file_name): 
		integer_groups[integer // 1000] += 1
	for index, group in enumerate(integer_groups):
		if group < 1000:
			return index*1000
	raise ValueError('No missing integer on file')


def read_integers(file_name: str) -> Iterable[int]:
	with open(file_name) as fp:
		for line in fp:
			if not line.rstrip().isdigit():
				raise ValueError(f'File contain non digit chars {line}')
			yield int(line)


def is_in_range(integer: int, target_group: int) -> bool:
	return integer >= target_group and integer <= (target_group + 999)


def find_unset_bit(bit_vector: List[bool]) -> int:
	for vector_index, bit in enumerate(bit_vector):
		if bit == False:
			return vector_index 
	raise ValueError('No unset bit found')


print(missing_int('missing_int_harder.input'))
import pdb;pdb.set_trace()

