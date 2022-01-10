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


Time complexity is at least n*2^n
O(n*n^2) Space complexity 


"""
from typing import Set, List


def power_set(numbers: Set[int]) -> List[Set[int]]:
	""" Finds all subsets of the given set """
	indexed_numbers: List[int] = list(numbers)
	result: List[Set[int]] = []
	
	result.append(set())

	for i in range(0, len(indexed_numbers)):
		subsets: List[Set[int]] = build_subsets(
			result, 
			indexed_numbers[i]
		)
		result.extend(subsets)

	return result


def build_subsets(base_subsets: List[Set[int]], 
				  number: int) -> List[Set[int]]:
	new_subsets: List[Set[int]] = [subset.copy() for subset in base_subsets]
	for subset in new_subsets:
		subset.add(number)
	return new_subsets


"""
Recursive version

Either use the element or dont
1 4 2 3
                                _
            1                                   _
    4               _               4                   _
2       _       2       _       2       _           2       _
3 _     3 _     3 _     3 _    3 _     3  _        3  _    3  _


solve(result: List[List[int]], )
"""




