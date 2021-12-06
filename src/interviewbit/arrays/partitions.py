"""
Problem Description

You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n]) 


In - numbers: List[int]
Out - int

[1, 2, 3, 0, 3]
 1  3  6  6  9  # Prefix
 9  8  6  3  3  # sufix
whole sum = 9

mid starts at 1 ends 2


build prefix and sufix dictionaries, from sum to index
iterate on one of them and find matches on the other that are with index bigger than curr + 1 
check if the values are the same and that their sum minus the total equals them selves

0: 1
1: 3


O(n*m) time complexity where n is the size of numbers and m is the amount of possible sums
O(n) space complexity where n is the size of numbers


"""
import collections
from typing import List, Dict


def partitions(numbers: List[int]) -> int:
	if not numbers:
		return 0
	prefix: List[int] = build_prefix(numbers) 
	suffix_to_index: Dict[int, List[int]] = build_suffix_equivalency(
		numbers
	) 
	total_sum: int = sum(numbers)
	count: int = 0
	for curr_index, curr_sum in enumerate(prefix):
		if curr_sum not in suffix_to_index:
			continue
		# Iterates on the places that the prefix sum is equal the curr sum
		for index in suffix_to_index[curr_sum]:
			# Case that there would be no space for mid partition
			if index <= curr_index + 1:
				continue
			# Case that the three partitions are the same
			if curr_sum * 3 == total_sum:
				count += 1
	return count


def build_prefix(numbers: List[int]) -> List[int]:
	prefix: List[int] = []
	last: int = 0
	for number in numbers:
		prefix.append(number + last)
		last = number + last
	return prefix


def build_suffix_equivalency(
	numbers: List[int]
) -> Dict[int, List[int]]:
	equivalency: Dict[int, List[int]] = collections.defaultdict(list)
	last: int = 0
	for index, number in enumerate(reversed(numbers)):
		equivalency[number + last].append(len(numbers)-1-index)
		last = number + last
	return equivalency
	



