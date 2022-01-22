"""
Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
Hints: #138, #174, #187, #209, #243, #265, #295


In - number: int
Out - Iterable[str]

( or ) at each step, closing only available if has opening before

			(
	)				(
	(			)		(
			

heigth of tree is n with at most 2 branches at each node
O(n*2^n) time complexity where n is the inputed number
O(n^2) space complexity where n is the input


"""
from typing import Iterable, List


def parens(number: int) -> Iterable[str]:
	""" Finds and yields all possible valid 
		parentesis combinations of at most 
		pair size 'number' """
	yield from parens_helper(number*2, opening=0, 
							 max_opening=number, curr_word=[])


def parens_helper(number: int, opening: int, max_opening: int,
				  curr_word: List[str]) -> Iterable[str]:
	if number == 0:
		yield ''.join(curr_word)

	if max_opening > 0:
		yield from parens_helper(number - 1, opening + 1, 
								 max_opening - 1, curr_word + ['('])
	
	if opening > 0:
		yield from parens_helper(number - 1, opening - 1, 
								 max_opening, curr_word + [')'])


print([a for a in parens(2)])
print([a for a in parens(3)])
import pdb;pdb.set_trace()
