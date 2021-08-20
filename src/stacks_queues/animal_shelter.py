"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintai n this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in LinkedList data structure.

push (enqueue) 

in Animal
out None


pop_left

in AnimalType
out Any


Can use two queues
cats [1, 3, 7]
dogs [2, 4, 6]

insertion O(1)
pop O(M)
M = amount of types

"""
import dataclasses
from typing import Any, Optional, Union
import enum
import math
import collections


class AnimalType(enum.Enum):
	dog = 1
	cat = 2
	anyone = 3


@dataclasses.dataclass
class Animal:
	type_: AnimalType
	sequence: Optional[int] = None


@dataclasses.dataclass
class Node:
	value: Any
	next: Optional['Node'] = None


class Queue:
	
	def __init__(self) -> None: 
		self.start: Optional[Node] = None
		self.end: Optional[Node] = None

	def push(self, value: Any) -> None:
		if not self.start:
			self.start = Node(value)
			self.end = self.start
		else:
			self.end.next = Node(value)
			self.end = self.end.next
		
	def pop_left(self) -> Any:
		if not self.start:
			raise IndexError('Empty queue')
		value: Any = self.start.value
		if self.start == self.end:
			self.end = None
		self.start = self.start.next
		return value

	def peek(self) -> Any:
		if not self.start:
			raise IndexError('Empty queue')
		return self.start.value


class AnimalShelter:

	def __init__(self) -> None:
		self.animals: Dict[AnimalType, Queue] = collections.defaultdict(Queue)
		self.sequence_number: int = 0  # Keeps track of who got here first
		
	def push(self, animal: Animal) -> None:
		self.sequence_number += 1
		animal.sequence = self.sequence_number
		self.animals[animal.type_].push(animal)

	def pop_left(self, animal_type: AnimalType) -> Animal:
		if not self.animals:
			raise ValueError('Empty shelter')
		if animal_type == AnimalType.anyone:
			return self.pop_oldest()
		if not self.animals.get(animal_type):
			raise ValueError('No such animal on the shelter')
		return self.animals[animal_type].pop_left()

	def pop_oldest(self) -> Animal:
		""" Compares Animal queues from diff types to get the oldest """
		older_type: Optional[AnimalType] = None
		min_sequence: Union[int, float] = math.inf
		for animal_type, animal_queue in self.animals.items():
			if not animal_queue.start:  # REALLY IMPORTANT
				continue
			animal: Animal = animal_queue.peek()
			if min_sequence > animal.sequence:
				min_sequence = animal.sequence
				older_type = animal_type
		return self.animals[older_type].pop_left()


if __name__ == '__main__':

	shelter = AnimalShelter()
	shelter.push(Animal(AnimalType.dog))
	shelter.push(Animal(AnimalType.cat))
	shelter.push(Animal(AnimalType.cat))
	shelter.push(Animal(AnimalType.dog))
	import pdb;pdb.set_trace()


