"""
Min stack


Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

pop:

in - None
out - int

push:

in - int
out - None

min: 

in - None
out - int

O(1) time

python list append and pop

keep track of the min value 

[3 4 ]

2 3 4


3 4 2 
(current, min_till_now)

#############Problem is that wastes too mutch memory repeating values
[(4, 1)]

"""
import collections
import dataclasses
import math
from typing import List, Union


@dataclasses.dataclass
class MinNode:
	value: int
	amount: int


class Stack:

	def __init__(self):
		self.array: List[int] = []
		self.min_values: List[MinNode] = []
	
	def pop(self) -> int:
		if not self.array:
			raise IndexError('Empty stack')
		self.update_current_min_value(-1)
		return self.array.pop()

	def push(self, value: int) -> None:
		current_min: Union[int, float] = self.min() if self.array else math.inf
		if value < current_min:
			self.min_values.append(MinNode(value, 1))
		else:
			self.update_current_min_value(+1)
		self.array.append(value)

	def update_current_min_value(self, change: int) -> None:
		""" Updates value of current min, adding or removing from amount """
		self.min_values[-1].amount += change
		if self.min_values[-1].amount <= 0:
			self.min_values.pop()

	def min(self) -> int:
		if not self.array:
			raise IndexError('EmptyStack')
		return self.min_values[-1].value


asdf = Stack()
import pdb;pdb.set_trace()


	


