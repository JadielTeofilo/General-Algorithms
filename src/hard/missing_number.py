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


BitCount = collections.namedtuple('BitCount', 'zeros')


def missing_number(numbers: List[int]) -> int:
	last_num: int = len(numbers)
	target_number: int = 0
	for bit in range(math.ceil(math.log(last_num, 2))):
		expected_bit_count: BitCount = find_expected_bit_count(bit, last_num) 
		bit_count: BitCount = find_current_bit_count(bit, numbers)
		if expected_bit_count.zeros <= bit_count.zeros:
			target_number = update_bit(target_number, bit, 1)
		else:
			target_number = update_bit(target_number, bit, 0)
		print(target_number)
	return target_number

	
def find_expected_bit_count(bit: int, size: int) -> BitCount:
	if bit == 0:
		window_size = 2
	else:
		window_size: int = bit * 4  # the size of cycle, 0101 = 2, 0011 = 4
	windows: int = size // window_size
	zeros: int = windows * window_size // 2
	left_overs: int = size % window_size + 1
	left_over_zeros: int = min(left_overs, window_size // 2)
	return BitCount(zeros+left_over_zeros)


def find_current_bit_count(bit: int, numbers: List[int]) -> BitCount:
	zeros: int = 0
	for number in numbers:
		# Adds one if equals zero
		zeros += int(get_bit(number, bit) == 0)
	return BitCount(zeros)

def get_bit(number: int, index: int) -> int:
	# Gets bit on the desired position
	return int(number & (1 << index) != 0)


def update_bit(number: int, bit: int, value: int) -> int:
	# Cleans bit
	number = number & ~(1 << bit)
	# Sets bit
	return number | (value << bit)



print(missing_number([
0,1,2,3,4,5,6,7,8,9,10,12,13,14,15
]))
