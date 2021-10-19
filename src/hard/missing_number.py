"""
Missing Number: An array A contains all the integers from 0 to n, except for one number which
is missing. In this problem, we cannot access an entire integer in A with a single operation. The
elements of A are represented in binary, and the only operation we can use to access them is "fetch
the jth bit of A[i]," which takes constant time. Write code to find the missing integer. Can you do it in O(n) time?

In - numbers: List[int]
Out - int

Are those 32 bit integers?
yup

Going bit by bit, you can tell the expected amount of ones and zeros
"""
import collections
import math
from typing import List


BitCount = collections.namedtuple('BitCount', 'zeros ones')


def missing_number(numbers: List[int]) -> int:
	last_num: int = len(numbers)
	target_number: int = 0
	for bit in range(math.ceil(math.log(last_num, 2))):
		bit_count: BitCount = find_current_bit_count(bit, numbers)
		if (bit_count.zeros == bit_count.ones - 1 or 
			bit_count.zeros == bit_count.ones):
			missing_bit: int = 0
		else:
			missing_bit: int = 1
		numbers = remove_incorrect(numbers, bit, correct_bit=missing_bit)
		target_number = update_bit(target_number, bit, missing_bit)
	return target_number


def find_current_bit_count(bit: int, numbers: List[int]) -> BitCount:
	zeros: int = 0
	ones: int = 0
	for number in numbers:
		# Adds one if equals the desired bit
		zeros += int(get_bit(number, bit) == 0)
		ones += int(get_bit(number, bit) == 1)
	return BitCount(zeros, ones)


def get_bit(number: int, index: int) -> int:
	# Gets bit on the desired position
	return int(number & (1 << index) != 0)


def update_bit(number: int, bit: int, value: int) -> int:
	# Cleans bit
	number = number & ~(1 << bit)
	# Sets bit
	return number | (value << bit)


def remove_incorrect(numbers: List[int], 
					 bit: int, correct_bit: int) -> List[int]:
	return [
		number 
		for number in numbers
		if get_bit(number, bit) == correct_bit
	]


print(missing_number([
0,2,3,4,5,6,7,8,9,10,11,12,13,14,15
]))
