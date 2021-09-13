"""
 Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator) . You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.



Splits the smaller until finds 2, always solving just one side 

18 * 14
18 * 7 + same
18 * 3 + same + 18
18 >> 2 + same + 18


O(log m) time complexity where m is the size of the smaller number
O(log m) space complexity for the stack where m is the size of the smaller number

"""
from typing import Dict


def recursive_multiply(left: int, right: int) -> int:
	bigger: int = left if left > right else right
	smaller: int = right if left > right else left
	return multiply_helper(bigger, smaller)


def multiply_helper(bigger: int, smaller: int) -> int:
	base_cases: Dict[int, int] = {
		0: 0, 1: bigger, 2: bigger << 1
	}
	if base_cases.get(smaller) is not None:
		return base_cases[smaller]

	if smaller % 2 == 0:
		multiplication: int = multiply_helper(bigger, smaller >> 1)
		return multiplication + multiplication

	multiplication: int = multiply_helper(bigger, (smaller - 1) >> 1)
	return multiplication + multiplication + bigger


import pdb;pdb.set_trace()
