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

left 0, 1
mid 1, 0
right -1, 0


[]


"""
import collections
import enum
from typing import Dict, Optional


StackMetadata = collections.namedtuple('StackMetadata', ['end', 'size'])


class StackType(enum.Enum):
	left = 1
	mid = 2
	right = 3


class ActionType(enum.Enum):
	insert = 1
	remove = 2


class TripleStack:

	def __init__(self):
		empty_metadata: StackMetadata = StackMetadata(-1, 0)
		self.stacks: Dict[str, StackMetadata] = collections.defaultdict(lambda: empty_metadata)
		self.array: List[int] = []

	def peek(self, stack_type: StackType) -> int:
		if self.stacks[stack_type.name].size == 0:
			raise IndexError('Stack is empty')
		return self.array[self.stacks[stack_type.name].end]
		
	def append(self, type_: StackType, value: int) -> None:
		is_empty: bool = self.stacks[type_.name].size == 0
		if is_empty:
			self.initialize_stack(type_) 
		self.array.insert(self.stacks[type_.name].end + 1, value)
		self.update_metadata(ActionType.insert, type_, first=is_empty)

	def pop(self, type_: StackType) -> int:
		if self.stacks[type_.name].size == 0:
			raise IndexError('Stack is empty')
		value: int = self.array.pop(self.stacks[type_.name].end)
		self.update_metadata(ActionType.remove, type_)
		return value
		
	def initialize_stack(self, stack_type: StackType) -> None:
		""" Initialize empty stacks on the right position """

		# Gets previous stack on the array if not the first stack 
		previous_stack: Optional[StackMetadata] = (self.stacks[StackType(stack_type.value - 1).name] 
 												   if stack_type.value > 1 else None)
		if not previous_stack:
			self.stacks[stack_type.name] = StackMetadata(-1, 0)
			return
		self.stacks[stack_type.name] = StackMetadata(previous_stack.end + 1, 0)
	

	def update_metadata(self, action: ActionType, stack_type: StackType, first: bool = False) -> None:
		""" Updates pointers on metadata """
		curr_metadata: StackMetadata = self.stacks[stack_type.name]
		if first:
			self.stacks[stack_type.name] = StackMetadata(curr_metadata.end, 1)
			return
		if action == ActionType.insert:
			self.stacks[stack_type.name] = StackMetadata(curr_metadata.end + 1, 
														 curr_metadata.size + 1)
		elif action == ActionType.remove:
			self.stacks[stack_type.name] = StackMetadata(curr_metadata.end - 1, 
														 curr_metadata.size - 1)





import pdb;pdb.set_trace()


	
