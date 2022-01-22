"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

1 4 5
4 5
5 2 3





O(N^3*2^N) Time complexity
Desconsiderando a concatenação de lista




"""
from typing import List, Optional
import dataclasses


@dataclasses.dataclass
class Node:
	value: int
	left: Optional['Node'] = None
	right: Optional['Node'] = None


def possible_sequences(root: Node) -> List[List[int]]:
	if not root:
		return [[]]
	left_sequences: List[List[int]] = possible_sequences(root.left)
	right_sequences: List[List[int]] = possible_sequences(root.right)
	sequences: List[List[int]] = weave_sequences(left_sequences, right_sequences)
	return [[root.value] + sequence for sequence in sequences]
	

def weave_sequences(left_sequences: List[List[int]], 
					right_sequences: List[List[int]]) -> List[List[int]]:
	""" Weaves all possible combinations between the two list of lists """
	result: List[List[int]] = []
	for left_sequence in left_sequences:
		for right_sequence in right_sequences:
			result.extend(weave(right_sequence, left_sequence))
	return result


def weave(left: List[int], right: List[int]) -> List[List[int]]:
	""" Finds all possible combinations of left and right 
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
