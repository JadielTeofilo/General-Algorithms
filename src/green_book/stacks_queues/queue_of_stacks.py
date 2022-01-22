"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks


Methods

push

in  int
out None 

popleft

in None

out int

---------

1 2 3

1
2
3

[]
[3 2 1]

O(1) insertion
O(1) retrival amortized


1
2

"""
from typing import List


class Queue:

	def __init__(self) -> None:	
		self.in_stack: List[int] = []
		self.out_stack: List[int] = []

	def push(self, value: int) -> None:
		self.in_stack.append(value)

	def pop_left(self) -> int:
		if self.out_stack:
			return self.out_stack.pop()
		self.update_out_stack()  # TODO
		if not self.out_stack:
			raise IndexError('Empty Queue')
		return self.out_stack.pop()

	def update_out_stack(self) -> None:
		""" Move elements from in_stack to out_stack """
		while self.in_stack:
			self.out_stack.append(self.in_stack.pop())


if __name__ == '__main__':
	queue: Queue = Queue()
	queue.push(1)
	queue.push(2)
	queue.push(3)
	queue.push(4)
	import pdb;pdb.set_trace()

