"""
 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte. The screen has width w, where wis divisible by 8 (that is, no byte will
be spl it across rows). The height of the screen, ofcourse, can be derived from the length of the array
and the width . Implement a function that draws a horizontal line from (x1, y) to (x2, y).
The method signature should look something like:


drawLine(byte[] screen, int width, int X1 , int X2 , int y)


w = 16

line = w/8 * y

[
0x00, 0x00
0x00, 0x00
0x00, 0x00
]

word that starts x1/8
word that ends  x2/8

words in between should be turned into ones


"""
from typing import List

BYTE_MAX_INDEX = 7
BYTE_SIZE = 8


def draw_line(screen: List[int], width: int, x1: int, x2: int, y: int) -> None:
	""" Draws line on screen according to coordinates """
	starting_index: int = width/BYTE_SIZE * y + x1//BYTE_SIZE
	ending_index: int = starting_index + x2//BYTE_SIZE
	if starting_index == ending_index:
		line: int = group_of_ones(1 + x2 - x1)
		screen[starting_index] = update_bits(
			screen[starting_index], 
			line, 
			BYTE_MAX_INDEX - x2, 
			BYTE_MAX_INDEX - x1
		)
	else:
		x1 %= BYTE_SIZE
		x2 %= BYTE_SIZE
		line: int = group_of_ones(x1 - BYTE_SIZE)
		screen[starting_index] = update_bits(screen[starting_index], line, 
											 0, BYTE_MAX_INDEX - x1)
		line: int = group_of_ones(x2 + 1)
		screen[ending_index] = update_bits(screen[ending_index], line, 
										   BYTE_MAX_INDEX, BYTE_MAX_INDEX - x2)
		empty_bytes_in_between(screen, starting_index, ending_index)


def update_bits(number: int, value: int, start: int, end: int) -> int:
	
	# Cleans bits
	number &= ~(group_of_ones(start - end + 1) << start)
	# Inserts value
	return number | (value << start)


def empty_bytes_in_between(numbers: List[int], start: int, end: int) -> None:
	for i in range(start + 1, end):
		numbers[i] = 0xFF


def group_of_ones(size: int) -> int:
	return (1 << size) - 1




