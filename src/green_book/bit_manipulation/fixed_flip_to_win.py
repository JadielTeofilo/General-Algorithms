"""
 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.
EXAMPLE
Input:
 1775
 (or: 11011101111)
Output:
 8
 
 
2 1 3 1 4


O(1) memory
O(b) where b is the amount of bit on the integer

"""
from typing import Iterable, Optional
import collections


Window = collections.namedtuple('Window', 'left_ones mid_zeros right_ones')


def flip_to_win(number: int) -> int:
    """ Finds the biggest 1s sequence after 
        inserting a bit 1 """
    max_size: int = 0
    for left_ones, mid_zeros, right_ones in _get_window(number):
        if mid_zeros == 1:
            max_size = max(max_size, left_ones + right_ones + 1)
    return max_size


def _get_window(number: int) -> Iterable[Window]:
    """ Builds sliding windows when the mid element is a 0 bit """
    bit_length_encoding: Iterable[int] = _get_length_encoding(number)
    left: int = 0
    mid: int = 0
    right: int = 0
    mid_has_zero_bit: bool = False
    for encoding in bit_length_encoding:
        left = mid
        mid = right
        right = encoding
        if mid_has_zero_bit and mid == 1:
            yield Window(left, mid, right)
        mid_has_zero_bit = not mid_has_zero_bit


def _get_length_encoding(number: int) -> Iterable[int]:
    """ Finds the iterable of the bit length encoding 
        
        Always starts with the bit 0, meaning it adds 
        an encoding of length one if the first bit is 
        a one
        """
    counter: int = 0
    last_bit: Optional[int] = None
    for bit in _get_bits(number):
        if last_bit is None and bit == 1:
            # Yields one representing a encoding of 
            # size one for bit 0
            yield 1
        if last_bit is not None and last_bit != bit:
            yield counter
            counter = 0
        counter += 1
        last_bit = bit
    
    if counter and counter > 0:
        yield counter
    

def _get_bits(number: int) -> Iterable[int]:
    number %= 0x100000000
    while number != 0:
        yield number & 1
        number >>= 1

print(flip_to_win(5), 5)
print(flip_to_win(7), 7)
print(flip_to_win(10), 10)
print(flip_to_win(11), 11)
import pdb;pdb.set_trace()
