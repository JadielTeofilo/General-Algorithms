"""
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different

Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1

In - number: int


372512

iterate backwards
2
add curr - 2
1
add curr and add the product with the elements to the right

					[[5], []]	[[1], [2]]	[[2]]



"""

import dataclasses
from typing import List, Iterable, Set


@dataclasses.dataclass
class Subset:

	values: List[int] = dataclasses.field(default_factory=list)
	product: int = 1  # TODO check it wont aftect result

	def copy(self):
		return Subset(values=self.values.copy(), product=self.product)


class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, number: int) -> int:
		if number < 0:
			number *= -1
		if number < 10:
			return 1
		subsets: List[Subset] = self.generate_subsets(number)
		subsets.pop(0)  # Removes the empty subset
		return 0 if self.repeated_products(subsets) else 1

	def generate_subsets(self, number: int) -> List[Subset]:
		subsets: List[Subset] = [Subset()]
		aux_subsets: List[Subset] = []
		for digit in self.get_digits(number):
			aux_subsets: List[Subset] = [subset.copy() 
										 for subset in aux_subsets + [Subset()]]
			self.fill_subsets(aux_subsets, digit)
			subsets.extend(aux_subsets)
		return subsets

	def fill_subsets(self, subsets: List[Subset], digit: int) -> None:
		for subset in subsets:
			subset.values.append(digit)
			subset.product *= digit

	def repeated_products(self, subsets: List[Subset]) -> bool:
		visited: Set[int] = set()
		for subset in subsets:
			if subset.product in visited:
				return True
			visited.add(subset.product)
		return False
				

	def get_digits(self, number: int) -> Iterable[int]:
		while number > 0:
			yield number % 10
			number //= 10


