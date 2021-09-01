"""
Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at
most 32 characters, print "ERROR:'


in - number: float

out: str


 




"""
from typing import List


def binary_to_string(number: float) -> str:
	""" Turns values from 0 to 1 into binary representation """
	if number is None or number <= 0 or number >= 1:
		raise ValueError('Input outside the range (0, 1)')
	result: List[str] = []

	while number != 0:
		if len(result) >= 32:
			print('ERROR')
			#raise ValueError(
			#	'Binary representation bigger than 32 bits'
			#)
		number *= 2
		if number >= 1:
			result.append('1')
			number -= 1
		else:
			result.append('0')
			
	return ''.join(result)


import pdb;pdb.set_trace()

