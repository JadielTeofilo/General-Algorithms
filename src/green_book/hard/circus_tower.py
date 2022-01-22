"""
Circus Tower: A circus is designing a tower routine consisting of people standing atop one another's
shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than
the person below him or her. Given the heights and weights of each person in the circus, write a
method to compute the largest possible number of people in such a tower.

In - people: List[Person]
Out - int

 kg   cm
(70, 180)
(80, 170)
(59, 150)
(69, 160)

Brute force will test all possibilities

Stacks of people starting from each person


		70 				80				59			 69
	59     60			70 59 69		-			59


That will be n^2 time complexity (with memoization we will have n nodes each doing n operations)


(59, 150) (69, 160) (68, 180) (80, 170) 
sorting helps you to just go through the list 

"""
import collections
from typing import List, Dict


Person = collections.namedtuple('Person', 'height weight')


def circus_tower(people: List[Person]) -> int:
	# TODO validate empty input
	cache: Dict[Person, int] = {}
	people.sort()  # Minor optimization
	people.reverse()  # Have the biggest heights first
	return circus_tower_helper(
		people, cache, index=0, 
	)

# TODO Fix this, its flawed, should follow a combinations implementation
def circus_tower_helper(
	people: List[Person], 
	cache: Dict[Person, int], 
	index: int
) -> int:
	curr_person: Person = people[index]
	if curr_person in cache:
		return cache[curr_person]
	max_size: int = 0
	for next_index in range(index + 1, len(people)):
		if is_valid(curr_person, people[next_index]):
			max_size = max(
				max_size, 
				circus_tower_helper(people, cache, next_index)
			)
	cache[curr_person] = curr_person.height + max_size
	return cache[curr_person]
		

def is_valid(left_person: Person, right_person: Person) -> bool:
	return (right_person.height < left_person.height and 
			right_person.weight < left_person.weight)


print(circus_tower(
[
Person(1, 8),
Person(2, 3),
Person(5, 1),
Person(2, 1),
Person(7, 4),
Person(8, 1),
]
))

