"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator) . You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.



In left: int right: int

Out int

12 * 6 = 72

12 * (2 * 2 + 2)

48 + 


1000 >> 1
100 >> 1
10 >> 1
1 >> 

110 >> 1
11 >> 1
1

15
1111 >> 1
111 >> 1
11 >> 1
1

[3,1,1,1,0]

12*2*2+12

12 << 1

O(log m) time complexity where m is the number of bits of the smaller of the numbers
O(log m) space complexity where m is the number of bits of smaller of the numbers

"""
from typing import List


def recursive_multiply(left: int, right: int) -> int:
	smaller: int = left if left < right else right
	bigger: int = right if left < right else left
	return multiply_helper(bigger, smaller)


def multiply_helper(bigger: int, smaller: int) -> int:
	shift_array: List[int] = build_shift_array(smaller)
	result: int = 0
	for shift in shift_array:
		result += bigger << shift
	return result


def build_shift_array(number: int) -> List[int]:
	""" Builds an array that indicates the  
		shifts to be made to achieve the multiplication """
	shift_array: List[int] = []
	multiplier: int = 0
	# Adds a shift of zero for the odd numbers
	if number & 1:
		shift_array.append(0)
	while number > 1:
		multiplier += 1
		number >>= 1
		if number != 1 and number & 1:
			shift_array.append(1)
	shift_array.append(multiplier)
	return shift_array	

recursive_multiply(5, 10)
import pdb;pdb.set_trace()
