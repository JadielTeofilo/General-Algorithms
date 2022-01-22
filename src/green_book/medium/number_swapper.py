"""
Number Swapper: Write a function to swap a number in place (that is, without temporary vari-
ables).


left: int, right: int

left, right = right, left

left = left + right
right = left - right


coded = N * B + A
A = coded%N
B = (coded - A)/N

In - numbers: List[int], origin, target
Out - None


numbers[origin], numbers[target] = numbers[target], numbers[origin]




"""
from typing import List


def number_swapper(numbers: List[int], left: int, 
				   right: int) -> None:
	""" Does the swapping on the desired indexes """
	numbers[left] = numbers[left] * 2 ** 32 + numbers[right]
	numbers[right] = numbers[left]
	numbers[left] = numbers[left] % 2 ** 32
	numbers[right] = numbers[right] // 2 ** 32


def number_swapper_simpler(numbers: List[int], 
						   left: int, right: int) -> None:
	""" Does the swapping on the desired indexes """
	numbers[left] = numbers[left] + numbers[right]
	numbers[right] = numbers[left] - numbers[right]
	numbers[left] = numbers[left] - numbers[right]
	

def number_swapper_bitwise(numbers: List[int], 
						   left: int, right: int) -> None:
	""" Does the swapping on the desired indexes """
	numbers[left] = numbers[left] ^ numbers[right]
	numbers[right] = numbers[right] ^ numbers[left]
	numbers[left] = numbers[left] ^ numbers[right]


test = [1,2,3,4,5]
print(test)
number_swapper(test, 0, 3)
print(test)
test = [1,2,3,4,5]
number_swapper_simpler(test, 0, 3)
print(test)
test = [1,2,3,4,5]
print(test)
number_swapper_bitwise(test, 0, 3)
print(test)
import pdb;pdb.set_trace()
