"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

1 4 5
4 5
5 2 3


1

2




"""
from typing import List


def weave(left: List[int], right: List[int]) -> List[List[int]]:
	""" Gives all possible combinations of left and right 
		keeping the original order on left and right """
	if not left or not right:
		return [left] if left else [right]
	left_result: List[List[int]] = weave_helper(left, right)
	right_result: List[List[int]] = weave_helper(right, left)
	return left_result + right_result
	

def weave_helper(first: List[int], second: List[int]) -> List[List[int]]:
	""" Does the recursion to find the weaving of the ramaining 
		of the list excluding the first char of the first list """
	sufix_weaving: List[List[int]] = weave(first[1:], second)
	result: List[List[int]] = []
	for weaved in sufix_weaving:
		result.append([first[0]] + weaved)  # linked list would be better
	return result
		

import pdb;pdb.set_trace()
