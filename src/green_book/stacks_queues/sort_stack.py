"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array) . The stack supports the following operations: push, pop, peek, and isEmpty



in: Stack

out Stack (sorted)


Is it a stack of integers?
yes
should it be a stable sorting?
no, but how would you do it
are there going to be repeated elements?
yes

[2 1 4]

[5 4]


O(N) space
O(N*N) time


"""
from typing import List


def sort_stack(stack: List[int]) -> List[int]:
	aux_stack: List[int] = []
	
	while stack:
		item: int = stack.pop()
		insert_into_new_stack(item, old_stack=stack, 
							  new_stack=aux_stack)
	
	return aux_stack


def insert_into_new_stack(item: int, old_stack: List[int], 
						  new_stack: List[int]) -> None:
	""" 
	Finds sorted place on the new stack to insert item 

	As a side effect the old stack might receive items that 
	are smaller than the current item
	"""
	while new_stack:
		if new_stack[-1] >= item:
			new_stack.append(item)
			break
		old_stack.append(new_stack.pop())
	else:  # Case it does not find a place
		new_stack.append(item)


if __name__ == '__main__':
	print(sort_stack([3,4,2,1,4,5]))
