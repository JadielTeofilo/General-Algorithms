"""
There is a rod of length N lying on x-axis with its left end at x = 0 and right end at x = N. Now, there are M weak points on this rod denoted by positive integer values(all less than N) A1, A2, …, AM. You have to cut rod at all these weak points. You can perform these cuts in any order. After a cut, rod gets divided into two smaller sub-rods. Cost of making a cut is the length of the sub-rod in which you are making a cut.

Your aim is to minimise this cost. Return an array denoting the sequence in which you will make cuts. If two different sequences of cuts give same cost, return the lexicographically smallest.


1 | 2 | 3 4 5 | 6

1 2 5

Brute force

try cutting on every position and call the recursion on it

iterate on cut positions, and call solve on the new start, end

memoize the start, end position

O(n^2*m) time complexity where n is the size of the list and m is the size of cuts


In - cuts: List[int], size: int
Out - List[int]

"""
import math
from typing import List


class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return a list of integers
	def rodCut(self, size: int, cuts: List[int]) -> int:
		return self.get_best_cuts(1, size, cuts, {})[1]


	def get_best_cuts(self, start: int, end: int, cuts: List[int], 
					  cache: Dict[int, int]) -> Tuple[int, List[int]]:
		if start >
		best_cuts: List[int] = []
		min_cost: Union[int, float] = math.inf
		for cut in cuts:
			if cut < start or cut > end:
				continue
			new_cost, path = self.get_best_cuts(start=start, end=cut)

