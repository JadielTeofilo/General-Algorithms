"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).


1, , , 

"""
from typing import List


class SetOfStacks:

	def __init__(self, max_size: int) -> None:
		self.stacks: List[List[int]] = [[]]
		self.max_size = max_size
		
	def push(self, value: int) -> None:
		self.update_full_stack()  #TODO
		self.stacks[-1].append(value)

	def update_full_stack(self) -> None:
		if len(self.stacks[-1]) == self.max_size:
			self.stacks.append([])

	def pop(self) -> int:
		self.remove_empty_stacks()
		if not self.stacks[-1]:
			raise IndexError('Empty Stack')
		return self.stacks[-1].pop()

	def remove_empty_stacks(self) -> None:
		""" Removes empty stacks at the end of the list """
		while len(self.stacks) > 1:
			if not self.stacks[-1]:
				self.stacks.pop()
			else:
				break



import pdb;pdb.set_trace()
