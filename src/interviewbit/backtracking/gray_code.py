"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

There might be multiple gray code sequences possible for a given n.

Return any such sequence.

In - bits: int
Out - stdout(List[int])


000
001
011
010



2^2 - 1
4

0 -> 3

0 : {1 2}
1 : 0 3
2 : 0 3
3 : 1 2

stop point is when n is 0, then return []
generate_sequence(size: int) -> List[str]

    next_level: str = generate_sequence(size - 1)

"""
from typing import List


def generate_sequence(size: int) -> List[int]:
    if size == 1: 
        return [0, 1]
    next_level: List[int] = generate_sequence(size - 1)

    first_half: List[int] = [change_bit(rest, 0, size - 1) 
                             for rest in next_level]
    next_level.reverse()
    second_half: List[int] = [change_bit(rest, 1, size - 1)
                              for rest in next_level]
    return first_half + second_half


def change_bit(number: int, bit: int, index: int) -> int:
    number &= ~(1 << index)  # Empties bit
    return number | (bit << index)  # Sets bit


class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, size: int) -> List[int]:
        if size < 1:
            return []
        return generate_sequence(size)



