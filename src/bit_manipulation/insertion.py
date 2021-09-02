"""
Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i and
j. Write a method to insert Minto N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input: N 100000000000 10011, i 2, j 6
Output: N 10001001100


In - target: int, num: int, start: int, end: int
Out - int


figure size (bits) of num
clear the target
shift the target and use OR 

10001001100


1001100

What happens if the num is negative?


"""



def insertion(target: int, num: int, start: int, end: int) -> int:
	""" Inserts from start to end the bits of num on target """
	if start == end:
		raise ValueError('Start value same as end')
	num_size: int = get_size(num)
	target = clear(target, start, start + num_size)
	return target | (num << start)


def clear(num: int, start: int, end: int) -> int:
	""" Sets zeros on bits of num from start to 
		end non inclusive """
	if start == end:
		raise ValueError('Start value same as end')
	# Builds group of 1s the size of the start - end
	mask: int = (1 << (end - start)) - 1
	return num & ~(mask << start)
	

def get_size(num: int) -> int:
	""" Finds the amount of bits on integer """
	if num < 0:
		return 32
	count: int = 0
	while num > 0:
		num >>= 1  # Removes one bit from integer
		count += 1
	return count


import pdb;pdb.set_trace()
