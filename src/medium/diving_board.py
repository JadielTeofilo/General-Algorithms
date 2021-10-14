"""
Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
There are two types of planks, one of length shorter and one of length longer. You must use
exactly K planks of wood. Write a method to generate all possible lengths for the diving board.


In planks: int, shorter: int, longer: int
Out: List[int]


Types are int?
yup


planks = 5
shorter = 1 
longer = 2

				_
		1				2
	1		2		1		2

generate(planks: int, shorter: int, longer: int, curr_sum: int) Iterable[int]:



BCR O(2^K)



"""
from typing import Iterable, Tuple, Set


def possible_diving_boards(
	planks: int, shorter: int, longer: int
) -> Iterable[int]:
	""" Finds all possible diving boards with 
		given planks, being able to choose 
		shorter or longer 
	"""
	if shorter < 0 or longer < 0 or planks < 0:
		raise ValueError('Inputed values can not be negative')
	cache: Set[Tuple[int, int]] = set()
	return generate_boards(planks, shorter, longer, 
						   curr_sum=0, cache=cache)

def generate_boards(
	planks: int, shorter: int, longer: int, 
	curr_sum: int, cache: Set[Tuple[int, int]]
) -> Iterable[int]:
	if (planks, curr_sum) in cache:
		return
	if planks <= 0:
		yield curr_sum
		cache.add((planks, curr_sum))
		return
	yield from generate_boards(planks - 1, shorter, 
							   longer, curr_sum + shorter, cache)
	yield from generate_boards(planks - 1, shorter, 
							   longer, curr_sum + longer, cache)


def crazy_diving_board(planks: int, shorter: int, 
					   longer: int) -> Iterable[int]:
	visited: Set[int] = set()
	for short_amount in range(planks + 1):
		long_amount: int = planks - short_amount
		size: int = long_amount * longer + short_amount * shorter
		if size in visited:
			continue
		yield size

print( [a for a in possible_diving_boards(5, 11, 32)])
print( [a for a in crazy_diving_board(5, 11, 32)])

