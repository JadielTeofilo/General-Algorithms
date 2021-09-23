"""
Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The
array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
available, how would you print all duplicate elements in the array

In List[int]



4KB is ~ 4_000 bytes or ~ 32_000 bits

So we can build a bit_vector of size 32_000 and check against it

In python an integer does not only take 32 bits, so for this problem we will consider that it does, or it will not be feasible

O(n) time complexity where n is the amount of numbers
O(n) space where n is the amount of numbers


"""
import math
from typing import List, Iterable


MAX_NUMBER = 32_000


def find_duplicates(numbers: List[int]) -> Iterable[int]:
	bit_vector: List[int] = build_bit_vector(size=MAX_NUMBER)
	for number in numbers:
		if get_bit(bit_vector, number) == 1:
			yield number
		set_bit(bit_vector, number)


def build_bit_vector(size: int) -> List[int]:
	size = math.ceil(size / 32)  # Get number of ints needed
	bit_vector: List[int] = []
	for _ in range(size): 
		bit_vector.append(0)
	return bit_vector


def get_bit(bit_vector: List[int], index: int) -> int:
	# Finds the desired integer in the list
	integer: int = bit_vector[index // 32]
	# Makes the Mask have the desired bit as 1
	mask: int = 1 << (31 - (index % 32))
	return int(integer & mask != 0)  # Checks if bit was not zero


def set_bit(bit_vector: List[int], index) -> None:
	integer: int = bit_vector[index // 32]
	# Makes the mask have only the desired bit as 1
	mask: int = 1 << (31 - (index % 32))
	# Sets the bit marked on the mask
	bit_vector[index // 32] = integer | mask


print([a for a in find_duplicates([1,2,3,4,5,6,7,8,3,9,10,11,1, 2])])
import pdb;pdb.set_trace()
