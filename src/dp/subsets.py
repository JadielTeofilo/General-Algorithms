"""
Power Set: Write a method to return all subsets of a set.

Set of integers?
Yes

In - numbers: Set[int]

Out: List[Set[int]]

{1 2 3}

{}
{1} {2} {3} 
{1 2} {1 3} {3 2}

build sets (size, values, result, curr_subset)
	
	bs(size - 1, values.diff(value), result, curr_subset.union(value))


Time complexity is at least n*2^N
O(n^2) Space complexity 


"""
from typing import Set, List


def power_set(numbers: Set[int]) -> List[Set[int]]:
	""" Finds all subsets of the given set """
	indexed_numbers: List[int] = list(numbers)
	result: List[Set[int]] = []
	
	result.append(set())
	last_size_subsets: List[Set[int]] = [set()]

	for i in range(0, len(indexed_numbers)):
		subsets: List[Set[int]] = build_subsets(
			last_size_subsets, 
			indexed_numbers[i]
		)
		last_size_subsets = subsets
		result.extend(subsets)

	return result


def build_subsets(base_subsets: List[Set[int]], 
				  number: int) -> List[Set[int]]:
	new_subsets: List[Set[int]] = [subset.copy() for subset in base_subsets]
	for subset in new_subsets:
		subset.add(number)
	return base_subsets + new_subsets


import pdb;pdb.set_trace()
