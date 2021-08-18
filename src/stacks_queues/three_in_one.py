"""

Describe how you could use a single array to implement three stacks.

What are the requirements for the three stacks, should they have 0(1) pop and insert

[1]

first (start, end, size)
second (start, end, size)
third (start, end, size)

append(type, value)

pop(type)

peek(type)

[(0, data), (1, data), (2, data)]


"""
import collections
from typing import Dict


StackMetadata = collections.namedtuple('StackMetadata', ['start', 'end', 'size'])


class TripleStack:

	def __init__(self):
		empty_metadata: StackMetadata = StackMetadata(None, None, 0)
		self.stacks: Dict[str, StackMetadata] = collections.defaultdict(empty_metadata)
		self.array: List[int] = []

	def append(self, type_: StackType, value: int) -> None:  # TODO StackType
		if self.stacks[type_].size == 0:
			self.initialize_stack(type_)  # TODO
		self.array.insert(self.stack[type_].end, value)
		self.update_metadata(ActionType.insert, self.stack[type_].end) # TODO update and ActioType
		
