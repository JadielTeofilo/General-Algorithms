"""
 Add Without Plus: Write a function that adds two numbers. You should not use + or any arithmetic
operators.


"""
from typing import Iterable, Set
import itertools as it


def sum_(left: int, right: int) -> int:
    if left < right:
        # Make sure left is always bigger
        return sum_(right, left)
    # TODO check empty inputs
    left_bits: Iterable[int] = get_bits(left)
    right_bits: Iterable[int] = get_bits(right)
    goes: int = 0
    result: int = 0
    i: int = -1
    for left_bit, right_bit in it.zip_longest(
        left_bits, right_bits, fillvalue=0
    ):
        i += 1
        curr_bit: int = left_bit ^ goes ^ right_bit
        goes = find_goes(left_bit, right_bit, goes)
        result = update_ith_bit(result, curr_bit, i)
    if goes == 1:
        result = update_ith_bit(result, goes, i+1)
    return result


def find_goes(first_bit: int, second_bit: int, goes: int) -> int:
    """ 
        Finds if there is a goes on the sum 

        Builds a num concatenating the three bits
        000 100 010 and 001 are not going to generate goes
    """
    number: int = (first_bit << 2) | (second_bit << 1) |  goes
    no_goes: Set[int] = {0, 1, 2, 4}
    # Returns one if number will generate goes
    return int(number not in no_goes)


def get_bits(number: int) -> Iterable[int]:
    # Make pythons shift logical
    number %= 0x100000000
    while number != 0:
        # Yields the last bit
        yield number & 1
        number >>= 1

def update_ith_bit(number: int, bit: int, index: int) -> int:
    # Cleans bit
    number = number & ~(1 << index)
    # Sets bit
    number = number | (bit << index)
    return number


import pdb;pdb.set_trace()
