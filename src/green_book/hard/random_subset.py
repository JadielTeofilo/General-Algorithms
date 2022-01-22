"""
Random Set: Write a method to randomly generate a set of m integers from an array of size n. Each
element must have equal probability of being chosen.

In - numbers: List[int], m: int
Out - List[int]

Use the same idea of the swaps

"""
import random
import time
from typing import List


def random_set(numbers: List[int], size: int) -> List[int]:
	# TODO Validade size vs len of numbers
	result: List[int] = numbers[:size]
	random.seed(time.time())
	for i in range(size, len(numbers)):
		k: int = random.randint(0, i)  # inclusive
		if k < size:
			result[k] = numbers[i]

	return result


print(random_set([i for i in range(21)], 5))



