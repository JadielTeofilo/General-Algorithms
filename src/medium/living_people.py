"""
Living People: Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. You may assume that all people were born
between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should be included in that year's count. For example, Person (birth = 1908, death = 1909) is included in the counts for both 1908 and 1909.


This problem is basically finding a number that crosses the most ranges. We can sort the ranges to make that easier 


The brute force approach goes on every year from the range and checks all people

another way is to sort the births and deaths sepparetly, go through them keeping track of how many people are alive O(p log p) p being the amount of people

another way is to use a map to keep track of how many lives are added each year O(p+k) p being the amount of people k being the range size


It could be resulting in more than one year, should i return anyone?
yup

In - List[Person], range: Range
Out - year: int
"""
import collections
from typing import List, Dict


Person = collections.namedtuple('Person', 'birth death')
Range = collections.namedtuple('Range', 'start end')


def living_people(people: List[Person], years_range: Range) -> int:
	""" Finds the year with the most amount of people """
	new_lives: Dict[int, int] = collections.defaultdict(int)
	fill_new_lives(new_lives, people)
	current_lives: int = 0
	max_lives: int = 0
	desired_year: int = -1
	for year in range(years_range.start, years_range.end + 1):
		current_lives += new_lives[year]
		if current_lives > max_lives:
			desired_year = year
		max_lives = max(max_lives, current_lives)
	return desired_year


def fill_new_lives(new_lives: Dict[int, int], 
				   people: List[Person]) -> None:
	for person in people:
		new_lives[person.birth] += 1
		new_lives[person.death + 1] -= 1


people = [
	Person(4, 9),
	Person(3, 3),
	Person(1, 3),
	Person(4, 4),
	Person(4, 10),
]
range_ = Range(1, 10)

print(living_people(people, range_))


