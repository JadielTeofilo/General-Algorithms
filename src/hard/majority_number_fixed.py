"""
Majority Element: A majority element is an element that makes up more than half of the items in
an array. Given a positive integers array, find the majority element. If there is no majority element,
return -1. Do this in O( N) time and O( 1) space.


In - numbers: List[int]


The way to do it is to validate small bunches of the array
Start with the first element, and walk the array until it is no longer the majority. 
This subarray will no longuer influence in the overall majority, since it wont change its balance

After we finish the whole array we might have a candidate, or not 
If we do, we validate it.

O(n) time complexity where n is the size of the input


"""
from typing import List, Optional


def majority_element(numbers: List[int]) -> int:
	# TODO validate input
	candidate: Optional[int] = find_candidate(numbers)
	return validated_candidate(numbers, candidate)


def find_candidate(numbers: List[int]) -> Optional[int]:
	validating_index: int = 0
	while validating_index < len(numbers):
		target: int = numbers[validating_index]
		target_delta: int = 1
		neighbor: int = validating_index + 1
		while neighbor < len(numbers):
			if target != numbers[neighbor]:
				target_delta -= 1
			else:
				target_delta += 1		
			if target_delta == 0:
				# Target is not majority, skip to next subarray
				validating_index = neighbor + 1
				break
			neighbor += 1
		# Case when the neighbor went through the whole array
		if target_delta != 0:
			return target
	return None


def validated_candidate(numbers: List[int], 
						candidate: int) -> int:
	return (candidate 
		    if numbers.count(candidate) > (len(numbers) // 2) 
			else -1)


print(majority_element([1,5,9,2,9,9,9]))
